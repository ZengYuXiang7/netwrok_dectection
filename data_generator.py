import pandas as pd
from collections import defaultdict
from datetime import datetime
import multiprocessing
import csv
import os
import glob
import pyshark

# 处理每个数据包的函数
def process_packet(packet):
    try:
        timestamp = packet.sniff_time
        source_ip = packet.ip.src
        destination_ip = packet.ip.dst
        if 'TCP' in packet:
            source_port = packet.tcp.srcport
            destination_port = packet.tcp.dstport
            protocol = 'TCP'
        elif 'UDP' in packet:
            source_port = packet.udp.srcport
            destination_port = packet.udp.dstport
            protocol = 'UDP'
        else:
            return None

        length = packet.length
        all_info = [timestamp.timestamp(), source_ip, destination_ip, source_port, destination_port, protocol, length]
        return all_info
    except AttributeError:
        return None

def write_to_csv(writer, data):
    writer.writerow(data)

def process_pcap(pcap_file, csv_file):
    os.makedirs(os.path.dirname(csv_file), exist_ok=True)
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Source IP", "Destination IP", "Source Port", "Destination Port", "Protocol", "Length"])
        packets = pyshark.FileCapture(pcap_file, display_filter='tcp or udp', keep_packets=False)
        i = 0
        for packet in packets:
            packet_info = process_packet(packet)
            if packet_info:
                write_to_csv(writer, packet_info)
                i += 1
            # if i >= 10000:
            #     break
        packets.close()

# 处理单个PCAP文件的函数，移到全局范围
def process_single_pcap(pcap_file, csv_dir):
    # 获取文件大小并转换为MB
    file_size = os.path.getsize(pcap_file)
    file_size_mb = file_size / (1024 ** 2)  # 转换为 MB
    base_name = os.path.splitext(os.path.basename(pcap_file))[0]
    csv_file = os.path.join(csv_dir, base_name + '.csv')
    print(f"Processing pcap file: {pcap_file} (Size: {file_size_mb:.2f} MB)")
    process_pcap(pcap_file, csv_file)
    print(f"Converted pcap file to csv: {csv_file}")

def process_pcap_files_in_directory(dataset):
    os.makedirs('./datasets/csv/', exist_ok=True)
    input_dir = os.path.join('./datasets', 'pcap', dataset)
    csv_dir = os.path.join('./datasets', 'csv', dataset)
    input_pattern = os.path.join(input_dir, '*.pcap')
    pcap_files = glob.glob(input_pattern)
    print(f"Total pcap files to process: {len(pcap_files)}")
    # 创建一个进程池
    with multiprocessing.Pool(processes=6) as pool:
        pool.starmap(process_single_pcap, [(pcap_file, csv_dir) for pcap_file in pcap_files])  # 使用starmap传递额外参数

def csv_to_flow(csv_file, time_interval):
    if not type(csv_file) == pd.core.frame.DataFrame:
        df = pd.read_csv(csv_file)
    else:
        df = csv_file

    # 创建一个字典存储流
    flows = defaultdict(list)

    for _, row in df.iterrows():
        raw_timestamp = row['Timestamp']
        src_ip, dst_ip = row['Source IP'], row['Destination IP']
        src_port, dst_port = row['Source Port'], row['Destination Port']
        protocol = row['Protocol']
        packet_length = row['Length']

        # 规范化流标识符
        flow_key = (src_ip, src_port, dst_ip, dst_port, protocol)
        reverse_flow_key = (dst_ip, dst_port, src_ip, src_port, protocol)

        # 判断流的方向：正向流或反向流
        visited = False
        if (0, flow_key) in flows:  # 如果当前流已经在流字典中，说明是正向流
            packet_length = packet_length  # 正向流，包长度不变
            flag = True
            visited = True
        elif (0, reverse_flow_key) in flows:  # 如果反向流已存在，说明包是反向流
            packet_length = -packet_length  # 反向流，包长度取负值
            flag = False
            visited = True
        else:
            flag = True
        now_flow_key = flow_key if flag else reverse_flow_key
        # print('-' * 100)
        i = 0
        if visited:
            # 循环判断当前流的时间间隔
            while True:
                # print(f'当前是 第{i}个流')
                now_key = (i, now_flow_key)
                # print(now_flow_key)
                # 判断当前流的时间间隔是否符合要求
                # print(now_key)
                # print(flows[now_key])
                # print(flows[now_key][0])
                if raw_timestamp - flows[now_key][0][0] <= time_interval:
                    # 符合时间间隔要求，添加包到当前流
                    flows[now_key].append([raw_timestamp, now_flow_key, packet_length])
                    break  # 成功处理后退出循环
                else:
                    # 如果时间间隔不符合要求，打印并尝试下一个流
                    # print(f'超出了当前流时间间隔: {now_key} -- {raw_timestamp - flows[now_key][0][0]}')
                    i += 1
                    if (i, now_flow_key) not in flows:
                        flows[(i, now_flow_key)].append([raw_timestamp, now_flow_key, packet_length])
                        # print(f'插入到新的流 {i} -- {now_flow_key}')
                        break
                    else:
                        # 遍历下一个流
                        continue
        else:
            now_key = (i, now_flow_key)
            flows[now_key].append([raw_timestamp, now_flow_key, packet_length])
            # print(f'创建新的流 {i} -- {now_flow_key}')

    # 查看流的结果
    # for flow_key, flow_data in flows.items():
    #     flow_id, flow_five_info = flow_key
    #     print(flow_id, flow_five_info)
    #     for packet in flow_data:
    #         print(f"    Packet: {packet}")
    return flows


if __name__ == '__main__':
    inputs = input('read or split: ')
    if inputs == 'read':
        # process_pcap_files_in_directory('IoT')
        process_pcap_files_in_directory('Medboit')
        # process_pcap_files_in_directory('Device')
    elif inputs == 'split':
        time_interval = 10
        all_flows = csv_to_flow("./datasets/csv/IoT/github.csv", time_interval)
        print(len(all_flows))


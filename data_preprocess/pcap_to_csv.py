# coding : utf-8
# Author : Yuxiang Zeng
import concurrent
import os
import glob
import pyshark
import pandas as pd
from tqdm import *

# 处理每个数据包的函数
def process_packet(packet):
    try:
        # 提取五元组信息
        timestamp = packet.sniff_time  # 获取时间戳
        source_ip = packet.ip.src  # 源IP
        destination_ip = packet.ip.dst  # 目标IP

        # 对于TCP/UDP协议，提取源端口和目标端口
        if 'TCP' in packet:
            source_port = packet.tcp.srcport  # 源端口
            destination_port = packet.tcp.dstport  # 目标端口
            protocol = 'TCP'
        elif 'UDP' in packet:
            source_port = packet.udp.srcport  # 源端口
            destination_port = packet.udp.dstport  # 目标端口
            protocol = 'UDP'
        else:
            return None  # 如果不是 TCP 或 UDP，则跳过

        length = packet.length  # 数据包的总长度
        all_info = [timestamp.timestamp(), source_ip, destination_ip, source_port, destination_port, protocol, length]
        # print(all_info)
        return all_info
    except AttributeError:
        print('Error')
        return None  # 如果解析失败，返回 None


# 保存数据到 CSV
def save_to_csv(data, csv_file):
    # 将数据转换为 DataFrame
    df = pd.DataFrame(data, columns=["Timestamp", "Source IP", "Destination IP", "Source Port", "Destination Port", "Protocol", "Length"])

    # 将 Timestamp 转换为 pandas datetime 格式，以便排序
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])

    # 按照时间戳升序排序
    df = df.sort_values(by='Timestamp')

    # 保存为 CSV 文件
    df.to_csv(csv_file, index=False)


# 处理抓包文件
def process_pcap(pcap_file, csv_file):
    os.makedirs(os.path.dirname(csv_file), exist_ok=True)
    packets = pyshark.FileCapture(pcap_file, display_filter='tcp or udp')
    result_list = []
    for packet in tqdm(packets):
        result_list.append(process_packet(packet))
    save_to_csv(result_list, csv_file)


def process_pcap_files_in_directory(dataset):
    """
    遍历指定文件夹中的所有pcap文件，并将其转换为csv文件
    """
    input_dir = os.path.join('../datasets', 'pcap', dataset)
    csv_dir = os.path.join('../datasets', 'csv', dataset)
    input_pattern = os.path.join(input_dir, '*.pcap')  # 匹配所有.pcap文件
    pcap_files = glob.glob(input_pattern)  # 获取所有匹配的pcap文件
    for pcap_file in pcap_files:
        base_name = os.path.splitext(os.path.basename(pcap_file))[0]
        if base_name == 'sogou':
            csv_file = os.path.join(csv_dir, base_name + '.csv')
            print(f"Preprocess pcap file : {pcap_file}")
            process_pcap(pcap_file, csv_file)
            print(f"Converted pcap file to csv: {csv_file}")
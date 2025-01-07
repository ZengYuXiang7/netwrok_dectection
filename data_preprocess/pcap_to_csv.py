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
            if i >= 10000:
                break
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
    input_dir = os.path.join('./datasets', 'pcap', dataset)
    csv_dir = os.path.join('./datasets', 'csv', dataset)
    input_pattern = os.path.join(input_dir, '*.pcap')
    pcap_files = glob.glob(input_pattern)

    print(f"Total pcap files to process: {len(pcap_files)}")

    # 创建一个进程池
    with multiprocessing.Pool(processes=6) as pool:
        pool.starmap(process_single_pcap, [(pcap_file, csv_dir) for pcap_file in pcap_files])  # 使用starmap传递额外参数
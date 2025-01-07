# coding : utf-8
# Author : Yuxiang Zeng
import concurrent
import csv
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
        return all_info
    except AttributeError:
        print('Error')
        return None  # 如果解析失败，返回 None


# 逐行写入 CSV
def write_to_csv(writer, data):
    writer.writerow(data)


# 处理抓包文件
def process_pcap(pcap_file, csv_file):
    os.makedirs(os.path.dirname(csv_file), exist_ok=True)

    # 打开 CSV 文件，保持文件处于打开状态
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Source IP", "Destination IP", "Source Port", "Destination Port", "Protocol", "Length"])

        # 读取 pcap 文件
        packets = pyshark.FileCapture(pcap_file, display_filter='tcp or udp', keep_packets=False)  # 使用流式处理，避免一次性加载所有包

        # 逐个处理数据包并写入 CSV
        for packet in packets:
            packet_info = process_packet(packet)
            if packet_info:
                write_to_csv(writer, packet_info)


def process_pcap_files_in_directory(dataset):
    """
    遍历指定文件夹中的所有 pcap 文件，并将其转换为 csv 文件
    """
    input_dir = os.path.join('./datasets', 'pcap', dataset)
    csv_dir = os.path.join('./datasets', 'csv', dataset)
    input_pattern = os.path.join(input_dir, '*.pcap')  # 匹配所有 .pcap 文件
    pcap_files = glob.glob(input_pattern)  # 获取所有匹配的 pcap 文件

    for pcap_file in pcap_files:
        # 获取文件大小并转换为 MB
        file_size = os.path.getsize(pcap_file)
        file_size_mb = file_size / (1024 ** 2)  # 转换为 MB

        base_name = os.path.splitext(os.path.basename(pcap_file))[0]
        csv_file = os.path.join(csv_dir, base_name + '.csv')

        print(f"Processing pcap file: {pcap_file} (Size: {file_size_mb:.2f} MB)")
        process_pcap(pcap_file, csv_file)
        print(f"Converted pcap file to csv: {csv_file}")



def process_pcap_files_in_directory(dataset):
    """
    遍历指定文件夹中的所有pcap文件，并将其转换为csv文件
    """
    input_dir = os.path.join('./datasets', 'pcap', dataset)
    csv_dir = os.path.join('./datasets', 'csv', dataset)
    input_pattern = os.path.join(input_dir, '*.pcap')  # 匹配所有.pcap文件
    pcap_files = glob.glob(input_pattern)  # 获取所有匹配的pcap文件

    # 定义处理单个PCAP文件的函数
    def process_single_pcap(pcap_file):
        # 获取文件大小并转换为MB
        file_size = os.path.getsize(pcap_file)
        file_size_mb = file_size / (1024 ** 2)  # 转换为 MB
        base_name = os.path.splitext(os.path.basename(pcap_file))[0]
        csv_file = os.path.join(csv_dir, base_name + '.csv')
        print(f"Processing pcap file: {pcap_file} (Size: {file_size_mb:.2f} MB)")
        process_pcap(pcap_file, csv_file)
        print(f"Converted pcap file to csv: {csv_file}")

    # 使用 ProcessPoolExecutor 进行并行处理
    with concurrent.futures.ThreadPoolExecutor(max_workers=16) as executor:
        executor.map(process_single_pcap, pcap_files)  # 使用map来并行处理多个pcap文件
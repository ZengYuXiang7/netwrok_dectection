import os
import glob
import pyshark
import csv
import logging


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

log = logging.getLogger(__name__)


def pcap_to_csv(pcap_file, csv_file, time_interval):
    """
    将pcap文件转换为csv文件,提取五元组、数据包真实长度和时间戳
    """
    # 创建CSV文件并写入表头
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        
        # 使用pyshark读取pcap文件
        log.debug('before cap')
        cap = pyshark.FileCapture(pcap_file, display_filter='ip')  # 使用过滤器提取IP层的数据包
        #cap = pyshark.FileCapture(pcap_file)  # 使用过滤器提取IP层的数据包
        log.debug('after cap')
        first_timestamp = None #第一个数据包的时间戳
        writer.writerow(["timestamp", "source_ip", "destination_ip", "source_port", "destination_port", "protocol", "length"])
        for packet in cap:
            # 提取五元组信息
            try:
                # 获取IP层的信息
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
                    source_port = destination_port = 'N/A'  # 如果不是TCP/UDP，端口设置为N/A
                    protocol = packet.highest_layer  # 使用最高层协议（如ICMP）

                # 获取数据包的真实长度
                length = packet.length  # 数据包的总长度
                
                if first_timestamp is None:
                    first_timestamp = timestamp  # 第一个数据包的时间戳
                
                # 计算与第一个包的时间戳差值（单位：秒）
                time_diff = (timestamp - first_timestamp).total_seconds()
                if time_diff > time_interval: 
                    break
                
                # 写入数据到CSV
                writer.writerow([time_diff, source_ip, destination_ip, source_port, destination_port, protocol, length])
            except AttributeError:
                # 如果包中缺少某些属性（如非IP包），跳过
                continue
        cap.close()
    f.close()

def process_pcap_files_in_directory(input_dir, csv_dir, time_interval):
    """
    遍历指定文件夹中的所有pcap文件，并将其转换为csv文件
    """
    input_pattern = os.path.join(input_dir, '*.pcap')  # 匹配所有.pcap文件
    pcap_files = glob.glob(input_pattern)  # 获取所有匹配的pcap文件

    # with concurrent.futures.ThreadPoolExecutor() as executor:
    #     futures = []
    for pcap_file in pcap_files:
        print(f"Processing pcap file: {pcap_file}")
        output_dir = csv_dir + f'{time_interval}s/'
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
        
        # 获取不带扩展名的文件名
        base_name = os.path.splitext(os.path.basename(pcap_file))[0]
        
        # 构建csv文件的输出路径（与pcap文件同名，但扩展名为.csv）
        csv_file = os.path.join(output_dir, base_name + '_' + str(time_interval) + 's' + '.csv')

        # 将pcap文件转换为csv文件
        pcap_to_csv(pcap_file, csv_file, time_interval)
        # futures.append(executor.submit(pcap_to_csv, pcap_file, csv_file))
        
        print(f"Converted pcap file to csv: {csv_file}")

        # concurrent.futures.wait(futures)

def process_single_pcap_file(pcap_file, csv_dir, time_interval):
    output_directory = csv_dir + f'{time_interval}s/'
    csv_file = os.path.join(output_directory, os.path.basename(pcap_file).replace('.pcap', '_' + str(time_interval) + 's.csv'))
    pcap_to_csv(pcap_file, csv_file, time_interval)

if __name__ == '__main__':
    # 将文件夹`././datasets/MedBIoT_pcap/`中的所有pcap文件转换为csv文件
    input_directory = './datasets/MedBIoT_pcap/'    # 输入pcap文件夹路径
    output_directory = './datasets/MedBIoT/csv/'    # 输出csv文件夹路径
    process_single_pcap_file(input_directory, output_directory, 100)
    # process_pcap_files_in_directory(input_directory, output_directory, 10)
    # process_pcap_files_in_directory(input_directory, output_directory, 50)
    # process_pcap_files_in_directory(input_directory, output_directory, 100)
    # process_pcap_files_in_directory(input_directory, output_directory, 500)
    # process_pcap_files_in_directory(input_directory, output_directory, 1000)

from data_preprocess.pcap_to_csv import *
import pandas as pd
from collections import defaultdict
from datetime import datetime


def csv_to_flow(csv_file, time_interval):
    df = pd.read_csv(csv_file)

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
#                         print(f'插入到新的流 {i} -- {now_flow_key}')
                        break
                    else:
                        # 遍历下一个流
                        continue
        else:
            now_key = (i, now_flow_key)
            flows[now_key].append([raw_timestamp, now_flow_key, packet_length])
#             print(f'创建新的流 {i} -- {now_flow_key}')


    # 查看流的结果
    # for flow_key, flow_data in flows.items():
    #     flow_id, flow_five_info = flow_key
    #     print(flow_id, flow_five_info)
    #     for packet in flow_data:
    #         print(f"    Packet: {packet}")
    return flows

if __name__ == '__main__':
    # os.makedirs('./datasets/csv/', exist_ok=True)
    # process_pcap_files_in_directory('Medboit')
    # process_pcap_files_in_directory('IoT')
    # process_pcap_files_in_directory('Device')
    # print('Done!')
    inputs = input('read or split: ')
    if inputs == 'read':
        process_pcap_files_in_directory('IoT')
    elif inputs == 'split':
        for i in range(10):
            all_flows = csv_to_flow("./datasets/csv/IoT/github.csv", i)
            print(len(all_flows))
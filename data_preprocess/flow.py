import os.path

from data_preprocess.data_generator import get_one_datasets
import pandas as pd
from collections import defaultdict
import numpy as np


# 定义五元组的键函数
def create_flow_key(row):
    return (
        row['source_ip'],
        row['destination_ip'],
        row['source_port'],
        row['destination_port'],
        row['protocol']
    )


def split_csv_to_flows(df):
    # 确保数据类型一致（可选，根据需要调整）
    df['timestamp'] = df['timestamp'].astype(float)
    df['length'] = df['length'].astype(int)

    # 创建五元组键
    df['flow_key'] = df.apply(lambda row: create_flow_key(row), axis=1)

    # 按五元组分组
    flows = defaultdict(list)
    for _, row in df.iterrows():
        flow_key = row['flow_key']
        flows[flow_key].append({
            "timestamp": row['timestamp'],
            "length": row['length']
        })

    # 生成流数组
    flows_array = [
        [
            {
                "timestamp": packet["timestamp"],
                "five_tuple": key,
                "length": packet["length"]
            }
            for packet in packets
        ]
        for key, packets in flows.items()
    ]

    # if flows_array:
    #     print("第一条流的信息:")
    #     for i in range(len(flows_array)):
    #         print(f'第{i}条流:')
    #         for packet in flows_array[i]:
    #             print(f"时间戳: {packet['timestamp']}, 五元组: {packet['five_tuple']}, 数据包长度: {packet['length']}")

    return flows_array


def flow_to_item(flows_array):
    all_five_tuple = []
    all_seq = []
    for i in range(len(flows_array)):
        all_five_tuple.append(list(flows_array[i][0]['five_tuple']))
        now_seq = []
        for j in range(len(flows_array[i])):
            now_packet = flows_array[i][j]
            x = now_packet['timestamp']
            y = now_packet['length']
            now_seq.append([x, y])
        all_seq.append(now_seq)
    return all_five_tuple, all_seq


def get_all_input(dataset, time_interval, label):
    csv_file = f'./datasets/MedBIoT_csv/{time_interval}s/{dataset}.csv'
    try:
        df = pd.read_csv(csv_file)
        flows_array = split_csv_to_flows(df)
        all_five_tuple, all_seq = flow_to_item(flows_array)
        assert len(all_five_tuple) == len(all_seq)
    except Exception as e:
        print(e)
        df = get_one_datasets(dataset, time_interval)
        flows_array = split_csv_to_flows(df)
        all_five_tuple, all_seq = flow_to_item(flows_array)
    all_labels = np.zeros(len(all_seq), dtype=np.int32) + int(label)
    # for i in range(len(all_five_tuple)):
    #     print(all_five_tuple[i], all_seq[i], all_labels[i])
    return all_five_tuple, all_seq, all_labels


if __name__ == '__main__':
    print(os.listdir('../datasets/MedBIoT_pcap/'))
    labels = {
        'bashlite_leg': 0,
        'mirai_leg': 0,
        'torii_leg': 0,
        'bashlite_mal_spread_all': 1,
        'bashlite_mal_CC_all': 2,
        'mirai_mal_spread_all': 3,
        'mirai_mal_CC_all': 4,
        'torii_mal_all': 5,
    }
    dataset = 'bashlite_leg'
    all_five_tuple, all_seq, all_labels = get_all_input(dataset, 10, labels[dataset])

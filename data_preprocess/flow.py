import csv
from collections import defaultdict

# 定义五元组的键函数
def create_flow_key(row):
    return (
        row['source_ip'],
        row['destination_ip'],
        row['source_port'],
        row['destination_port'],
        row['protocol']
    )

def split_csv_to_flows(csv_file):
    flows = defaultdict(list)

    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            flow_key = create_flow_key(row)
            flows[flow_key].append({
                "timestamp": float(row['timestamp']),
                "length": int(row['length'])
            })

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

    return flows_array


def flow_to_item(flow_array):
    all_five_tupe = []
    all_seq = []
    for i in range(len(flows_array)):
        all_five_tupe.append(flows_array[i][0]['five_tuple'])
        now_seq = []
        for j in range(len(flows_array[i])):
            now_packet = flows_array[i][j]
            x = now_packet['timestamp']
            y = now_packet['length']
            now_seq.append([x, y])
        all_seq.append(now_seq)
    return all_five_tupe, all_seq


if __name__ == '__main__':
    csv_file = '../datasets/MedBIoT_csv/500s/bashlite_leg.csv'
    flows_array = split_csv_to_flows(csv_file)
    # if flows_array:
    #     print("第一条流的信息:")
    #     for i in range(len(flows_array)):
    #         print(f'第{i}条流:')
    #         for packet in flows_array[i]:
    #             print(f"时间戳: {packet['timestamp']}, 五元组: {packet['five_tuple']}, 数据包长度: {packet['length']}")
    all_five_tupe, all_seq = flow_to_item(flows_array)
    assert len(all_five_tupe) == len(all_seq)
    for i in range(len(all_five_tupe)):
        print(all_five_tupe[i], all_seq[i])

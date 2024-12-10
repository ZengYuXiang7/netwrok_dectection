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

csv_file = './datasets/MedBIoT/csv/10s/bashlite_leg_10s.csv'
flows_array = split_csv_to_flows(csv_file)

if flows_array:
    print("第一条流的信息:")
    for i in range(len(flows_array)):
        print(f'第{i}条流:')
        for packet in flows_array[i]:
            print(f"时间戳: {packet['timestamp']}, 五元组: {packet['five_tuple']}, 数据包长度: {packet['length']}")        

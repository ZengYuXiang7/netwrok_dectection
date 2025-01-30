import subprocess
import os

def split_pcap_by_command(dataset, src_address, label):
    dst_address = f'./datasets/split_cap/{dataset}/{src_address.split('/')[-1].split('.')[0]}'
    cmd = f"mono SplitCap.exe -r {src_address} -s session -o '{dst_address}'"
    # print(cmd)
    # 执行命令
    subprocess.run(cmd, shell=True, check=True)
    pcap_name = src_address.split('/')[-1].split('.')[0]
    x = os.listdir(f'./datasets/split_cap/{dataset}/{pcap_name}')
    y = []
    for i in range(len(x)):
        x[i] = f'./datasets/split_cap/{dataset}/{pcap_name}/' + x[i]
        y.append(label)
    return x, y
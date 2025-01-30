import os

def get_iot():
    all_address, all_label = [], []
    add = os.listdir(f'./datasets/pcap/IoT')
    for i in range(len(add)):
        all_address.append('./datasets/pcap/IoT/' + add[i])
        all_label.append(i)
    return all_address, all_label
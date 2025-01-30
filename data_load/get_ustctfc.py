import os

from data_load.split_pcap import split_pcap_by_command
import pickle

def get_ustctfc():
    all_address, all_label = [], []
    benign_address = [item for item in os.listdir('./datasets/pcap/USTC-TFC2016/Benign') if 'pcap' in item]
    for i in range(len(benign_address)):
        benign_address[i] = './datasets/pcap/USTC-TFC2016/Benign/' + benign_address[i]
        all_address.append(benign_address[i])
        all_label.append(i)
        # all_label.append(0)
    # temp = os.listdir('./datasets/pcap/USTC-TFC2016/Benign/Weibo')
    # for i in range(len(temp)):
    #     address_now = './datasets/pcap/USTC-TFC2016/Benign/Weibo/' + temp[i]
    #     all_address.append(address_now)
    #     all_label.append(8)
    #     # all_label.append(0)
    # smb = os.listdir('./datasets/pcap/USTC-TFC2016/Benign/SMB')
    # for i in range(len(smb)):
    #     address_now = './datasets/pcap/USTC-TFC2016/Benign/SMB/' + smb[i]
    #     all_address.append(address_now)
    #     all_label.append(8)
    malware_address = os.listdir('./datasets/pcap/USTC-TFC2016/Malware')
    for i in range(len(malware_address)):
        address_now = './datasets/pcap/USTC-TFC2016/Malware/' + malware_address[i]
        all_address.append(address_now)
        all_label.append(8 + i)

    for i in range(len(all_address)):
        print(all_address[i], all_label[i])
    return all_address, all_label

def get_x_and_y(all_address, all_label):
    try:
        with open('./datasets/split_cap/ustctfc/x.pickle', 'rb') as f:
            all_x = pickle.load(f)
        with open('./datasets/split_cap/ustctfc/y.pickle', 'rb') as f:
            all_y = pickle.load(f)
    except:
        all_x, all_y = [], []
        for i in range(len(all_address)):
            x, y = split_pcap_by_command('ustctfc', all_address[i], all_label[i])
            all_x.extend(x)
            all_y.extend(y)
        with open('./datasets/split_cap/ustctfc/x.pickle', 'wb') as f:
            pickle.dump(all_x, f)
        with open('./datasets/split_cap/ustctfc/y.pickle', 'wb') as f:
            pickle.dump(all_y, f)
    return all_x, all_y
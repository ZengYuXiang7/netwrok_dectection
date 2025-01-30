import os
def get_medboit():
    all_address, all_label = [], []
    benign_address = [item for item in os.listdir('./datasets/pcap/Medboit') if 'pcap' in item]
    cnt = 1
    for i in range(len(benign_address)):
        benign_address[i] = './datasets/pcap/Medboit/' + benign_address[i]
        all_address.append(benign_address[i])
        if 'leg' in benign_address[i]:
            all_label.append(0)
        else:
            all_label.append(cnt)
            cnt += 1

    for i in range(len(all_address)):
        print(all_address[i], all_label[i])
    return all_address, all_label

# coding : utf-8
# Author : yuxiang Zeng
import os

import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from tqdm import *
from utils.config import get_config
import pickle


def temp():
    __author__ = 'dk'

    from flowcontainer.extractor import extract
    import os
    add = './datasets/pcap/IoT/' + os.listdir('./datasets/pcap/IoT')[0]
    print(add)
    result = extract(add, filter='(tcp or udp)', extension=['tls.handshake.certificate'])
    for key in result:
        value = result[key]
        print('Flow {0} info:'.format(key))
        print('src ip:', value.src)
        print('dst ip:', value.dst)
        print('sport:', value.sport)
        print('dport:', value.dport)
        print('payload lengths :', value.payload_lengths)
        print('payload timestamps:', value.payload_timestamps)
        print('ip packets lengths:', value.ip_lengths)
        print('ip packets timestamps:', value.ip_timestamps)
        print('default length sequence:', value.lengths)
        print('default timestamp sequence:', value.timestamps)
        print('extension:', value.extension)
        break

if __name__ == '__main__':
    temp()
    # Experiment Settings, logger, plotter
    # config = get_config()
    # try:
    #     all_interval = pickle.load(
    #         open(f'./datasets/flow/{config.dataset}_all_interval_{config.flow_length_limit}.pickle', 'rb'))
    #     all_seq = pickle.load(
    #         open(f'./datasets/flow/{config.dataset}_all_seq_{config.flow_length_limit}.pickle', 'rb'))
    #     all_labels = pickle.load(
    #         open(f'./datasets/flow/{config.dataset}_all_labels_{config.flow_length_limit}.pickle', 'rb'))
    #     # print(all_interval.shape, all_seq.shape, all_labels.shape)
    #     all_x = np.concatenate([all_interval, all_seq], axis=-1)
    #     # print(x.shape)
    # except Exception as e:
    #     all_flow = os.listdir('./datasets/flow/IoT')
    #     all_interval, all_seq, all_labels = [], [], []
    #     for i in trange(len(all_flow)):
    #         try:
    #             df = pd.read_csv(os.path.join('./datasets/flow/IoT', all_flow[i]))
    #             direction = df['direction']
    #             timestamp = df['Timestamp']
    #             packet_length = df['pktlen'] * direction
    #             x = np.array(packet_length[:config.flow_length_limit])
    #             timestamp = np.array(timestamp[:config.flow_length_limit])
    #             interval = np.diff(timestamp) / 1e9
    #             interval = np.insert(interval, 0, 0)
    #             label = df['tag'][0]
    #             if len(df) == 0:
    #                 continue
    #             if len(x) == config.flow_length_limit:
    #                 all_interval.append(interval)
    #                 all_seq.append(x)
    #                 all_labels.append(label)
    #         except:
    #             continue
    #     all_interval = np.stack(all_interval)
    #     all_interval /= np.max(all_interval)
    #     all_seq = np.stack(all_seq)
    #     all_labels = np.array(all_labels)
    #     from sklearn.preprocessing import LabelEncoder
    #
    #     label_encoder = LabelEncoder()
    #     all_labels = label_encoder.fit_transform(all_labels)
    #     # print(all_interval.shape, all_seq.shape, all_labels.shape)
    #     pickle.dump(all_interval,
    #                 open(f'./datasets/flow/{config.dataset}_all_interval_{config.flow_length_limit}.pickle', 'wb'))
    #     pickle.dump(all_seq,
    #                 open(f'./datasets/flow/{config.dataset}_all_seq_{config.flow_length_limit}.pickle', 'wb'))
    #     pickle.dump(all_labels,
    #                 open(f'./datasets/flow/{config.dataset}_all_labels_{config.flow_length_limit}.pickle', 'wb'))
    #
    # all_info = {
    #     'max_flow_length': config.flow_length_limit,
    #     'max_packet_length': np.max(all_seq),
    #     'num_classes': np.max(all_labels) + 1,
    # }
    # pickle.dump(all_info, open(f'./datasets/flow/{config.dataset}_info_{config.flow_length_limit}.pickle', 'wb'))
    # all_x = np.concatenate([all_interval, all_seq], axis=-1).astype(np.float32)
    # all_y = all_labels
    # print(all_x.shape, all_y.shape)
    # print(np.max(all_seq), np.min(all_seq))
    #
    # from sklearn.preprocessing import MinMaxScaler
    # data_scaler = MinMaxScaler()
    # all_seq = data_scaler.fit_transform(all_seq)
    # print(np.max(all_seq), np.min(all_seq))

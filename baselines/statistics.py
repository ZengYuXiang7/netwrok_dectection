# coding : utf-8
# Author : Yuxiang Zeng


import torch
import torch.nn as nn
import pickle
import numpy as np
from scapy.layers.inet import TCP, IP


class Statistics(torch.nn.Module):
    def __init__(self, config):
        super(Statistics, self).__init__()

        with open(f'./datasets/flow/{config.dataset}_info_{config.flow_length_limit}.pickle', 'rb') as f:
            info = pickle.load(f)
            num_classes = info['num_classes']
        self.fc1 = nn.Linear(39, config.rank)  # 第一层全连接
        self.ln1 = nn.LayerNorm(config.rank)  # 第一层 LayerNorm
        self.act1 = nn.ReLU()  # 第一层激活函数

        self.fc2 = nn.Linear(config.rank, num_classes)
        self.ln2 = nn.LayerNorm(num_classes)
        self.act2 = nn.ReLU()  # 第一层激活函数

    def forward(self, _, x):
        x = self.fc1(x)
        x = self.ln1(x)
        x = self.act1(x)
        x = self.fc2(x)
        x = self.ln2(x)
        y = self.act2(x)
        return y


def get_flow_feature(value):
    # src_ip = value.src
    # dst_ip = value.dst
    # sport = value.sport
    # dport = value.dport
    # fwd_flow, bwd_flow = [], []
    # for pkt in packets:
    #     if TCP in pkt:
    #         # 前向流：源 IP 和目的 IP 匹配
    #         if pkt[IP].src == src_ip and pkt[IP].dst == dst_ip and pkt[TCP].sport == sport and pkt[
    #             TCP].dport == dport:
    #             fwd_flow.append(pkt)
    #         # 后向流：源 IP 和目的 IP 反向匹配
    #         elif pkt[IP].src == dst_ip and pkt[IP].dst == src_ip and pkt[TCP].sport == dport and pkt[
    #             TCP].dport == sport:
    #             bwd_flow.append(pkt)
    # two_way_flow = fwd_flow + bwd_flow

    time_stamp = np.array(value.ip_timestamps)
    ip_length = np.array(value.ip_lengths)
    fwd_time_stamp = time_stamp[ip_length > 0]
    bwd_time_stamp = time_stamp[ip_length < 0]

    # 包到达的时间间隔 13
    fiat_mean, fiat_min, fiat_max, fiat_std = packet_iat(fwd_time_stamp)
    biat_mean, biat_min, biat_max, biat_std = packet_iat(bwd_time_stamp)
    diat_mean, diat_min, diat_max, diat_std = packet_iat(time_stamp)
    diat_total = duration = round(time_stamp[-1] - time_stamp[0] + 0.0001, 6)

    # 拥塞窗口大小特征 15
    # fwin_total, fwin_mean, fwin_min, fwin_max, fwin_std = packet_win(fwd_flow)
    # bwin_total, bwin_mean, bwin_min, bwin_max, bwin_std = packet_win(bwd_flow)
    # dwin_total, dwin_mean, dwin_min, dwin_max, dwin_std = packet_win(two_way_flow)

    # 包的数目
    fwd_flow_length = ip_length[ip_length > 0]
    bwd_flow_length = ip_length[ip_length < 0]
    fpnum = len(fwd_flow_length)
    bpnum = len(bwd_flow_length)
    dpnum = fpnum + bpnum
    bfpnum_rate = round(bpnum / (fpnum + 0.001), 6)
    fpnum_s = round(fpnum / duration, 6)
    bpnum_s = round(bpnum / duration, 6)
    dpnum_s = round(dpnum / duration, 6)

    # 包的总长度 19
    fpl_total, fpl_mean, fpl_min, fpl_max, fpl_std = packet_len(fwd_flow_length)
    bpl_total, bpl_mean, bpl_min, bpl_max, bpl_std = packet_len(bwd_flow_length)
    dpl_total, dpl_mean, dpl_min, dpl_max, dpl_std = packet_len(ip_length)
    bfpl_rate = round(bpl_total / (fpl_total + 0.001), 6)
    fpl_s = round(fpl_total / duration, 6)
    bpl_s = round(bpl_total / duration, 6)
    dpl_s = round(dpl_total / duration, 6)

    # 包的标志特征 12
    # get_tcp_flags(value, packets)
    # fin_cnt, syn_cnt, rst_cnt, pst_cnt, ack_cnt, urg_cnt, cwe_cnt, ece_cnt = packet_flags(two_way_flow, 0)
    # fwd_pst_cnt, fwd_urg_cnt = packet_flags(fwd_flow, 1)
    # bwd_pst_cnt, bwd_urg_cnt = packet_flags(bwd_flow, 1)

    # 包头部长度 6
    # fp_hdr_len = packet_hdr_len(fwd_flow)
    # bp_hdr_len = packet_hdr_len(bwd_flow)
    # dp_hdr_len = packet_hdr_len(two_way_flow)
    # f_ht_len = round(fp_hdr_len / (fpl_total + 1), 6)
    # b_ht_len = round(bp_hdr_len / (bpl_total + 1), 6)
    # d_ht_len = round(dp_hdr_len / dpl_total, 6)
    #
    # 总共提取72个特征
    feature = [fiat_mean, fiat_min, fiat_max, fiat_std, biat_mean, biat_min, biat_max, biat_std,
               diat_mean, diat_min, diat_max, diat_std, duration,
               # fwin_total, fwin_mean, fwin_min,
               # fwin_max, fwin_std, bwin_total, bwin_mean, bwin_min, bwin_max, bwin_std, dwin_total,
               # dwin_mean, dwin_min, dwin_max, dwin_std,
               fpnum, bpnum, dpnum, bfpnum_rate, fpnum_s,
               bpnum_s, dpnum_s, fpl_total, fpl_mean, fpl_min, fpl_max, fpl_std, bpl_total, bpl_mean,
               bpl_min, bpl_max, bpl_std, dpl_total, dpl_mean, dpl_min, dpl_max, dpl_std, bfpl_rate,
               fpl_s, bpl_s, dpl_s,
               # fin_cnt, syn_cnt, rst_cnt, pst_cnt, ack_cnt, urg_cnt, cwe_cnt, ece_cnt,
               # fwd_pst_cnt, fwd_urg_cnt, bwd_pst_cnt, bwd_urg_cnt, fp_hdr_len, bp_hdr_len, dp_hdr_len,
               # f_ht_len, b_ht_len, d_ht_len
               ]
    # print(feature)
    return feature



# 均值,标准差,最大值,最小值计算
def calculation(list_info):
    mean_,min_,max_,std_=0,0,0,0
    if len(list_info) < 1:
        return [mean_,min_,max_,std_]
    else:
        min_=round(min(list_info),6)
        max_=round(max(list_info),6)
        mean_ = round(sum(list_info)/len(list_info),6)
        sd = sum([(i - mean_) ** 2 for i in list_info])
        std_ = round((sd / (len(list_info))) ** .5,6)
        return [mean_,min_,max_,std_]


# 包到达时间间隔特征
def packet_iat(flow):
    piat=[]
    if len(flow)>0:
        pre_time = flow[0]
        for pkt in flow[1:]:
            next_time = pkt
            piat.append(next_time-pre_time)
            pre_time=next_time
        piat_mean,piat_min,piat_max,piat_std=calculation(piat)
    else:
        piat_mean,piat_min,piat_max,piat_std=0,0,0,0
    return piat_mean,piat_min,piat_max,piat_std


# 拥塞窗口大小特征
def packet_win(flow):
    pwin = []
    for pkt in flow:
        pwin.append(pkt.window)
    pwin_total = round(sum(pwin), 6)
    pwin_mean,pwin_min,pwin_max,pwin_std=calculation(pwin)
    return pwin_total,pwin_mean,pwin_min,pwin_max,pwin_std


# 包长度特征
def packet_len(flow):
    pl = []
    for pkt in flow:
        pl.append(pkt)
    pl_total = round(sum(pl), 6)
    pl_mean, pl_min, pl_max, pl_std = calculation(pl)
    return pl_total, pl_mean, pl_min, pl_max, pl_std


def packet_flags(flow, key):
    # 初始化标志位计数器
    flag = [0, 0, 0, 0, 0, 0, 0, 0]  # [FIN, SYN, RST, PSH, ACK, URG, ECE, CWR]
    # 遍历流中的每个数据包
    for pkt in flow:
        if TCP in pkt:
            flags = int(pkt[TCP].flags)  # 获取 TCP 标志字段
            for i in range(8):
                flag[i] += flags % 2  # 统计每个标志位的值
                flags = flags // 2  # 右移一位

    # 根据 key 返回不同的结果
    if key == 0:
        # 返回所有标志位的统计结果
        return flag[0], flag[1], flag[2], flag[3], flag[4], flag[5], flag[6], flag[7]
    else:
        # 返回 PSH 和 URG 标志位的统计结果
        return flag[3], flag[5]



# 包头部长度
def packet_hdr_len(flow):
    p_hdr_len=0
    for pkt in flow:
        p_hdr_len = p_hdr_len+14+4*pkt[IP].ihl+20
    return p_hdr_len
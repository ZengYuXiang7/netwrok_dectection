import math
import numpy as np
import os
import csv

# 数据路径
def generatelist(filename):
    array_time = np.loadtxt(filename, dtype=float, delimiter=',', usecols=0, unpack=True)
    array_eth_src = np.loadtxt(filename, dtype=str, delimiter=',', usecols=1, unpack=True)
    array_eth_dst = np.loadtxt(filename, dtype=str, delimiter=',', usecols=2, unpack=True)
    array_len = np.loadtxt(filename, dtype=int, delimiter=',', usecols=3, unpack=True)
    array_labels = np.loadtxt(filename, dtype=int, delimiter=',', usecols=4, unpack=True)

    return array_time, array_len, array_eth_src, array_eth_dst, array_labels

class DynamicList(list):

    def __getslice__(self, i, j):
        return self.__getitem__(slice(i, j))
    def __setslice__(self, i, j, seq):
        return self.__setitem__(slice(i, j), seq)
    def __delslice__(self, i, j):
        return self.__delitem__(slice(i, j))

    def _resize(self, index):
        n = len(self)
        if isinstance(index, slice):
            m = max(abs(index.start), abs(index.stop))
        else:
            m = index + 1
        if m > n:
            self.extend([self.__class__() for i in range(m - n)])

    def __getitem__(self, index):
        self._resize(index)
        return list.__getitem__(self, index)

    def __setitem__(self, index, item):
        self._resize(index)
        if isinstance(item, list):
            item = self.__class__(item)
        list.__setitem__(self, index, item)



def TIG(session,session_num, session_time):
    V_temp = []
    E_temp = DynamicList()
    E_time = DynamicList()
    edge = 0
    for k in range(0, len(session)):
        V_temp.append(session[k])
        k+=1
    B = DynamicList()
    B_time = DynamicList()
    Brow = 0
    B[Brow] = [session_num[0]]
    B_time[Brow] = [session_time[0]]
    for t in range(1, len(session)):
        if session[t-1]*session[t]>0:
            B[Brow].append(session_num[t])
            B_time[Brow].append(session_time[t])
        else:
            Brow+=1
            B[Brow].append(session_num[t])
            B_time[Brow].append(session_time[t])
    Brow+=1
    for Erow in range(0,Brow):
        if len(B[Erow])>1:
            for Ecol in range(0, len(B[Erow])-1):
                E_temp[edge][0] = B[Erow][Ecol]
                E_temp[edge][1] = B[Erow][Ecol+1]
                E_time[edge] = abs(B_time[Erow][Ecol + 1] - B_time[Erow][Ecol])
                edge += 1

                #########################################################################
                E_temp[edge][0] = B[Erow][Ecol + 1]
                E_temp[edge][1] = B[Erow][Ecol]
                E_time[edge] = abs(B_time[Erow][Ecol + 1] - B_time[Erow][Ecol])
                edge += 1
                #########################################################################

    for Erow in range(0, Brow-1):
        if len(B[Erow]) == 1 and len(B[Erow+1]) == 1:
            E_temp[edge][0] = B[Erow][0]
            E_temp[edge][1] = B[Erow+1][0]
            E_time[edge] = abs(B_time[Erow + 1][0] - B_time[Erow][0])
            edge += 1

            ###########################################################
            E_temp[edge][0] = B[Erow+1][0]
            E_temp[edge][1] = B[Erow][0]
            E_time[edge] = abs(B_time[Erow + 1][0] - B_time[Erow][0])
            edge += 1
            ###########################################################

        else:
            E_temp[edge][0] = B[Erow][0]
            E_temp[edge][1] = B[Erow+1][0]
            E_time[edge] = abs(B_time[Erow + 1][0] - B_time[Erow][0])
            edge += 1

            #############################################################
            E_temp[edge][0] = B[Erow+1][0]
            E_temp[edge][1] = B[Erow][0]
            E_time[edge] = abs(B_time[Erow + 1][0] - B_time[Erow][0])
            edge += 1
            ############################################################

            E_temp[edge][0] = B[Erow][len(B[Erow])-1]
            E_temp[edge][1] = B[Erow+1][len(B[Erow+1])-1]
            E_time[edge] = abs(B_time[Erow + 1][len(B[Erow + 1]) - 1] + B_time[Erow][len(B[Erow]) - 1])
            edge+=1

            ############################################################
            E_temp[edge][0] = B[Erow+1][len(B[Erow+1]) - 1]
            E_temp[edge][1] = B[Erow][len(B[Erow]) - 1]
            E_time[edge] = abs(B_time[Erow + 1][len(B[Erow + 1]) - 1] + B_time[Erow][len(B[Erow]) - 1])
            edge += 1
            ############################################################

    return V_temp, E_temp, E_time


def datatoset(array_time, array_len, array_eth_src, array_eth_dst, array_labels, k, num):
    length = len(array_len)
    packets = []
    packets_time = []
    labels = []
    labels_node = []
    graph_indicator = []
    G = DynamicList()
    m = 0
    window_size = 30
    begin = 0
    end = begin + window_size
    eth_src = array_eth_src[0]
    while begin < length and end <= length:
        for i in range(begin, end):
            if array_eth_src[i] == eth_src:
                packets.append(array_len[i])
                packets_time.append(array_time[i])
            elif array_eth_dst[i] == eth_src:
                packets.append(-array_len[i])
                #packets.append(array_len[i])
                packets_time.append(array_time[i])
        begin = end
        end = begin + window_size
        if len(packets) == 1:
            packets.clear()
            packets_time.clear()
        if len(packets) > 1:
            labels.append(array_labels[0])
            file = open('APPLICATIONS_node_labels.txt', 'a+')
            for r in range(len(packets)):
                s = str(abs(packets[r])).replace('[', '').replace(']', '') + '\n'
                file.write(s)
            file.close()
            packets_num = []
            for temp in range(len(packets)):
                packets_num.append(num)
                num+=1
            for s in range(len(packets)):
                labels_node.append(array_labels[0])
                graph_indicator.append(k)
            k+=1
            (V_temp, E_temp, E_time) = TIG(packets, packets_num, packets_time)
            if len(E_temp) != 0:
                file = open('APPLICATIONS_A.txt', 'a+')
                for r in range(len(E_temp)):
                    s = str(E_temp[r]).replace('[', '').replace(']', '') + '\n'
                    file.write(s)
                file.close()

                file = open('APPLICATIONS_edge_attribute.txt', 'a+')
                for tmp in range(len(E_time)):
                    s = str(E_time[tmp]).replace('[', '').replace(']', '') + '\n'
                    file.write(s)
                file.close()

                ###
                #E_time_ = []
                #for temp in range(len(E_time)):
                    #if E_time[temp] == 0:
                        #E_time_.append(0)
                    #else:
                        #E_time_.append(1)
                #print(E_time_)
                #file = open('Applications_edge_attribute_.txt', 'a+')
                #s = (str(E_time_)).replace('[', '').replace(']', '') + ','
                #file.writelines(s)
                #E_time_.clear()
                ###
                G[m] = (V_temp, E_temp, E_time)
                m += 1

            packets_time.clear()
            packets.clear()
    return G, labels, labels_node, graph_indicator, k, num


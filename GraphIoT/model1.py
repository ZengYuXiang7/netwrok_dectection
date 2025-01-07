import math
import numpy as np
import os
import csv

# 这个函数的目的是从一个CSV文件中读取数据，并将数据存储到不同的数组中。
# 三重引号之间的内容表示注释，其中的每一行都代表将CSV文件中的特定列加载到相应的数组中。
def generatelist(filename):
    """array_time = np.loadtxt(filename, dtype=float, delimiter=',', usecols=0, unpack=True)
    array_len = np.loadtxt(filename, dtype=int, delimiter=',', usecols=7, unpack=True)
    array_tcplen = np.loadtxt(filename, dtype=int, delimiter=',', usecols=8, unpack=True)
    array_src = np.loadtxt(filename, dtype=str, delimiter=',', usecols=1, unpack=True)
    array_dst = np.loadtxt(filename, dtype=str, delimiter=',', usecols=2, unpack=True)
    array_proto = np.loadtxt(filename, dtype=int, delimiter=',', usecols=3, unpack=True)
    array_srcport = np.loadtxt(filename, dtype=int, delimiter=',', usecols=4, unpack=True)
    array_dstport = np.loadtxt(filename, dtype=int, delimiter=',', usecols=5, unpack=True)
    array_labels = np.loadtxt(filename, dtype=int, delimiter=',', usecols=12, unpack=True)
    array_sdport = np.loadtxt(filename, dtype=int, delimiter=',', usecols=13, unpack=True)"""
    # np.loadtxt：这是NumPy库中用于从文本文件加载数据的函数
    # filename：这是要从中加载数据的文件的名称。
    # dtype=float：指定数组中元素的数据类型为浮点数。
    # delimiter=','：指定文件中的数据以逗号分隔。
    # usecols=0：指定只加载第一列的数据。
    # unpack=True：将数组进行转置，使每列成为一个单独的数组。
    # 这对于将每列分配给单独的变量很有用。
    # 后续的行也遵循相似的模式，每一行从CSV文件中加载特定的列到一个具有特定数据类型的单独数组：
    array_time = np.loadtxt(filename, dtype=float, delimiter=',', usecols=0, unpack=True)
    array_len = np.loadtxt(filename, dtype=int, delimiter=',', usecols=7, unpack=True)
    array_tcplen = np.loadtxt(filename, dtype=int, delimiter=',', usecols=8, unpack=True)
    array_src = np.loadtxt(filename, dtype=str, delimiter=',', usecols=1, unpack=True)
    array_dst = np.loadtxt(filename, dtype=str, delimiter=',', usecols=2, unpack=True)
    array_proto = np.loadtxt(filename, dtype=int, delimiter=',', usecols=3, unpack=True)
    array_srcport = np.loadtxt(filename, dtype=int, delimiter=',', usecols=4, unpack=True)
    array_dstport = np.loadtxt(filename, dtype=int, delimiter=',', usecols=5, unpack=True)
    array_labels = np.loadtxt(filename, dtype=int, delimiter=',', usecols=9, unpack=True)
    array_sdport = np.loadtxt(filename, dtype=int, delimiter=',', usecols=10, unpack=True)

    # 最后，函数返回所有的数组：
    return array_time, array_len, array_tcplen, array_src, array_dst, array_proto, array_srcport, array_dstport, array_labels, array_sdport

#定义了一个名为 DynamicList 的类，它继承自内置的 list 类，并添加了一些自定义的切片和调整大小的功能。
# 这个 DynamicList 类扩展了内置的 list 类，添加了在 Python 2 中处理切片的方法，
# 并提供了调整大小的功能，确保在访问或设置元素之前列表足够大。
# 在 Python 3 中，由于切片已经由 __getitem__、__setitem__ 和 __delitem__ 直接处理，
# 这些方法主要在 Python 2 中兼容。
class DynamicList(list):# 定义了一个新的类 DynamicList，它继承自内置的 list 类。

    # 定义了 __getslice__ 方法，该方法在 Python 2 中用于切片。在 Python 3 中，
    # 已经不再使用 __getslice__，而是使用 __getitem__ 直接处理切片。这里通过调用 __getitem__ 来实现对切片的处理。
    def __getslice__(self, i, j):
        return self.__getitem__(slice(i, j))

    # 定义了 __setslice__ 方法，类似于上面的 __getslice__，
    # 用于在 Python 2 中设置切片。在 Python 3 中，通过调用 __setitem__ 来实现对切片的设置。
    def __setslice__(self, i, j, seq):
        return self.__setitem__(slice(i, j), seq)

    # 定义了 __delslice__ 方法，同样用于在 Python 2 中删除切片。
    # 在 Python 3 中，通过调用 __delitem__ 来实现对切片的删除。
    def __delslice__(self, i, j):
        return self.__delitem__(slice(i, j))

    # 定义了一个内部方法 _resize，该方法用于调整列表的大小，确保列表足够大以容纳给定的索引或切片。
    # 如果是切片，则取切片的起始和终止位置的绝对值的最大值作为目标大小，然后通过扩展列表来实现调整大小。
    def _resize(self, index):
        n = len(self)
        if isinstance(index, slice):
            m = max(abs(index.start), abs(index.stop))
        else:
            m = index + 1
        if m > n:
            self.extend([self.__class__() for i in range(m - n)])

# 重写了 __getitem__ 方法，该方法在通过索引或切片访问列表时调用。在访问之前，
    # 通过调用 _resize 方法来确保列表足够大。然后调用父类 list 的 __getitem__ 方法来执行实际的访问操作。

    def __getitem__(self, index):
        self._resize(index)
        return list.__getitem__(self, index)

    # 重写了 __setitem__ 方法，该方法在通过索引或切片设置列表元素时调用。
    # 同样，在设置之前，通过调用 _resize 方法来确保列表足够大。
    # 如果设置的元素是列表，将其转换为 DynamicList 类型，然后调用父类 list 的 __setitem__ 方法来执行实际的设置操作。
    def __setitem__(self, index, item):
        self._resize(index)
        if isinstance(item, list):
            item = self.__class__(item)
        list.__setitem__(self, index, item)

# 函数 TIG，该函数接受三个参数 session、session_num 和 session_time，然后生成一个有向图的顶点集合
# 该函数的目的是根据输入的序列和时间信息构建一个有向图，
# 其中顶点表示序列中的元素，边表示相邻元素之间的关系，而边对应的时间差表示相邻元素之间的时间差异。
def TIG(session,session_num, session_time):
    V_temp = [] # V_temp 是一个列表，用于存储图中的顶点。
    E_temp = DynamicList() # E_temp 是一个 DynamicList 类型的列表，用于存储图中的边。DynamicList 可能是自定义的动态列表类。
    E_time = DynamicList() # E_time 也是一个 DynamicList 类型的列表，用于存储每条边对应的时间差。
    edge = 0 # edge 是一个计数器，用于跟踪边的数量。

    # 将 session 中的元素添加到 V_temp 列表
    for k in range(0, len(session)):
        V_temp.append(session[k])
        k+=1
    B = DynamicList()  # 创建一个 DynamicList 类型的列表 B 用于存储相邻元素符号相同的组，B_time 存储相邻元素符号相同的组对应的时间。
    B_time = DynamicList() # 用于存储相邻元素符号相同的组对应的时间的列表
    Brow = 0 # 用于追踪 B 列表的行数
    B[Brow] = [session_num[0]] # 将第一个元素添加到 B 中的第一行
    B_time[Brow] = [session_time[0]] # 将第一个元素对应的时间添加到 B_time 的第一行

    # 使用循环遍历 session_num 和 session_time 列表，将相邻元素符号相同的元素分组并存储到 B 和 B_time 中。
    for t in range(1, len(session)):
        if session[t-1]*session[t] > 0:
            B[Brow].append(session_num[t])
            B_time[Brow].append(session_time[t])
        else:
            Brow += 1
            B[Brow].append(session_num[t])
            B_time[Brow].append(session_time[t])
    Brow += 1

    # 遍历相邻元素符号相同的组，构建正向和反向边的信息，并将其添加到 E_temp 和 E_time 列表中。这一部分涉及添加正向和反向边的逻辑。
    for Erow in range(0, Brow):
        if len(B[Erow]) > 1:
            for Ecol in range(0, len(B[Erow])-1):
                # 添加正向边信息
                E_temp[edge][0] = B[Erow][Ecol]
                E_temp[edge][1] = B[Erow][Ecol+1]
                E_time[edge] = abs(B_time[Erow][Ecol + 1] - B_time[Erow][Ecol])
                edge += 1

             #########################################################################
                # 添加反向边信息
                E_temp[edge][0] = B[Erow][Ecol + 1]
                E_temp[edge][1] = B[Erow][Ecol]
                E_time[edge] = abs(B_time[Erow][Ecol + 1] - B_time[Erow][Ecol])
                edge += 1
            #########################################################################

    # 遍历相邻元素符号不同的组，构建正向和反向边的信息，并将其添加到 E_temp 和 E_time 列表中。这一部分同样涉及添加正向和反向边的逻辑
    for Erow in range(0, Brow-1):
        if len(B[Erow]) == 1 and len(B[Erow+1]) == 1:
            # 添加正向边信息
            E_temp[edge][0] = B[Erow][0]
            E_temp[edge][1] = B[Erow+1][0]
            E_time[edge] = abs(B_time[Erow + 1][0] - B_time[Erow][0])
            edge += 1

        ###########################################################
            # 添加反向边信息
            E_temp[edge][0] = B[Erow+1][0]
            E_temp[edge][1] = B[Erow][0]
            E_time[edge] = abs(B_time[Erow + 1][0] - B_time[Erow][0])
            edge += 1
        ###########################################################

        else:
            # 添加正向边信息
            E_temp[edge][0] = B[Erow][0]
            E_temp[edge][1] = B[Erow+1][0]
            E_time[edge] = abs(B_time[Erow + 1][0] - B_time[Erow][0])
            edge += 1

        #############################################################
            # 添加反向边信息
            E_temp[edge][0] = B[Erow+1][0]
            E_temp[edge][1] = B[Erow][0]
            E_time[edge] = abs(B_time[Erow + 1][0] - B_time[Erow][0])
            edge += 1
        ############################################################
            # 添加连接末尾元素的边信息
            E_temp[edge][0] = B[Erow][len(B[Erow])-1]
            E_temp[edge][1] = B[Erow+1][len(B[Erow+1])-1]
            E_time[edge] = abs(B_time[Erow + 1][len(B[Erow + 1]) - 1] + B_time[Erow][len(B[Erow]) - 1])
            edge += 1

        ############################################################
            # 添加连接末尾元素的反向边信息
            E_temp[edge][0] = B[Erow+1][len(B[Erow+1]) - 1]
            E_temp[edge][1] = B[Erow][len(B[Erow]) - 1]
            E_time[edge] = abs(B_time[Erow + 1][len(B[Erow + 1]) - 1] + B_time[Erow][len(B[Erow]) - 1])
            edge += 1
        ############################################################
    #最后，函数返回顶点集合 V_temp、边集合 E_temp 和边对应的时间差集合 E_time。
    return V_temp, E_temp, E_time

# 这是一个函数定义，接受多个数组（array_time、array_len、array_labels等）
# 和两个变量（k和num）作为输入参数
# 作用是对输入的网络数据进行处理，将数据转换为一种适用于动态图的格式，并生成一个动态图的表示
def datatoset(array_time, array_len, array_labels, array_src, array_dst, array_proto, array_srcport, array_dstport, array_sdport, k, num):
    length = len(array_len)# length 是 array_len 的长度
    # packets、packets_time、labels、labels_node、graph_indicator 被初始化为空列表。
    packets = []
    packets_time = []
    labels = []
    labels_node = []
    graph_indicator = []
    G = DynamicList()# G 被初始化为 DynamicList() 的实例
    m = 0# m 被初始化为 0。
    flag = [0 for i in range(length)]# flag 被初始化为一个长度等于 length 的零列表。
    begin = 0# begin 被初始化为 0
    # 代码进入一个 while 循环，一直持续到 begin 不再小于 length-1。
    while begin < length-1:
        #print("begin:", begin)

        tmp = begin + 1# tmp 被设置为 begin + 1
        if tmp > length:# 如果 tmp 大于 length，则退出循环。
            break
        # 一个嵌套的 while 循环运行，只要 array_sdport[tmp]
        # 等于 array_sdport[begin]。它递增 tmp 直到遇到不同的值或达到数组的末尾
        while array_sdport[tmp] == array_sdport[begin]:
            if tmp < length-1:
                tmp = tmp + 1
            else:
                break
        end = tmp# end 被设置为 tmp 的值
        #print("end:", end)
        # 一个循环从 begin 到 end-1 运行。它检查如果 flag[i] 是 0，
        # 就根据一些条件将元素添加到 packets 和 packets_time 中。它还将 flag[i] 设置为 1。
        for i in range(begin, end):
            if flag[i] == 0:
                packets.append(array_len[i])
                packets_time.append(array_time[i])
                flag[i] = 1
                # 一个嵌套的循环从 i+1 运行到 end。如果 flag[j] 是 0，
                # 它检查条件并将元素添加到 packets 和 packets_time 中。它将 flag[j] 设置为 1。
                for j in range(i+1, end+1):
                    if flag[j] == 0:
                        if array_src[i] == array_src[j] and array_dst[i] == array_dst[j] and array_proto[i] == array_proto[j] and array_srcport[i] == array_srcport[j] and array_dstport[i] == array_dstport[j]:
                            packets.append(array_len[j])
                            packets_time.append(array_time[j])
                            flag[j] = 1
                        elif array_src[i] == array_dst[j] and array_dst[i] == array_src[j] and array_proto[i] == array_proto[j] and array_srcport[i] == array_dstport[j] and array_dstport[i] == array_srcport[j]:
                            packets.append(-array_len[j])
                            packets_time.append(array_time[j])
                            flag[j] = 1
                # 如果 packets 的长度为 1，则清空 packets 和 packets_time。
                if len(packets) == 1:
                    packets.clear()
                    packets_time.clear()
                num_max = 30# num_max 被设置为 30
                # 如果 packets 的长度大于 1，它被截断为 num_max 个元素。
                if len(packets) > 1:
                    if len(packets) > num_max:
                        packets = packets[:num_max]
                        packets_time = packets_time[:num_max]
                    # labels 被附加上 array_labels 的第一个元素。
                    labels.append(array_labels[0])

                    # 将 packets 中元素的绝对值写入名为 'Applications_node_labels.txt' 的文件中
                    file = open('Applications_node_labels.txt', 'a+')
                    #file = open('Applications_node_attributes.txt', 'a+')
                    for r in range(len(packets)):
                        s = str(abs(packets[r])).replace('[', '').replace(']', '') + '\n'
                        file.write(s)
                    file.close()
                    # packets_num 中的值为每个 packets 中的元素递增的 num。
                    packets_num = []

                    for temp in range(len(packets)):
                        packets_num.append(num)
                        num+=1
                        #temp+=1
                        # 对于 packets 中的每个元素，labels_node 被附加上 array_labels 的第一个元素，
                        # 而 graph_indicator 被附加上当前的 k。
                    for s in range(len(packets)):
                        labels_node.append(array_labels[0])
                        graph_indicator.append(k)
                        #s+=1
                    k+=1# k 被递增

                    # 调用函数 TIG，并使用 packets、packets_num 和 packets_time 作为参数。
                    # 将结果的值赋给 (V_temp, E_temp, E_time)。
                    (V_temp, E_temp, E_time) = TIG(packets, packets_num, packets_time)

                    # 如果 E_temp 的长度不为 0，它将 E_temp 中的元素写入 'Applications_A.txt'，
                    # 将 E_time 中的元素写入 'Applications_edge_attribute.txt'。
                    if len(E_temp) != 0:
                        file = open('Applications_A.txt', 'a+')
                        for r in range(len(E_temp)):
                            s = str(E_temp[r]).replace('[', '').replace(']', '') + '\n'
                            file.write(s)
                        file.close()

                        file = open('Applications_edge_attribute.txt', 'a+')
                        for tmp in range(len(E_time)):
                            s = str(E_time[tmp]).replace('[', '').replace(']', '') + '\n'
                            file.write(s)
                        file.close()
                        G[m] = (V_temp, E_temp)
                        m+=1
                    packets_time.clear()
                    packets.clear()
        begin = end
    return G, labels, labels_node, graph_indicator, k, num

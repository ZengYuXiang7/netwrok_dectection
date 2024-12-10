import csv
from collections import Counter
import jenkspy
import matplotlib.pyplot as plt
import numpy as np

def read_packet_data(csv_file):
    packet_sizes = []

    # 读取 CSV 文件
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            packet_sizes.append(int(row['length']))
    
    return packet_sizes

def cluster_and_plot(csv_file, n_classes):
    # 读取数据包大小
    packet_sizes = read_packet_data(csv_file)
    
    # 统计数据包大小的数量
    size_counts = Counter(packet_sizes)
    sizes = list(size_counts.keys())
    counts = list(size_counts.values())
    
    # 使用 jenkspy 聚类
    breaks = jenkspy.jenks_breaks(sizes, n_classes=n_classes)

    # 可视化数据
    plt.figure(figsize=(10, 6))
    
    # 遍历每个区间并绘制折线图
    for i in range(len(breaks) - 1):
        start, end = breaks[i], breaks[i + 1]
        indices = [j for j, size in enumerate(sizes) if start <= size < end]
        cluster_sizes = [sizes[j] for j in indices]
        cluster_counts = [counts[j] for j in indices]
        
        # 按 x 轴排序，确保折线连贯
        sorted_indices = np.argsort(cluster_sizes)
        cluster_sizes = np.array(cluster_sizes)[sorted_indices]
        cluster_counts = np.array(cluster_counts)[sorted_indices]
        
        # 绘制折线图
        plt.plot(cluster_sizes, cluster_counts, marker='o', label=f'Range: [{start}, {end})')
    
    # 图形美化
    plt.title('Packet Size Clustering Using Jenks Natural Breaks')
    plt.xlabel('Packet Size')
    plt.ylabel('Frequency')
    plt.legend()
    plt.grid(True)
    plt.show()

# 示例用法
csv_file = './datasets/MedBIoT/csv/1000s/mirai_mal_spread_all_1000s.csv'  # 替换为您的 CSV 文件路径
cluster_and_plot(csv_file, n_classes=8)  # n_classes 是聚类数量

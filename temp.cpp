//
// Created by 曾渝翔 on 25-1-7.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <thread>
#include <pcap.h>
#include <arpa/inet.h>
#include <netinet/ip.h>
#include <netinet/tcp.h>
#include <netinet/udp.h>
#include <dirent.h>
#include <sys/stat.h>

#define MAX_THREADS 8

// 定义存储抓包数据的结构体
struct PacketInfo {
    std::string timestamp;
    std::string source_ip;
    std::string destination_ip;
    uint16_t source_port;
    uint16_t destination_port;
    std::string protocol;
    uint32_t length;
};

// 处理每个数据包的函数
PacketInfo process_packet(const struct pcap_pkthdr *header, const uint8_t *data) {
    PacketInfo packet_info;

    // 获取时间戳
    packet_info.timestamp = std::to_string(header->ts.tv_sec) + "." + std::to_string(header->ts.tv_usec);

    // 解析 IP 和端口（假设是 IPv4）
    struct ip *ip_header = (struct ip *)(data + 14);  // 跳过以太网头
    packet_info.source_ip = inet_ntoa(ip_header->ip_src);
    packet_info.destination_ip = inet_ntoa(ip_header->ip_dst);

    // 判断协议类型
    if (ip_header->ip_p == IPPROTO_TCP) {
        packet_info.protocol = "TCP";
        struct tcphdr *tcp_header = (struct tcphdr *)(data + 14 + ip_header->ip_hl * 4);
        packet_info.source_port = ntohs(tcp_header->th_sport);
        packet_info.destination_port = ntohs(tcp_header->th_dport);
    } else if (ip_header->ip_p == IPPROTO_UDP) {
        packet_info.protocol = "UDP";
        struct udphdr *udp_header = (struct udphdr *)(data + 14 + ip_header->ip_hl * 4);
        packet_info.source_port = ntohs(udp_header->uh_sport);
        packet_info.destination_port = ntohs(udp_header->uh_dport);
    } else {
        packet_info.protocol = "Unknown";
        packet_info.source_port = 0;
        packet_info.destination_port = 0;
    }

    // 获取包长度
    packet_info.length = header->len;

    return packet_info;
}

// 保存数据到 CSV 文件
void save_to_csv(const std::vector<PacketInfo> &packets, const std::string &csv_file) {
    std::ofstream file;
    file.open(csv_file, std::ios::app); // 追加写入

    // 如果文件是空的，写入表头
    if (file.tellp() == 0) {
        file << "Timestamp,Source IP,Destination IP,Source Port,Destination Port,Protocol,Length\n";
    }

    // 写入数据
    for (const auto &packet : packets) {
        file << packet.timestamp << ","
             << packet.source_ip << ","
             << packet.destination_ip << ","
             << packet.source_port << ","
             << packet.destination_port << ","
             << packet.protocol << ","
             << packet.length << "\n";
    }
}

// 处理抓包文件的函数
void process_pcap(const std::string &pcap_file, const std::string &csv_file) {
    pcap_t *handle;
    char errbuf[PCAP_ERRBUF_SIZE];

    // 打开 pcap 文件
    handle = pcap_open_offline(pcap_file.c_str(), errbuf);
    if (handle == nullptr) {
        std::cerr << "Error opening file " << pcap_file << ": " << errbuf << std::endl;
        return;
    }

    std::vector<PacketInfo> packet_info_list;
    const struct pcap_pkthdr *header;
    const uint8_t *data;

    // 遍历数据包
    while (pcap_next_ex(handle, &header, &data) >= 0) {
        // 处理每个数据包
        PacketInfo packet_info = process_packet(header, data);
        packet_info_list.push_back(packet_info);
    }

    // 保存数据到 CSV
    save_to_csv(packet_info_list, csv_file);

    // 关闭文件句柄
    pcap_close(handle);
}

// 遍历目录中的所有 pcap 文件并处理
void process_pcap_files_in_directory(const std::string &directory, const std::string &csv_dir) {
    DIR *dir;
    struct dirent *entry;

    dir = opendir(directory.c_str());
    if (dir == nullptr) {
        std::cerr << "Error opening directory: " << directory << std::endl;
        return;
    }

    while ((entry = readdir(dir)) != nullptr) {
        if (entry->d_type == DT_REG && std::string(entry->d_name).find(".pcap") != std::string::npos) {
            std::string pcap_file = directory + "/" + entry->d_name;
            std::string base_name = entry->d_name;
            base_name = base_name.substr(0, base_name.find_last_of('.')); // 去除扩展名

            std::string csv_file = csv_dir + "/" + base_name + ".csv";
            std::cout << "Processing pcap file: " << pcap_file << std::endl;
            process_pcap(pcap_file, csv_file);
            std::cout << "Converted pcap file to csv: " << csv_file << std::endl;
        }
    }

    closedir(dir);
}

int main() {
    std::string input_dir = "../datasets/pcap/sogou"; // 输入目录
    std::string output_dir = "../datasets/csv/sogou"; // 输出目录

    // 创建输出目录
    struct stat st;
    if (stat(output_dir.c_str(), &st) == -1) {
        mkdir(output_dir.c_str(), 0700);
    }

    // 处理文件夹中的所有 pcap 文件
    process_pcap_files_in_directory(input_dir, output_dir);

    return 0;
}
from data_preprocess.pcap_to_csv import *

if __name__ == '__main__':
    os.makedirs('./datasets/csv/', exist_ok=True)
    # process_pcap_files_in_directory('Medboit')
    process_pcap_files_in_directory('IoT')
    # process_pcap_files_in_directory('Device')

import wfdb
import csv
import os

path_store_csv = './convert_file/'  # 文件存储的路径


def convert_wave():
    if not os.path.exists(path_store_csv):
        os.mkdir(path_store_csv)
    file_list = [i.split('.')[0] for i in os.listdir('./source_file/')]  # 数据文件路径
    remain = (list(set(file_list)))  # 去重
    for i in remain:
        signals, fields = wfdb.rdsamp('source_file/' + str(i), channels=[0, 0, 0, 0], sampfrom=100, sampto=15000)
        file_path = path_store_csv + str(i) + '.csv'
        with open(file_path, 'w', newline='') as f:
            csv_write = csv.writer(f)
            csv_write.writerows(signals)


convert_wave()

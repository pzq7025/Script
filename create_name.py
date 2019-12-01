# -*- coding:utf-8 -*-
# !bin/even/python-3.6.5
# author: pzq
# email: **********@qq.com
"""
随机生成密码和姓名
"""
import csv
import random

base_path = '../download_file/'


def generate_data():
    # 姓氏
    last_name = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许', '何', '吕', '施', '张', '孔', '曹', '严', '华']
    # 名字
    first_name = ['华', '玉', '秀', '文', '明', '兰', '金', '国', '春', '红', '丽', '小', '梅', '云', '芳', '平', '海', '珍', '荣']
    all_data = []
    for i in range(60):
        browser_id = ''.join([str(random.randrange(0, 9)) for _ in range(6)])
        browser_name = ''.join([last_name[random.randrange(28)]] + [first_name[random.randrange(19)]] + [first_name[random.randrange(19)] if random.randrange(10) % 2 == 1 else ""])
        browser_password = ''.join([chr(random.randrange(97, 123)) for _ in range(3)] + [str(random.randrange(0, 9)) for _ in range(3)])
        browser_status = 1
        browser_number = 0
        browser_number_max = 18
        overdraft = 0.00
        browser_type = random.randint(1, 3)
        one = [browser_id, browser_name, browser_password, browser_status, browser_number, browser_number_max, overdraft, browser_type]
        all_data.append(one)
    write_to_file(all_data)


def write_to_file(contents):
    file_path = base_path + 'student.csv'
    with open(file_path, 'w', encoding='utf-8-sig', newline='') as f_csv:
        buffer_csv = csv.writer(f_csv)
        header = ['browser_id', 'browser_name', 'browser_password', 'browser_status', 'browser_number', 'browser_number_max', 'overdraft', 'browser_type']
        buffer_csv.writerow(header)
        buffer_csv.writerows(contents)


if __name__ == '__main__':
    generate_data()

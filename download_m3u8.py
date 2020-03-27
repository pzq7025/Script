import requests
import os
import re
from Crypto.Cipher import AES

url = "https://1252524126.vod2.myqcloud.com/9764a7a5vodtransgzp1252524126/0176cbbd5285890799673243539/drm/v.f230.m3u8?"
data = {
    "time": ""
}

download_url = "https://1252524126.vod2.myqcloud.com/9764a7a5vodtransgzp1252524126/0176cbbd5285890799673243539/drm/"

"""
列举一个单位格大小：
#EXTINF:2.000000,
v.f230.ts?start=0&end=158495&type=mpegts
#EXT-X-KEY:METHOD=AES-128,URI="https://app.xiaoe-tech.com/get_video_key.php?edk=CiCTzP%2B6jBR9H5awSTdnrwcCQzZlldD%2BTYaAr%2FlaHOwsPBCO08TAChiaoOvUBCokYjRhNjFiNTgtMmVhNy00OWYxLTgwZGMtZTE0NTIyODc5YWIy&fileId=5285890799673243539&keySource=VodBuildInKMS",IV=0x00000000000000000000000000000000
"""


def download():
    url_key = "https://app.xiaoe-tech.com/get_video_key.php?edk=CiCTzP%2B6jBR9H5awSTdnrwcCQzZlldD%2BTYaAr%2FlaHOwsPBCO08TAChiaoOvUBCokYjRhNjFiNTgtMmVhNy00OWYxLTgwZGMtZTE0NTIyODc5YWIy&fileId=5285890799673243539&keySource=VodBuildInKMS"
    content_key = requests.get(url_key).content  # 获取key值
    download_path = os.getcwd() + r"\download"
    if not os.path.exists(download_path):
        os.mkdir(download_path)
    m3u8_content = requests.get(url, params=data).text
    print(m3u8_content)
    exit()
    result = re.compile(r"v\.f230\.ts\?start=[0-9]+&end=[0-9]+&type=mpegts", re.S).findall(m3u8_content)  # 匹配.ts的文件地址
    vi = "0x00000000000000000000000000000000"
    vt = vi.replace("0x", "")[:16].encode()  # 偏移码
    ci = AES.new(content_key, AES.MODE_CBC, vt)  # 构建解码器
    for i in enumerate(result):
        print(f"正在下载：{i[0]}")
        content_ts = requests.get(download_url + str(i[1])).content
        with open(download_path + "\\" + str(i[0] + 1) + ".mp4", 'ab') as f:
            f.write(ci.decrypt(content_ts))  # 将内容解码
            f.flush()


if __name__ == '__main__':
    download()

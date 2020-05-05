from urllib.parse import unquote

def transform(str_param):
    # 将包转换成为字典的形式
    param = {i[0]: unquote(i[1]).encode('utf-8').decode('utf-8') for i in [i.split('=') for i in str_param.split('&')]}
    return param


def register_student(requests):
    get_data = requests.body.decode('utf-8')
    param = transform(get_data)

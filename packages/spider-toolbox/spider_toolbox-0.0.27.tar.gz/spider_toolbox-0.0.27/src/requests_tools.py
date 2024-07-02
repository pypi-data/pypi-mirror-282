import time
import os
import requests
# from rich import print

default_ua = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 '
                  'Safari/537.36'}


# 请求超时重试
def get(url: str,
        headers=None,
        params=None,
        cookies=None,
        timeout: int = None,
        retry_num: int = 10,
        retry_sleep: int = 1,
        info=False,
        proxies=False):
    """
    :param url: 地址
    :param headers: 请求头
    :param params: params
    :param retry_num: 重试次数
    :param retry_sleep: 重试休眠时间
    :param timeout: 超时时间
    :param info: 是否输出信息
    :param proxies:
    """
    if headers is None:
        headers = default_ua
    for i in range(1, retry_num + 1):
        try:
            resp = requests.get(url, headers=headers, cookies=cookies, params=params, timeout=timeout, proxies=proxies)
            return resp
        except Exception:
            if info:
                print(f'{url} 失败 {i} 次')
            time.sleep(retry_sleep + i / 3)
    print(f'{url}访问失败')
    raise '链接访问失败'


def post(url: str,
         headers=None,
         params=None,
         cookies=None,
         data=None,
         timeout: int = None,
         retry_num: int = 10,
         retry_sleep: int = 1,
         info=False):
    """
    :param url: 地址
    :param headers: 请求头
    :param params: params
    :param retry_num: 重试次数
    :param retry_sleep: 重试休眠时间
    :param timeout: 超时时间
    :param info: 是否输出信息
    """
    if headers is None:
        headers = default_ua
    for i in range(1, retry_num + 1):
        try:
            resp = requests.post(url, headers=headers, cookies=cookies, params=params, timeout=timeout, data=data)
            return resp
        except Exception:
            if info:
                print(f'{url} 失败 {i} 次')
            time.sleep(retry_sleep + i / 3)
    print(f'{url}访问失败')
    raise '链接访问失败'


def session():
    return requests.Session()


def byte_downloader(url: str,
                    workdir: str,
                    file_name: str,
                    file_type: str,
                    headers=None,
                    timeout: int = None,
                    retry_num: int = 10,
                    retry_sleep: int = 1) -> bool:
    """
    :param url:
    :param workdir:
    :param file_name: 文件名
    :param file_type: 文件后缀 无需.
    :param headers:
    :param timeout: 超时时间
    :param retry_num: 重试次数
    :param retry_sleep: 重试间隔
    :return: bool
    """
    file_type = file_type.replace('.', '')
    workdir = os.path.join(workdir, file_name) + '.' + file_type
    resp = get(url,
               headers=headers,
               timeout=timeout,
               retry_num=retry_num,
               retry_sleep=retry_sleep)
    if resp:
        with open(workdir, 'wb') as f:
            f.write(resp.content)
        return True
    else:
        return False


if __name__ == '__main__':
    print(get('https://www.google.com.hk/').text)

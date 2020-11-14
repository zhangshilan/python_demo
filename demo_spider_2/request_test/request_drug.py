# -*- codeing = utf-8 -*-
#@Time :2020/11/14 17:55
#@Author :张士澜
#@File :request_drug.py
#@Software :PyCharm

import requests
import json
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 86.0.4240.198Safari / 537.36'
    }
    id_list = []
    all_data_list = []
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'

    for page in range(1,6):
        page = str(page)
        data = {
            'on': 'true',
            'page': page,
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname': '',
            'applysn': ''
        }

        response = requests.post(url = url,headers = headers,data = data)
        json_ids = response.json()
        for dic in json_ids['list']:
            id_list.append(dic['ID'])

    for id in id_list:
        data = {
            'id':id
        }
        detail_json = requests.post(url = post_url,data = data,headers = headers).json()
        #print(detail_json,'---------ending----------')
        all_data_list.append(detail_json)

    fp = open('./allData.json','w',encoding='utf-8')
    json.dump(all_data_list,fp = fp,ensure_ascii=False)
    print('over')
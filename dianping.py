import requests
import json
import re
from tqdm import tqdm

orgin_url = 'http://s.dianping.com/event/'

cookies = {
    '_lxsdk_cuid': '167b542ff3f5b-0c703e059f7432-35647600-13c680-167b542ff40c8',
    '_lxsdk': '167b542ff3f5b-0c703e059f7432-35647600-13c680-167b542ff40c8',
    '_hc.v': '0ed79a07-8dbb-4a7c-739b-ba1bcd181616.1544934326',
    'ctu': 'ebcf67266e9b22aca41709463bf938278bb0a47763266e266f070a3c93fd5055',
    'cye': 'lianyuangang',
    'dper': 'ff9885c6bc2b7943abc9f43feb4fae7f38b83e337ef25f137d9988a693db7e5f45fd5fe7ff1374b5254a04bc380921a12235c4785edb18fa19ffe323010a11fa2bd2e779263c605f9777148beffa0d78f72fa6b62edf4648b2c998f3a4a1f7b2',
    'll': '7fd06e815b796be3df069dec7836c3df',
    'ua': 'HelloWorld_9933',
    'uamo': '13141350678',
    'cy': '2',
    'locallat': '39.8836559',
    'locallng': '116.4735119',
    'geoType': 'wgs84',
    'pvhistory': '6L+U5ZuePjo8L2dldGxvY2FsY2l0eWlkP2xhdD0zOS44ODM2NTU5JmxuZz0xMTYuNDczNTExOSZjb29yZFR5cGU9MSZjYWxsYmFjaz1XaGVyZUFtSTExNTUwNzM1NDIxNjgyPjo8MTU1MDczNTQyMjI4MV1fWw==',
    'm_flash2': '1',
    '_lx_utm': 'utm_source%3Ddp_pc_group',
    '_lxsdk_s': '1690efe229c-e39-9ee-86f%7C%7C41',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Referer': 'http://s.dianping.com/event/beijing',
    'Origin': 'http://s.dianping.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
    'Content-Type': 'application/json',
}


ids = []
activityTitles = []
data = {"cityId":"2","type":0,"mode":"","page":1}
for page in range(1,10):
    data["page"] = str(page)
    response = requests.post('http://m.dianping.com/activity/static/pc/ajaxList', headers=headers, cookies=cookies, data=str(json.dumps(data)))
    # print(page)
    for item in response.json()['data']['detail']:
        activityTitles.append(item['activityTitle'])
        ids.append(item['offlineActivityId'])

print('搜索到'+str(len(ids))+'条霸王餐')

cookies = {
    '_lxsdk_cuid': '167b542ff3f5b-0c703e059f7432-35647600-13c680-167b542ff40c8',
    '_lxsdk': '167b542ff3f5b-0c703e059f7432-35647600-13c680-167b542ff40c8',
    '_hc.v': '0ed79a07-8dbb-4a7c-739b-ba1bcd181616.1544934326',
    'ctu': 'ebcf67266e9b22aca41709463bf938278bb0a47763266e266f070a3c93fd5055',
    'cye': 'lianyuangang',
    'dper': 'ff9885c6bc2b7943abc9f43feb4fae7f38b83e337ef25f137d9988a693db7e5f45fd5fe7ff1374b5254a04bc380921a12235c4785edb18fa19ffe323010a11fa2bd2e779263c605f9777148beffa0d78f72fa6b62edf4648b2c998f3a4a1f7b2',
    'll': '7fd06e815b796be3df069dec7836c3df',
    'ua': 'HelloWorld_9933',
    'uamo': '13141350678',
    'cy': '2',
    'locallat': '39.8836559',
    'locallng': '116.4735119',
    'geoType': 'wgs84',
    'pvhistory': '6L+U5ZuePjo8L2dldGxvY2FsY2l0eWlkP2xhdD0zOS44ODM2NTU5JmxuZz0xMTYuNDczNTExOSZjb29yZFR5cGU9MSZjYWxsYmFjaz1XaGVyZUFtSTExNTUwNzM1NDIxNjgyPjo8MTU1MDczNTQyMjI4MV1fWw==',
    'm_flash2': '1',
    '_lx_utm': 'utm_source%3Ddp_pc_group',
    '_lxsdk_s': '1690efe229c-e39-9ee-86f%7C%7C41',
}

headers = {
    'Origin': 'http://s.dianping.com',
    'Accept-Encoding': 'gzip, deflate',
    'X-Request': 'JSON',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8;',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Accept': 'application/json, text/javascript',
    'Referer': 'http://s.dianping.com/event/885343990',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
}

data = {
  'offlineActivityId': '885343990',
  'phoneNo': '151****3863',
  'shippingAddress': '',
  'extraCount': '',
  'birthdayStr': '',
  'email': '',
  'marryDayStr': '',
  'babyBirths': '',
  'pregnant': '',
  'marryStatus': '0',
  'comboId': '',
  'branchId': '568675',
  'usePassCard': '0',
  'passCardNo': '',
  'isShareSina': 'false',
  'isShareQQ': 'false'
}
success = []
for _id in tqdm(ids):
    text = requests.get(orgin_url+str(_id),headers=headers,cookies=cookies).text
    shopid = re.search(r'shopid:[0-9]*',text).group() # 一个就够
    shopid = shopid.split('shopid:')[1]
    data['offlineActivityId'] = str(_id)
    data['branchId'] = shopid
    response = requests.post('http://s.dianping.com/ajax/json/activity/offline/saveApplyInfo', headers=headers,cookies=cookies, data=data)

    msg = json.loads(response.text)
    if response.text[0] != '{':
        print(activityTitles[ids.index(_id)]+' 登记成功')
        success.append(activityTitles[ids.index(_id)])
        continue
    if "不要重复报名" in msg["msg"]["html"]:
        success.append(activityTitles[ids.index(_id)])
    # print(activityTitles[ids.index(_id)]+' 登记失败')

print('成功登记活动：')
for i in success:
    print(i)


import requests
import json
import re
from tqdm import tqdm

orgin_url = 'http://s.dianping.com/event/'
cookies = {
    '_lxsdk_cuid': '167b542ff3f5b-0c703e059f7432-35647600-13c680-167b542ff40c8',
    '_lxsdk': '167b542ff3f5b-0c703e059f7432-35647600-13c680-167b542ff40c8',
    '_hc.v': '0ed79a07-8dbb-4a7c-739b-ba1bcd181616.1544934326',
    '_lx_utm': 'utm_source%3Ddp_pc_event',
    'dper': 'db1066a015bd0911adb3bcc9e15880006f29ed373cf67879b12739d4036fb21f79806506b0596ef4365631877054084c6193dfcb26bb260ae8f8cee7275e58b71e88f988afeddfd346e39936d062a10bf381be636dc89ec87f0b26148c93e4bb',
    'll': '7fd06e815b796be3df069dec7836c3df',
    'ua': 'HelloWorld_9933',
    'ctu': 'ebcf67266e9b22aca41709463bf938278bb0a47763266e266f070a3c93fd5055',
    'uamo': '13141350678',
    '_lxsdk_s': '168bd2155b1-257-548-e50%7C%7C53',
    'cy': '1',
}

headers = {
    'Origin': 'http://s.dianping.com',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Content-Type': 'application/json',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Referer': 'http://s.dianping.com/event/beijing',
    'Connection': 'keep-alive',
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
    'cy': '2',
    'lgtoken': '0a01ef863-882f-4c80-b9f7-8a8d18e322d0',
    'dper': '03b951cadf1779954e6b2ba7295851187a2410417d6f78ef7549353252f7c9a1fd4b865efa92301458b8d006fa2949db8f32a5187b846f8816e73bae68d4442d60c372020f587ced0f147d27bf83a4386806795c13d5bc79188dc11e3dd834c1',
    'll': '7fd06e815b796be3df069dec7836c3df',
    'ua': 'dpuser_6248862560',
    'uamo': '15197323863',
    '_lx_utm': 'utm_source%3Ddp_pc_group',
    '_lxsdk_s': '168bd7b1ea6-673-2dc-d10%7C%7C57',
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


__author__ = 'creator'

import requests as rq
import csv
import json

def getAddressFromNaver(name) :
	url = "http://map.naver.com/search2/local.nhn"
	header = header = {'User-Agent': 'Mozilla/5.0'}
	payload = {'query': name}

	req = rq.Request('Get', url, headers=header, params=payload)
	r = req.prepare()
	s = rq.Session()
	result = s.send(r)
	return result.json()

target_li = ['지하철','편의점', '카페', '마트', '은행', '파출소', '우체국', '보건소', '의원']

reader = csv.reader(open('dong_list.csv','r'))
writer = csv.writer(open('bus_dong_final2.csv','w'))

for row in reader:
    gu = row[0]
    dong = row[1]
    t_li = []

    for j in range(len(target_li)) :
        target = target_li[j]
        data = getAddressFromNaver("서울특별시"+gu+dong+target)
        t_value = data['result']['totalCount']
        t_li.append(t_value)


    print (gu,dong, t_li)
    writer.writerow([gu, dong, t_li[0], t_li[1], t_li[2], t_li[3], t_li[4], t_li[5], t_li[6], t_li[7], t_li[8]])
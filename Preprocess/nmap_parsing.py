__author__ = 'creator'

import requests as rq
import csv


def getAddressFromNaver(name) :
	url = "http://map.naver.com/search2/local.nhn" #네이버 지도 검색값
	header = header = {'User-Agent': 'Mozilla/5.0'} # 헤더값 할당
	payload = {'query': name} #검색값

	req = rq.Request('Get', url, headers=header, params=payload) #헤더값과 파라미터값을 get방식으로 요청

	r = req.prepare()
	s = rq.Session()
	result = s.send(r)
	return result.json() #결과값 json형태로 반환

target_li = ['지하철','편의점', '카페', '마트', '은행', '파출소', '우체국', '보건소', '의원'] # 검색 데이터로 쓸 값들

reader = csv.reader(open('InputData/dong_list.csv','r'))          #서울시에 행정동값 데이터가 있는 파일 읽기 스트림 생성
#writer = csv.writer(open('OutputData/nmap_search_result.csv','w'))    #검색결과값이 쓰여질 파일 스트림 생성

print (target_li)
for row in reader:
    gu = row[0] # 구값 추출
    dong = row[1] #동갑 추출
    t_li = [] #각 구와 동값이 들어갈 리스트

    for j in range(len(target_li)) :
        target = target_li[j]
        data = getAddressFromNaver("서울특별시"+gu+dong+target) # 서울특별시에 있는 구,동,타겟 값을 바꿔가면서 검색
        t_value = data['result']['totalCount'] #검샐결과중에서 전체 개수값만을 가져옴
        t_li.append(t_value)


    print (gu,dong, t_li)
#    writer.writerow([gu, dong, t_li[0], t_li[1], t_li[2], t_li[3], t_li[4], t_li[5], t_li[6], t_li[7], t_li[8]]) #결과파일에 쓰기
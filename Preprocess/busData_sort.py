__author__ = 'creator'

import requests
import csv

def match_loc(x, y) : # 좌표 x,y의 값에 해당하는 현재 위치를 반환하는 함수
    results = requests.get("http://rapi.daum.net/regioncode/getUnionResponse.JSON",
                           params={'x': x, 'y': y})
    anw = results.json()['codes']['hcode']['fullName']
    return anw

def changelocal (x,y): # x,y의 값의 좌표계를 TM좌표계에서 CONGNAMUL좌표계로 변환하는 함수
    results = requests.get("http://apis.daum.net/local/geo/transcoord",
                           params={'apiKey': 'c9bc480caaee4f7b4daf8be52c9f9216',#본인의 apiKey를 발급받아야합니다.
                                   'fromCoord': 'TM',
                                   'x': x,
                                   'y': y,
                                   'toCoord':'CONGNAMUL',
                                   'output':'json'
                                   })
    return (results.json())


reader = csv.reader(open('InputData/bus_loc_point.csv','r')) #제공받은 bus의 위치데이터가 들어있는 csv파일
writer = csv.writer(open('OutputData/bus_value_result.csv', 'w', newline=''))

past_header = False # 맨윗줄값을 건너뛰기 위한 변수
dong_li={}


for row in reader :
    if not past_header: # 첫번째 헤더값 넘어가기
        past_header = True
        continue

    k=changelocal(row[1],row[2]) #좌표계를 변환하여 값을 대입
    loc_x,loc_y=k['x'],k['y']
    match_dong=match_loc(loc_x,loc_y)
    #    print (row[0],match_dong,row[3]) #정류소 고유코드와 해당동, 지나가는 버스수를 출력 후, 입력

#서울특별시에 있는 동을 사전형식으로 저장
    if match_dong[:5]=='서울특별시': #값의 처음 이름이 서울특별시일 경우 실행
        if match_dong in dong_li: #매칭되는 동이 사전에 이미 있는 경우
            dong_li[match_dong][1]+=1 #기존의 사전의 첫번째 값[버스 정류장수에 1을 더함
            dong_li[match_dong]=[ int(dong_li[match_dong][0])+int(row[3]) , dong_li[match_dong][1]] #사전의 값에 첫번재는 전체 버스의수, 두번째에는 정류장의수를 반복적으로 합산

        else:   # 사전에 매칭되는 값이 없는경우, 현재 버스의수와 버스 정류장의 수를 1로 초기화 시킴.
            dong_li[match_dong]=[int(row[3]),1]

        print ('번호: ',row[0],'   동:',match_dong,' 버스의 수: ',dong_li[match_dong][0],' 정류장수: ',dong_li[match_dong][1]) #반복출력값


writer.writerow([ '번호','동이름','버스의 수','정류장의 수' ]) # 헤더부분 추가

count = 1
for x in dong_li:
    writer.writerow([count,x,dong_li[x][0],dong_li[x][1]]) #번호 동에 전체 버스의 수와 버스 정류장의 수값을 입력
    count+=1

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

reader = csv.reader(open('bus_loc_point.csv','r')) #제공받은 bus의 위치데이터가 들어있는 csv파일
writer = csv.writer(open('bus_value_result.csv', 'w', newline=''))

past_header = False # 맨윗줄값을 건너뛰기 위한 변수

writer.writerow(['버스정류장 코드','동이름','버스수'])

for row in reader :
    if not past_header:
        past_header = True
        continue
    k=changelocal(row[1],row[2]) #좌표계를 변환하여 값을 대입
    loc_x,loc_y=k['x'],k['y']

    print (row[0],match_loc(loc_x,loc_y),row[3]) #정류소 고유코드와 해당동, 지나가는 버스수를 출력 후, 입력
    writer.writerow([row[0],match_loc(loc_x,loc_y),row[3]])
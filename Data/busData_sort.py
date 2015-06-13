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
writer = csv.writer(open('bus_value_result_temp.csv', 'w', newline=''))

past_header = False # 맨윗줄값을 건너뛰기 위한 변수

writer.writerow(['버스정류장 코드','동이름','버스수'])

for row in reader :
    if not past_header:
        past_header = True
        continue
    k=changelocal(row[1],row[2])
    loc_x,loc_y=k['x'],k['y']

    print (row[0],match_loc(loc_x,loc_y),row[3])
    writer.writerow([row[0],match_loc(loc_x,loc_y),row[3]])


"""
    k=changelocal(float(busstop_li[i][1]),float(busstop_li[i][2]))
    loc_x,loc_y=k['x'],k['y']
    dong = match_loc(loc_x, loc_y)

    print (busstop_li[i][0],dong,busstop_li[i][4][0])
    writer.writerow([busstop_li[i][0], dong, busstop_li[i][4][0]])
"""

"""
for row in reader :
    if not past_header:
        past_header = True
        continue

    if row[0] not in stn_li :
        busstop_li.append((loc_id, loc_x, loc_y, len(temp_bus), temp_bus)) # [ 정류소고유코드, (좌표x,좌표y), 지나가는버스수, 지나가는버스목록 ]
        temp_bus = []	# 버스 리스트 리셋
        loc_id = row[0]

        stn_li.append(loc_id)
        (loc_x, loc_y) = (row[1], row[2])
        temp_bus.append(row[3])

print("서울 버스정류장수 :", len(busstop_li))
print(['버스정류장 코드','동이름','버스수'])

print (busstop_li[1])
writer = csv.writer(open('bus_value_result_temp.csv', 'w', newline=''))
writer.writerow(['버스정류장 코드','동이름','버스수'])

for i in range(1,len(busstop_li)):

    k=changelocal(float(busstop_li[i][1]),float(busstop_li[i][2]))
    loc_x,loc_y=k['x'],k['y']
    dong = match_loc(loc_x, loc_y)
    print (busstop_li[i][0],dong,busstop_li[i][4][0])
    writer.writerow([busstop_li[i][0], dong, busstop_li[i][4][0]])
"""
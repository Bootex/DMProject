__author__ = 'creator,seodebt'

## 서울시 버스 정보 데이터
import csv #버스데이터 값을 정리하기 위한 전처리 과정

reader = csv.reader(open('InputDate/bus_station_list.csv','r'))
wt = csv.writer(open('InputData/stn_loc_point.csv', 'w'))

bus_stop = []; stn_li = [] ; temp_bus = []
loc_id = 0 ; (loc_x, loc_y) = (0,0)

#past_header = False

for row in reader :
	if row[0] not in stn_li :
		#bus_stop.append((loc_id, loc_x, loc_y, len(temp_bus), temp_bus))
		# [ 정류소고유코드, (좌표x,좌표y), 지나가는버스수, 지나가는버스목록 ]
		wt.writerow([loc_id, loc_x, loc_y, len(temp_bus), temp_bus])
		temp_bus = []	# 버스 리스트 리셋
		loc_id = row[0] ; stn_li.append(loc_id)
		(loc_x, loc_y) = (row[1], row[2])
		temp_bus.append(row[3])
	else :
		temp_bus.append(row[3])

print("서울 버스정류장수 :", len(bus_stop))

# 처리 결과 저장 : 서울 버스정류장수는 13301개
__author__ = 'creator'

import csv
from bs4 import BeautifulSoup

reader = csv.reader(open('InputData/dongCode_value_fianl.csv','r'),delimiter=",")
svg = open('InputData/seoul_dong_prev.svg','r').read()#지도 이미지 파일 로드

dong_count = {}
count_a = []
min_value = 100; max_value = 0; first_header = False

for row in reader:#첫 헤더값 무시
    if not first_header:
        first_header=True
        continue

    try:
        unique = row[0]
        count = float(row[1].strip() )
        dong_count[unique] = count
        count_a.append(count)

    except:
        pass

soup = BeautifulSoup(svg) #

paths = soup.findAll('g')
colors = ["#CCCCCC","#66A3FF","#3385FF","#FFFF00","#003D99","#FF0000"]
g_style = "font-size:12px;fill-rule:nonzero;stroke:#FFFFFF;stroke-opacity:1;stroke-width:0.1;stroke-miterlimit:4;stroke-dasharray:none;stroke-linecap:butt;marker-start:none;stroke-linejoin:bevel;fill:"

for p in paths:
    try:
        count = dong_count[p['id']]
    except:
        continue

    if count > 100:#red
        color_class = 5

    elif count > 90:#blue
        color_class = 4

    elif count > 80: #Yellow
        color_class = 3

    elif count > 30:
        color_class = 2

    elif count > 10:
        color_class = 1

    else:
        color_class = 0

    color = colors[color_class]
    p['style'] = g_style + color

print (soup.prettify())

f = open("OutputData/map_ranking.svg",'w')
f.write(soup.prettify())

#출처코드 http://visualize.tistory.com/47
#-*- coding:utf-8 -*-

# 파이썬 문자열, 리스트, 딕셔너리 다루기 마스터해보자

import json

with open('./swit_chat.json', 'r', encoding='UTF8') as jsonfile:
    swit_chat_data = json.load(jsonfile)
    #print(swit_chat_data)

# swit_chat_data 에 담긴 데이터는 실제 광주인공지능사관학교 스윗의 데이터이다.
# 문제 :
# 가장 많이 글을 쓴 채팅을 작성한 사람은 누구일까..?

# 힌트 ) 유저 별 content 수를 세서 누가 가장 많이 썼을지 알아보기

use_list = []
tmt = [0,'가장 자주 채팅을 작성한 사람']

for i in range(len(swit_chat_data['data'])):
    if swit_chat_data['data'][i]['content'] != 0:
        use_list.append(swit_chat_data['data'][i]['user_name'])

for user in use_list:
    cnt = use_list.count(user)
    if tmt[0] < cnt:
        tmt[0] = cnt
        tmt[1] = user

print("가장 자주 채팅을 작성한 사람 : "+tmt[1]+"(%d회)" %tmt[0])
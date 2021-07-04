########################################################
# 텍스트 파일 쓰기

with open("test.txt", "w", encoding="utf8") as f:
    for i in range(10):
        f.write(str(i) + "번째 줄입니다\n") # \n = 줄바꿈

# 텍스트 파일 읽기
#with open("keywords.txt", "r", encoding = "utf8") as f:
    #for line in f:
        #print(line, end="") # 경로적어야할 때 역슬래쉬2번, 그냥 슬래쉬1번

fileList = ["test.txt", "test2.txt", "test.txt"] #요소 하나하나가 지금 텍스트 파일
for fileName in fileList:
    try:
        with open(fileName, "r", encoding="utf8") as f:
            for line in f:  # 텍스트 파일(f)을 리스트로 간주하면
                print(line, end="") # 요소 하나하나(line)는 텍스트 한줄이 됨.
        print("-----------파일 하나 끝났습니다", fileName)
    except: # try 문에서 에러 발생시 이 부분 실행
        print("에러가 났습니다, 아마도 파일이 없는듯합니다ERROR")


#########################################################
# 날짜 처리

from datetime import datetime
nowTime = datetime.now()
print(nowTime)
print(nowTime.date())
print(nowTime.time())
print(nowTime.strftime("%d.%m.%Y"))     #strftime : 날짜형식 조정
print(nowTime.strftime("%d.%m.%y"))

timeString = "30/06/2021"
parsedTime = datetime.strptime(timeString, "%d/%m/%Y")
print(parsedTime)
print(parsedTime.strftime("%Y년 %m월 %d일"))

#################################################3
#dictionary

# dictionary 변수 : 실제 사전책 하나
# key : 단어
# value : 단어의 뜻
# 중복 불가 = 고유함
# 차이점 : 파이썬 dictionary는 key들이 정렬되어있지는 않음


#dictionary 생성
    # method1
        # 빈 딕셔너리 만들기 : dict = {}, cf. 빈리스트 만들기 : list = []
        # dict["Key1"] = "value"
    # method2
        # dict = {"key1" : "value1", "key2"="value2"}
exDict = {}
exDict["막말"] = "되는대로 함부로 하느느 말"
exDict["막무가내"] = "내 아들놈"
print(exDict) # {'막말': '되는대로 함부로 하느느 말', '막무가내': '내 아들놈'}

#dictionary 접근
    # 1. key 입력하면 value 나옴
        # print(dict["key1"]) --> dict은 사전! []
        # print(dict.get("key")) --> get은 함수! ()
    # 2. key, value, 둘다 불러오기
        # print(exDict.keys())
        # print(exDict.values())
        # print(exDict.items())
print(exDict["막말"])
print(exDict.get('막무가내'))
print(exDict.get('내 아들놈'))  # value입력하면 안나옴
print(exDict.keys())

print("+++++++++++++")
for i in exDict: #list 처럼 dict도 ㅇㅇ
    print(i, exDict.get(i), sep="\t")

print("============")
for key in exDict: # 요소는 key가 된다.
    print(key, exDict.get(key), sep="\t")



print("============")
for key in exDict.keys():
    print(key, exDict.get(key), sep="\t")

print("============")
for v in exDict.values():
    print(v, sep="\t")

print("============")
for k, v in exDict.items(): #[('막말', '되는대로 함부로 하느느 말'), ('막무가내', '내 아들놈')] list 요소가 tuple(?)
    print(k, v, sep="\t")

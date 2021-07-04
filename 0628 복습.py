# 1. 폴더, 새파일 생성 : alt + insert
# 2. 복제 : ctrl + d (shift로 이동)
# 3. 삭제 : ctrl + y
# 4. 실행취소(undo) : ctrl + z
#    실행 취소 한걸 재실행 (redo) : ctrl + shift + z
# 5. 편집창 닫기 : ctrl + f4
#    파이참 종료 : alt + f4
# 6. 실행하기(run)
# 	1) 파일 선택해서 run : alt + shift +f10
#   2) 현재파일 run : ctrl + shift + f10
#   3) 재실행 run : shift + f10
# 7. 화면 이동 : ctrl + tap (ctrl 키 누른채로 방향키)
# 8.  파일 , 폴더 이름 변경 : shift + f6
# 9. ()소괄호 밖 탈출 : ctrl + shift + enter
# 10. 주석처리 및 해제 : ctrl + / (영역 지정후)

###################################
# end= 끝을 어떻게 처리할 건지
    # end = "" 끝에 아무것도 없어
    # end = "\n" 끝에 엔터
    # end = "/n" 끝에 tab
print(2, end="")
print(33)

print(2, end="\n")
print(33)

####################################
# input은 숫자도 str로 받아 따라서 연산시 int로 type변환필요
# age = input("숫자로 입력해도 문자로 받는지 보자:")
# print(type(age))

####################################
# strip() str에 앞뒤 공백 있으시 제거해줌. (strip("apple")과 .strip()차이?
str4 = "        앞뒤로 공백이 존재한다면           "
print(str4)
print(str4.strip())

# strip() , append() 같은 함수는 메소드로 변수와 . 로 연결지어서 사용

#####################################
# split() 특정 문자열로 문자열을 분리하는 함수
    #여기선 12라는 문자열로 '오늘', '점심은', '뭐먹을까' 이렇게 3개의
    #단어로 분리함. 즉 인덱스는 앞 공백 포함 3까지 (0~4)
str5 = "12오늘12점심은12뭐먹을까"
print(str5[3])
#문자열은 []로 인덱스표시가능

splitResult = str5.split("12")
print(splitResult[0])
print(splitResult[1])
print(splitResult[2])
print(splitResult[3])

#DIY
diyString = "   처음에 글이 있고 중간에는        공백이 길고, 끝부분에는 공백이 짧아요   "
print(diyString)
print(diyString.strip())

splitResult2 = diyString.split("공백")
print(splitResult2)
print(splitResult2[1])
print(splitResult2[2])

print(diyString.strip().split("공백")[1][4]) # ,나옴
print(diyString.strip().split("공백")[0][2])  # 에 나옴
# strip하고 split을 해 그 결과에서 첫번째(0인덱스) 구에서 3번째(2번째 인덱스) 출력




############################################
exampleList = [2, 3, 4, 6, "2", 2, 2]
print(exampleList[3])   #인덱스번호가 3번째 인애 출력
print(exampleList.index(3)) #3의 인덱스 번호를 출력해봐
print(exampleList.index("2")) #문자 2의 인덱스 번호를 출력해봐   .index()
print(exampleList.count(2)) #   .count()

############################################
# range(시작인덱스, 끝인덱스전까지, 건너뛰는크기)
#   같은 것끼리 묶으면
for i in range(3, 10, 1):
     print(i)

for i in [3, 4, 5, 6, 7, 8, 9]:
    print(i)

#   같은 것끼리 묶으면 2
for i in range(3):
    # for i in range(0, 3):
    # for i in range(0, 3, 1):
    print(i)

######################################
#DIY 별 만들기

#1
for numOfstars in range(1,6):
    print("*" * numOfstars)

#2
for numOfstars in range(0,5):
    print("*" * (2 * numOfstars + 1))

for numOfstars in range(1, 10, 2):
    print("*" * numOfstars)

#3
for numOfstars in range(5, 0, -1):
    print("*" * numOfstars)     # 5에서 1까지 -1만큼 줄어드는

for numOfstars in range(0,5):
    print("*" * (5 - numOfstars))

#4
for numOfstars in range(1, 10, 2):
    print(" " * int((9 - numOfstars) / 2), end = "")
    print("*" * numOfstars)

for lineNumber in range(1, 6):  #행번호 관점
    # 공백 찍기 : 1행 -> 4, 2행 -> 3개
    # 공백은 5 - 행번호
    print(" " * (5 - lineNumber), end="")

    # 별 찍기 : 행번호 * 2 - 1
    print("*" * (lineNumber * 2 - 1))

#5

for i in range(1,6):
    print(" " * i, end="")
    for number in range(1, 6 - i + 1):
        print(number, end="")
    print()

# print()를 안하면 1234 123 12 1 돼

#6
for i in range(1, 6):
    print(" " * (i - 1), end="")
    for number in range(1, 6 - i + 1): # 6 - i는 (1,5) 인데 이건 1부터 4까지
        print(number, end="")
    for num in range(5 - i, 0, -1): #(4,0)이니까 5,4,3,2,1이고 여기서 -1이니까 4,3,2,1,0임
            print(num, end="")

    print()


##################################################
print(2, end="\n") # print 함수는 end인자의 기본값이 \n
print(3)
print(2, 3, 4, 5, 6, sep="")
print(2, 3, 4, 5, 6)

###########################################
#DIY 3

for



import random







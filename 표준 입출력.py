#표준 입출력

print("Python","Java",sep=",")
print("Python","Java",sep="vs")
print("Python","Java","JavaScript",sep="vs")
print("Python","Java",sep=",",end="?") #end ? 뒤에 다음 출력문이 바로붙음
print("무엇이 더 재밌을까요?")


import sys
print("Python","Java",file=sys.stdout) #표준출력
print("Python","Java",file=sys.stderr) #표준에러


#시험 성적
scores={"수학":0,"영어":50, "코딩":100} #사전
for subject,score in scores.items(): #key와 value를 쌍으로 보내줌
      #print(subject,score)
      print(subject.ljust(8),str(score).rjust(4),sep=":") #subject는 왼쪽에 8칸 확보후 왼쪽으로정렬
                                                  #score는 오른쪽에 4칸 확보후 오른쪽으로정렬


#은행 대기 순번표
#001,002,003, ....

for num in range(1,21): #1~20의 num 생성.
    #print("대기번호:{0} " .format(str(num)))
    print("대기번호 : " +str(num).zfill(3)) #zfill(3)은 공간 3개확보후 숫자부분을 제외한 나머지는 0으로 채움.

    


answer=input("아무 값이나 입력하세요 : ") #사용자 입력을 받을땐 항상 문자열로 받음.

print(type(answer))
print("입력 하신 값은 "  +answer+ "입니다")
                                            



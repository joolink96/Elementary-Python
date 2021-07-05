#파일 입출력

#case 1
score_file=open("score.txt","w",encoding="utf8")
print("수학 : 0", file=score_file)
print("영어 : 50",file=score_file)
score_file.close()

#case2
score_file=open("score.txt","a",encoding="utf8") #a는 append를 의미
score_file.write("과학 :80 ")
score_file.write("\n코딩 : 100 ")
score_file.close()

#case 3
score_file=open("score.txt","r",encoding="utf8")
print(score_file.read())
score_file.close()

#case 4
score_file=open("score.txt","r",encoding="utf8")
print(score_file.readline()) # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()

#case 5
score_file=open("score.txt","r",encoding="utf8")
while True:
    line=score_file.readline()
    if not line:
        break
    print(line,end="") #줄 바꿈 없이
    print("\n")

score_file.close()

#case 6
score_file=open("score.txt","r",encoding="utf8")
lines=score_file.readlines() #list 형태로 저장
for line in lines:
    print(line,end="")



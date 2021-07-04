# def profile(name,age,lang1,lang2,lang3,lang4,lang5):
#     print("이름 : {0} \t 나이 : {1} \t " .format(name,age),end=" ")
#     print(lang1,lang2,lang3,lang4,lang5)


def profile(name,age,*language): #서로 다른 개수의 값을 넣어줄때는 <가변인자>를 사용 !!

    print("이름 : {0} \t 나이 : {1} \t " .format(name,age),end=" ")
    for lang in language:
        print(lang, end=" ")
    print() #줄바꿈




profile("유재석",20,"Python","Java","C","C++","C#","JavaScript")
profile("김태호",25,"Kotlin","Swift","","","")
    
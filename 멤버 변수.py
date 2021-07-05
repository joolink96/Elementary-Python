#멤버 변수

class Unit:
    def __init__(self,name,hp,damage):
        self.name=name  #멤버변수
        self.hp=hp      #멤버변수
        self.damage=damage  #멤버변수
        print("{0}유닛이 생성 되었습니다" .format(self.name))
        print("체력 {0}, 공격력 {1}" .format(self.hp,self.damage))


# marine1= Unit("마린",40,5) #객체
# marine2= Unit("마린",40,5) #객체
# tank=Unit("탱크",150,35)   #객체

# 레이스 : 궁중 유닛, 비행기 . 클로킹(상대방에게 보이지 않음)

wraith1=Unit("레이스",80,5)
print("유닛 이름: {0},공격력 :{1}" .format(wraith1.name,wraith1.damage)) #클래스 내부에있는 멤버변수를 외부에서 사용


# 마인드 컨트롤 : 상대방 유닛을 내것으로 만드는것(빼았음)

wraith2=Unit("빼았은 레이스",80,5)
wraith2.clocking=True
if wraith2.clocking==True:
    print("{0}는 현재 클로킹 상태입니다." .format(wraith2.name))
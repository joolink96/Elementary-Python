#다중상속


#일반유닛
# class Unit:

#     def __init__(self,name,hp):

#       self.name=name  #멤버변수
#       self.hp=hp      #멤버변수
         
         

# #공격유닛
# class AttackUnit(Unit): #공격유닛은 일반유닛 클래스를 상속받음
#     def __init__(self,name,hp,damage):
#         Unit.__init__(self,name,hp)
#         self.damage=damage  #멤버변수

#     def attack(self,location):
#         print("{0}: {1}방향으로 적군을 공격 합니다.[공격력 {2}]"\
#             .format(self.name,location,self.damage))    

#     def damaged(self,damage):
#      print("{0}: {1}데미지를 입었습니다." .format(self.name,damage))
#      self.hp-=damage
#      print("{0}:현재 체력은 {1}입니다." .format(self.name,self.hp))
#      if self.hp<=0:
#          print("{0} : 파괴되었습니다." .format(self.name))


#드랍쉽 : 공중 유닛, 수송기. 마린/파이어뱃/탱크 등을 수송. 공격기능 x

class Flyable: #날수있는 기능을 가진 클래스
    def __init__(self,flying_speed):
      self.flying_speed=flying_speed

    def fly(self,name,location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 : {2} ]" \
            .format(name,location,self.flying_speed))


#공중 공격 유닛 클랫

class FlyableAttackUnit(AttackUnit,Flyable):
    def __init__(self,name,hp,damage,flying_speed):
     AttackUnit.__init__(self,name,hp,damage)
     Flyable.__init__(self,flying_speed)


#발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사

valkyrie=FlyableAttackUnit("발키리",200,6,5)
valkyrie.fly(valkyrie.name,"3시")
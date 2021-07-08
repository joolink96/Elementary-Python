#모듈 직접 실행

# import travel.thailand  #import 뒤에는 모듈이나 패키지만 정의 가능.
# #import travel.thailand.ThailandPackage #이 형태처럼 import 뒤에 클래스는 정의 불가능.

# trip_to=travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage #from import에서는 모듈,패키지,클래스 다 정의 가능.
# trip_to=ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to=vietnam.VietnamPackage()
# trip_to.detail()

# from random import *
from travel import * #travel 내에 있는 모듈을 전부 사용
trip_to=thailand.ThailandPackage()
trip_to.detail()



# class ThailandPackage:  <<<<이 부분을 thailand.py 라는 모듈에 추가 해주기!!!>>>>
#     def detail(self):
#         print("[태국 패키지 3박 5일] 방콕,파타야 여행(야시장 투어) 50만원")


# if __name__ =="__main__": #모듈 직접실행 
#     print("Thailand모듈을 직접 실행")
#     print("이 문장은 모듈을 직접 실행할 때만 실행되요")
#     trip_to=ThailandPackage()
#     trip_to.detail()

# else:  #외부에서 모듈 실행
#     print("Thailand 외부에서 모듈 호출") 
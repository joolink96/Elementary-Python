#패키지

# import travel.thailand  #import 뒤에는 모듈이나 패키지만 정의 가능.
# #import travel.thailand.ThailandPackage #이 형태처럼 import 뒤에 클래스는 정의 불가능.

# trip_to=travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage #from import에서는 모듈,패키지,클래스 다 정의 가능.
# trip_to=ThailandPackage()
# trip_to.detail()

from travel import vietnam
trip_to=vietnam.VietnamPackage()
trip_to.detail()
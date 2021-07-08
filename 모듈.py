#모듈   thearter_module.py 파일에 함수 각각 선언해줘야함.

# case 1)
# import theater_module
# theater_module.price(3) #3명이서 영화보러 갔을때 가격
# theater_module.price_morning(4) #4명이서 조조할인 영화 보러 갈때
# theater_module.price_soldier(5) #5명의 군인이 영화 보러 갔을 때

# case 2)

# import theater_module as mv #모듈명을 변경

# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# case 3)

# from theater_module import *
 
# price(3)
# price_morning(4)
# price_soldier(5)

# case 4)

# from theater_module import price,price_morning #이 두 함수만 씀.
# price(5)
# price_morning(6)
# # price_soldier(7) #오류 (사용불가)

#  case 5)

# from theater_module import price_soldier as price #soldier함수만 쓰는데 price로 줄여서 씀
                                            #여기서 price는 원래있던 price가 아닌 price_soldier 임.

 
# price(5)
 
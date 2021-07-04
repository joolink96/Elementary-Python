#정렬도 가능

num_list=[5,2,4,3,1]
num_list.sort()
print(num_list)

#순서 뒤집기

num_list.reverse()
print(num_list)

#모두 지우기
num_list.clear()
print(num_list)


#다양한 자료형 함께 사용
num_list=[5,2,4,3,1]
mix_list=["조세호",20,True]
print(mix_list)

num_list.extend(mix_list)
print(num_list)
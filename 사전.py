cabinet = {3: "유재석",100: "김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
#print(cabinet[5]) #에러 (데이터 값이 없음)

print(cabinet.get(5,"사용가능")) 

print(3 in cabinet) #True
print(5 in cabinet) #False

cabinet={"A-3":"유재석","B-100":"김태호"} 
print(cabinet["A-3"])
print(cabinet["B-100"])

#새 손님
print(cabinet)
cabinet["A-3"]="김종국"
cabinet["C-20"]="조세호"
print(cabinet)

#간 손님
del cabinet["A-3"]
print(cabinet)

# 현재있는key 들만 출력
print(cabinet.keys())

# 현재있는 values 들만 출력
print(cabinet.values())

#현재있는 key,value 쌍으로 출력
print(cabinet.items())

#목욕탕 폐점

cabinet.clear()
print(cabinet)





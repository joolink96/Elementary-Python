#예외처리 (에러를 처리해줄수 있는 기능)


try: #try내부에서 문제가 발생시 밑에 except문 출력


    print("나누기 전용 계산기입니다")
    nums=[]
    nums.append(int(input("첫번째 숫자를 입력하세요: ")))
    
    nums.append(int(input("두번째 숫자를 입력하세요: ")))

    #nums.append(int(nums[0]/nums[1]))

    print("{0}/{1}={2}" .format(nums[0],nums[1],int(nums[2])))


except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")


except ZeroDivisionError as err:
    print(err)

except Exception as err:
     print("알 수 없는 에러가 발생하였습니다.")
     print(err)
     
# except:   #위에 except문에 없는 에러는 여기에 해당
#     print("알 수 없는 에러가 발생하였습니다.")
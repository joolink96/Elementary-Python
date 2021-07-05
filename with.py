#with

# import pickle


# with open("profile.pickle","rb") as profile_file:
#     print(pickle.load(profile_file))



# with open("study.text","w",encoding="utf8") as study_file: #파일 쓰기
#     study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.text","r",encoding="utf8")as study_file: #파일 읽기
    print(study_file.read())

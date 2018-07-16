#딕셔너리 내부에 키 존재 확인

dictionary ={
    "name" :"7D 건조 망고",
     "type" :"당절임",
    "ingredient" :["망고" ,"설탕" ,"메타뭐>", "치자"],
    "origin" :"필리핀"
}

#print(dictionary["game"]) #KeyError

if "game" in dictionary:
    print( dictionary["game"])
else :
    print("No existing key")

'''dictionary. 를 해보면 많은 도구가 있다'''
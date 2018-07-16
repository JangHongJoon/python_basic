#딕셔너리 get() 함수
dictionary ={
    "name" :"7D 건조 망고",
     "type" :"당절임",
    "ingredient" :["망고" ,"설탕" ,"메타뭐>", "치자"],
    "origin" :"필리핀"
}

value = dictionary.get("game") #딕셔너리 키로 값을
                                #추출해낸다

                                
print("값:" ,value)

if value==None:
    print("No Existence.")
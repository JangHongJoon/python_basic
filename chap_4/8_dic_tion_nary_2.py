#딕셔너리 요소 접근
dictionary ={
    "name" :"7D 건조 망고",
     "type" :"당절임",
    "ingredient" :["망고" ,"설탕" ,"메타뭐>", "치자"],
    "origin" :"필리핀"
}

#출력
print(dictionary["name"])
print(dictionary["type"])
print(dictionary["ingredient"])
print(dictionary["origin"])

print()

#값 변경
dictionary["name"] ="8D 건조 망고"
print("name: ",dictionary["name"])
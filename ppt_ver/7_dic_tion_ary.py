#딕셔너리를 선언합니다
dictionary={
    "이름":"Paul",
    "나이":"20",
    "거주지":"Gimhae",
    "관심사":"음악"
}
#딕셔너리를 출력합니다
print(dictionary)

#딕셔너리의 요소를 출력합니다
print(dictionary["이름"])

#딕셔너리에 키와 값을 추가합니다
dictionary["장래희망"]="뮤지션"
print(dictionary)

#딕셔너리의 요소를 제거합니다
del dictionary["이름"]
print(dictionary)
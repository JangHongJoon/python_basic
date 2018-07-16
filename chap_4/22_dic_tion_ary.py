dictionary={
    "key1":"ant",
    "key2":"bee",
    "key3":"cake"
}

print("#딕셔너리의 items() 함수")
print("items():",dictionary.items())
print()


for key,element in dictionary.items():
    print("dictionary[{}]= {}".format(key,element))

a_list=["1","2","3"]
b_list=["a","b","c"]

for i in range(len(a_list)):
    print(a_list[i],b_list[i])
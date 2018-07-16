import random as ran

print(ran.random()) #실수 형태로 랜덤한 수 출력
print(ran.uniform(2.5,10.0)) #실수 2.5 와 10.0 에서 2.5 초함 랜덤
print(ran.expovariate(1/5)) #?
print(ran.randrange(10)) # 10 실수 밑으로 랜덤 출력\
print(ran.randrange(0,101,2)) # 2칸 간격으로 0부터 100 까지
print(ran.choice(['win','lose','draw']))
deck="Make it this great".split()
deck_sh=ran.shuffle(deck)
print(deck_sh)
print(ran.sample(deck,k=2))



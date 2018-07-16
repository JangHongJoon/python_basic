import random
hanguls=list("가나다라마바사아자차카타파하")

with open("brexit.txt","w") as file:
    for i in range(1000):
        name = random.choice(hanguls) + random.choice(hanguls) # list에서 랜덤 선택
        weight = random.randrange(40,100)
        height = random.randrange(140,200)
`
        #텍스트를 씁니다.

        file.write("{}, {}, {}\n".format(name,weight,height))

    with open("brexit.txt" ,"r") as file:
        for line in file:
            (name, weight, height) = line.strip().split(",")
            if (not name) or (not weight) or (not height):
                continue

            bmi =int(weight)/(int(height) * int(height))
            result=""

            if 25 <= bmi:
                result="과체중"
            elif 18.5 <= bmi :
                result="정상체중"
            else :
                result = "저체중"

            print()
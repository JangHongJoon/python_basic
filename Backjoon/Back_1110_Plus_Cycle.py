num = int(input(""))

front = int(num / 10)
back = int(num % 10)

ori_front = front
ori_back = back

cnt = 0
hap = 0

while(True):
    hap = front + back
    cnt += 1
    if ori_front == back and ori_back == hap % 10:
        print(cnt)
        break
    else:
        front = back
        back = hap % 10


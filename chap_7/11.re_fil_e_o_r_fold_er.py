import os

def read_folder(path,cnt):
    output = os.listdir(path)
    for path in output:
        if os.path.isdir(path):  # 매개변수가 폴더(디렉터리) 이면 True
            for i in range(cnt): print("    ",end="")
            print("폴더:", path)
            read_folder(path,cnt+1)
        else:
            for i in range(cnt): print("    ", end="")
            print("파일:", path)

output = os.listdir(".") #.매개변수의 내부 폴더 파일 출력


for path in output:
    if os.path.isdir(path): # 매개변수가 폴더(디렉터리) 이면 True
        print("폴더:",path)
        read_folder(path,1)
    else :
        print("파일:",path)
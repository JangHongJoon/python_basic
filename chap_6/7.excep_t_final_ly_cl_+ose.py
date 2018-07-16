try:
    file=open("file.txt","w")
    예외.발생해라()
    file.close()
except Exception as e:
    print(e)
    print(file.closed)
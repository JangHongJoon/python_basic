from urllib import request

target = request.urlopen("https://google.com")
output = target.read()

print(output)

#b' -> 바이너리 데이터 라는 뜻

from urllib import request

target = request.urlopen("https://www.google.com/logos/doodles/2018/hubert-cecil-booths-147th-birthday-5355133176119296-law.gif")
out=target.read()
print(out)

file = open("out.png","wb")
file.write(out)
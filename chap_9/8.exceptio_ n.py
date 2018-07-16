'''
class CustomException(Exception):
    def __init__(self):
        Exception.__init__(self)
raise CustomException

Traceback (most recent call last):
  File "C:/Users/PAUL/Desktop/Python/chap_9/8.exceptio_ n.py", line 4, in <module>
    raise CustomException
__main__.CustomException
'''

'''
class CustomException(Exception):
    def __init__(self):
        Exception.__init__(self)
        print("### My Error Errupted! ###")
    def __str__(self):
        return "ERROR ERRUPTED"
raise CustomException

Traceback (most recent call last):
### My Error Errupted! ###
  File "C:/Users/PAUL/Desktop/Python/chap_9/8.exceptio_ n.py", line 19, in <module>
    raise CustomException
__main__.CustomException: ERROR ERRUPTED
'''


class CustomException(Exception):
    def __init__(self,message,value):
        Exception.__init__(self)
        self.message = message
        self.value = value

    def __str__(self):
        return self.message

    def print(self):
        print("### 오류 정보 ####")
        print("메세지:", self.message)
        print("값:", self.value)

try:
    raise CustomException("딱히 이유 없음",273)
except CustomException as e:
    e.print()

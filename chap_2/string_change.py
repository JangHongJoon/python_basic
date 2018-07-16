#자료형식 출력
output_a=int("52")
output_b=float("52.273")

print(type(output_a),output_a)
print(type(output_b), output_b)

#input() 함수와 float() 함수 조합
input_a = float(input("입력 >"))
input_b = float(input("입력 >"))

print("덧셈 결과:", input_a + input_b)
print("뺄셈 결과:", input_a - input_b)
print("곱셈 결과:", input_a * input_b)
print("나눗셈 결과:", input_a / input_b)

#잘못된 자료형 변환
int("안녕하세요")
float("안녕하세요")

int("52.273")


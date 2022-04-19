# 입력받은 숫자를 split()을 활용해서 띄어쓰기를 기준으로 나누어주고 map을 사용해 int로 변환
a, b = map(int, input().strip().split(' '))
# 행의 개수만큼 반복
for i in range(b):
    # 별의 개수만큼 반복
    for j in range(a):
        # 다음줄로 넘어가기 위해 end=''
        print('*', end='')
    print()


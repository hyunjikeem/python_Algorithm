# 첫째 줄에 N (1 <= N <= 100) 과 M (1 <= M <= 100) 이 주어짐
N, M = map(int, input().split())

# 둘째 줄에는 M개의 줄에 걸쳐서 공을 넣는 방법이 주어짐
# 각 방법은 세 정수 i j k 로 이루어져 있음
# i 번 바구니부터 j 번 바구니까지에 k번 번호가 적혀져 있는 공을 넣는다는 뜻

basket = [0]*N

for _ in range(M):
    i,j,k = map(int, input().split())
    for idx in range(i, j+1):
         basket[idx-1] = k
# 1번 바구니부터 N번 바구니에 들어있는 공의 번호를 공백으로 구분해 출력. 공이 들어있지 않은 바구니는 0을 출력
for i in range(N):
    print(basket[i], end=' ')



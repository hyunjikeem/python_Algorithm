# 첫 줄에는 영수증에 적힌 총 금액 X가 주어짐
# The first line contains the total amount X written on the receipt.
total = int(input())

# 둘째 줄에는 영수증에 적힌 구매한 물건의 종류의 수 N이 주어짐
# The second line contains the number N of different types of items purchased, as written on the receipt.
variety = int(input())

totalPrice = 0

# 둘째줄에서 받은 N개의 줄만큼 각 물건의 가격 a과 개수 b가 공백을 사이에 두고 주어짐
# The next N lines contain the price a and quantity b of each item, separated by a space.
for i in range(variety):
    price, number  = map(int, input().split())
    totalPrice += price * number

if totalPrice == total:
    print('Yes')
else:
    print('No')
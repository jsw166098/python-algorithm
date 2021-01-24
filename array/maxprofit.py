# 주식을 사고 팔기 가장 좋은 시점

## 브루트 포스로 계산

def maxProfit1(self, prices):
    max_price = 0

    for i, price in enumerate(prices):
        for j in range(i, len(prices)):
            max_price = max(prices[j] - price, max_price)

    return max_price

## 저점과 현재 값과의 차이 계산

def maxProfit2(self, prices):
    profit = 0
    min_price = sys.maxsize

    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price-min_price)

    return profit
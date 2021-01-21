# 주식을 사고 팔기 가장 좋은 시점

* 두 수의 차 중 가장 큰 값 
* 값을 그래프로 나열하여 대략 어떤 식으로 풀지에 대한 직관을 가진다.

## 내 풀이

~~~
    def maxProfit(self, prices):
        diff = 0
        diff_max = 0
        
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                diff = prices[j] - prices[i]
                if diff_max < diff:
                    diff_max = diff
        
        return diff_max
~~~

## 브루트 포스로 계산

~~~
    def maxProfit(self, prices):
        max_price = 0
        
        for i, price in enumerate(prices):
            for j in range(i, len(prices)):
                max_price = max(prices[j]-price, max_price)
        
        return max_price
~~~

## 저점과 현재 값과의 차이 계산 

~~~
def maxProfit2(self, prices):
    profit = 0
    min_price = sys.maxsize
    
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price-min_price)
        
    return profit
~~~

## 문법

### 최대 최소 나타내기

* 최댓값은 가장 낮은 값을 최솟값은 가장 높은 값을 초깃값으로 할당한다. 

#### sys 모듈 사용

~~~
sys.maxsize

-sys.maxsize
~~~

#### float() 사용하여 무한대 지정

~~~
mx = float('-inf')

mn = flost('inf')
~~~
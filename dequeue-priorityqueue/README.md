# 데크와 우선순위 큐

## 데크

* 양쪽 끝을 모두 추출할 수 있는 큐를 일반화한 형태의 추상 자료형이다.
* Double Ended Queue의 줄인 말
* 스택과 큐의 특징을 모두 가지고 있다. 
* 양쪽에서 삭제와 삽입이 기능하기 때문에 스택과 큐의 연산 구현이 가능하다.
* 양쪽으로 head와 tail이라는 이름의 두 폰인터를 갖는다.
* collections 모듈에서 deque를 통해 구현할 수 있다. 이는 이중 연결리스트로 구현되어 있다. 

## 우선순위 큐

* 우선순위 큐는 특정 조건에 따라 우선순위가 가장 높은 요소가 추출되는 자료형이다.
* 정렬 기준과 우선순위가 같다면 정렬 알고리즘을 통해 우선순위 큐를 구현할 수 있다. 
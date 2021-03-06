# 배열

### 자료구조 분류
* 메모리 공간 기반 연속 방식 -> 배열
* 포인터 기반 연결 방식 -> 연결 리스트

## 배열 특징
* 크기를 지정하고 해당 크기만큼의 연속된 메모리 공간을 할당받는 작업을 수행하는 자료형
* 크기가 고정되어 있으며 한번 생성한 배열은 크개 변경이 불가능하다.
* 어느 위치든 O(1)에 조회가 가능하다. -> 크기가 고정되어 있기 때문에 주소계산 가능, 값이 메모리에 직접적으로 담겨 있기 때문

## 동적 배열

* 크기가 자동으로 저정되는 배열
* 값 조회가 o(1)안에 가능하다.
* 초기값을 미리 잡아 배열을 생상헌 후 꽉 차게 되면 2배로 늘리게 되는 더즐링이 발생한다. 
* 파이썬의 그로스 팩터(재할당 비율, 성장 인자)는 초반에는 2배, 전체적으로 1.125배이다. 
* 동적 배열의 경우 더 큰 크기의 배열을 할당하며 기존 데이터를 복사해야 하기 때문에 최악의 경우 O(n) 시간 복잡도를 가진다.
* 최악의 경우는 자주 일어나지 않기 때문에 분할 상환 분석을 통해 O(1) 시간 복잡도를 가진다고 할 수 있다. 

## 문제

* 두 수의 합 -> 첫번째 수 미리 빼기, 투 포인터, in 접근
* 빗물 트래핑
* 세 수의 합 -> 투 포인터 사용 (투 포인터 이동시키는 기준 중요!)
* 배열 파티션 -> 파티션 중에서 큰 값들 -> 짝수 위치 가장 크다.
* 자신을 제외한 배열의 곱 -> 왼쪽, 오른쪽 나눠서 곱한다.
* 주식을 사고팔기 가장 좋은 시점 -> 포인터 이동시키면서 가장 저점 저장해놓았다가 가증 큰거 나오면 빼서 결과 알려준다.






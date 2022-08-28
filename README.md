# minimal_expression_generator - DEC 01 2021

## Digital Logic Circuit Design Project

minterm expression을 입력으로 받아, sum of products 형태의 minimal expression을 계산하는 프로그램

Quine mccluskey method 사용


#### Quine-McCluskey Method

사용한 알고리즘은 퀸-맥클러스키 방법으로, 최소항의 합을 이진법으로 표현했을 때, 한 변수만 다른 경우에 결합할 수 있음을 이용한다.

그래서 결합하여 새로운 column을 만들 수 있는데, 이때 새로운 column을 더 만들지 못하게 되는 항들이 prime implicants가 된다.

그 다음엔, prime implicants들의 최소 집합을 얻기 위해서 차트를 이용한다.

어떤 한 최소항이 단 하나의 prime implicants에 포함된다면, 그것을 essential prime implicants 라고 한다.

##### 자세한 내용은 코드에 주석으로 상세히 설명하였다.

<div align="center">
  <h1>💪🏻AlgorithmWithPython💪🏻</h1>
  <p>매일 한문제 파이썬 코딩 스터디!</p>
</div>

---
## ✨스터디방식

- 일주일에 7문제를 푼다.
- 할 수 있으면 하루에 한문제를 푼다. 다만 사정이 있는 경우 1주일에 7문제는 꼭 지키도록 한다.
- 문제의 순서는 백준 온라인 강의 -> [코딩테스트 준비 기초](https://code.plus/course/51), [코딩테스트 준비 연습](https://code.plus/course/52), [코딩테스트 준비 문제](https://code.plus/course/53)를 따르도록 한다. 
- 배운것에 대해 그 문제를 푼 당일 적어야한다. 
- 이름은 문제번호_문제이름으로 한다. (ex)2309_일곱난쟁이)

## 👩🏻‍💻문제

> **기초 - 브루트포스**


|                      |                                      #문제                                       |                                     #알고리즘 설명                                      |                                        #배운점                                        |
| :------------------: | :-------------------------------------------------------------------------------: | :-------------------------------------------------------------------------: | :------------------------------------------------------------------------------: |
| **2022.01.09일(일)** |    [일곱난쟁이](https://www.acmicpc.net/problem/2309)    | 아홉 난쟁이들의 키의 총 합을 구한 후 두 난쟁이의 키를 뺀다.<br/>이때 값이 100이면 출력   | del arr[1] or arr.remove(1)<br/>a.sort() or a = sorted(a)<br/>파이썬 함수에 아직 익숙하지 않은 듯 하다.. |
| **2022.01.10일(월)** |    [사탕 게임](https://www.acmicpc.net/problem/3085)    | 전체 맵에서 가장 긴 연속부분의 길이를 센다<br/>칸 두개를 바꾸면서 해당 줄의 가장 긴 연속부분의 길이를 센다.<br/>이때 row방향으로 칸 두개를 바꾸면, 해당 칸 두개의 column과 해당 row만 count해주면 된다.<br/>마찬가지로 column방향으로 칸 두개를 바꾸면, 해당 칸 두개의 row와 해당 column만 count해주면 된다.    |   |
| **2022.01.10일(월)** |    [날짜 계산](https://www.acmicpc.net/problem/1476)    |  1씩 더해주며 입력으로 들어온 값과 비교해준다.  |  변수 할당에도 if else문을 쓸 수 있어 편리했다. |
| **2022.01.11일(화)** |    [리모컨](https://www.acmicpc.net/problem/1107)    | 고장난 버튼이 없으면 100에서 +-로 움직인것과 버튼 누른것의 최솟값<br/>버튼이 모두 고장났으면 100을 빼준 값이 정답<br/>9999999이하의 숫자중 고장난 버튼을 제외한 나머지 버튼으로 만들 수 있는 수의 경우를 다 만들어본다.<br/>min( abs(N-100)[시작점에서 N까지 +-버튼을 누른 횟수], len(수)[수를 만들기위해 버튼을 누른 횟수] + abs(수 - N)[+-버튼 누른 횟수])이 정답이된다.<br/>0버튼을 눌러 0에서부터 횟수를 셀 수 있는데, 일의자리만 이 방법을 사용해서 틀렸었다. 10과 같은 수에도 유효하다. 조건문을 잘 보고 써야할 것 같다.  |  for문, if문 한줄에 쓸 수 있어 코드가 간결해진다.<br/>global변수를 사용할 때 유의해야한다.  |
| **2022.01.16일(일)** |    [카잉달력](https://www.acmicpc.net/problem/6064)    | x,y변수에 1씩더하여 범위 비교를 해줬던 날짜계산문제와 달리, 이 문제에서는 똑같이 하면 시간초과가 난다.<br/>그래서 이 문제를 풀때는 x의 값은 문제에서 주어진 값과 같게 맞춰놓고, y값을 더해서 범위 비교를 해주면서 cnt를 해주었다.<br/>이때 한번 나왔던 y의 값이 다시 나온다면, 이는 날짜를 찾을 수 없는 경우이므로 -1을 출력하게 해주었다. | 반례를 생각할 때 좀 더 깊이 생각해야 할 것 같다.<br/>알고리즘은 맞게 짠거같은데 자꾸 시간초과가 나서 보니, python은 input()으로 받아오면 느리기때문에 sys.stdin.readline()으로 받아오는것이 좋다는 것을 배웠다.<br/>또, 백준에서 언어 설정을 Python3로 했을때는 시간초과가 났는데, PyPy3으로 언어설정을 한 후 채점을 하니 맞았다<br/>c++은 통과하는 알고리즘을 파이썬으로 짜서 채점할 경우 시간초과가 나는 경우가 생긴다고 한다. 이때 PyPy3으로 채점한다고 한다.<br/>[이 블로그]( https://m.blog.naver.com/crm06217/221832195003)에서 위와 같은 점들을 배울 수 있었다. |
| **2022.01.16일(일)** |    [수 이어쓰기1](https://www.acmicpc.net/problem/1748)    | 시간제한이 0.15초였다. 수를 다 이어붙여서 길이를 재는것은 무리라는 생각이 들었다.<br/>N이 101일때, 1-9까지는 자릿수가 1개이므로 9x1, 10-99까지는 자릿수가 2개이므로 2x90 그리고 +2 이런식으로 곱셈을 이용해 수를 이어붙인 값의 길이를 쟀다. |  |
| **2022.01.16일(일)** |    [1,2,3더하기](https://www.acmicpc.net/problem/9095)    | 현재 수가 n이라고 할 때 n을 만드는 방법의 수가 R(n)이면 R(n) = R(n-1) + R(n-2) + R(n-3)으로 식을 만들 수 있다.<br/>R(n-1)의 방법들 뒤에 + 1을 붙인다면 n을 만드는 방법이 된다. 그렇기때문에 위 식을 세울 수 있다.   |  |


> **기초 - Queue and Graph**


|                      |                                      #문제                                       |                                     #알고리즘 설명                                      |                                        #배운점                                        |
| :------------------: | :-------------------------------------------------------------------------------: | :-------------------------------------------------------------------------: | :------------------------------------------------------------------------------: |
| **2022.06.11일(토)** |    [DFS와 BFS](https://www.acmicpc.net/problem/1260)    | DFS와 BFS | edge = [[]] * (N + 1) 이렇게 해준다면 얕은 복사가 되어 N+1개의 1차원 배열이 모두 같은 값을 가지게 된다. 그래서 빈 배열에 for문과 append()함수를 이용해 빈 1차원 배열을 넣어주었다. 이를 코드 1줄로 간단히 할 수 있었는데, edge = [[] for _ in range(N+1)] 이렇게 해주면 됐다.  |
| **2022.06.11일(토)** |    [ABCDE](https://www.acmicpc.net/problem/13023)    | DFS | 1) 처음 풀었을 때 seen을 DFS함수의 매개변수로 넣었는데, 재귀를 사용하면서 전역변수인 seen의 배열의 값이 c++처럼 함수 내에서만 바뀌는게 아니라 전체적으로 바뀌어 문제가 됐었다.<br /> 2)깊은 복사 : arr = [[False]*n for _ in range(n)]  <br />   얕은 복사 : [[False] * n] * n <br />ex) {a = [[1]*3]*2} == {a = [[1,1,1],[1,1,1]]}<br />  -> {if: a[0][0] = 3} => {a = [[3,1,1],[3,1,1]]} <br />3) sys.exit()를 사용했으나 오류가 났는데, 이는 VSCode에서 언어 인식에서 오류가 난 것이었음. 언어를 바꿔주니 해결.  |
| **2022.06.11일(토)** |    [미로탐색](https://www.acmicpc.net/problem/2178)    | BFS | ***1) And와 &*** <br /> ***And*** : lazy evaluation.<br/> -> if the first statement is False, it does not check the second statement. and returns False immediately <br/> ***&*** : bitwise<br/> [참고](https://www.geeksforgeeks.org/difference-between-and-and-in-python/)<br/> 2)sys.stdin.readline() & input()<br/> input() : 입력이 주어질 때 "10101"이 주어진다면 저 값만 받아옴 <br/> sys.stdin.readline() : 그 줄을 읽어오는 것이기 때문에 줄바꿈값까지 받아오게 됨. list로 만든 후 int함수를 적용하면 '/n'에는 int함수를 적용할 수 없기때문에 에러가 난다. |
| **2022.06.11일(토)** |    [토마토](https://www.acmicpc.net/problem/7576)    | BFS | |

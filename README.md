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
| **2022.01.11일(화)** |    [리모컨](https://www.acmicpc.net/problem/1107)    | 고장난 버튼이 없으면 100에서 +-로 움직인것과 버튼 누른것의 최솟값<br/>버튼이 모두 고장났으면 100을 빼준 값이 정답<br/>9999999이하의 숫자중 고장난 버튼을 제외한 나머지 버튼으로 만들 수 있는 수의 경우를 다 만들어본다.<br/>min( abs(N-100)[시작점에서 N까지 +-버튼을 누른 횟수], len(수)[수를 만들기위해 버튼을 누른 횟수] + abs(수 - N)[+-버튼 누른 횟수])이 정답이된다.<br/>0버튼을 눌러 0에서부터 횟수를 셀 수 있는데, 일의자리만 이 방법을 사용해서 틀렸었다. 조건문을 잘 보고 써야할 것 같다.  |  for문, if문 한줄에 쓸 수 있어 코드가 간결해진다.<br/>global변수를 사용할 때 유의해야한다.  |



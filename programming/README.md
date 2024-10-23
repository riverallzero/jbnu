- A03 
  - 원의 면적구하기(반지름 입력받아 면적 출력): 03-1.py
  - 칼로리 구하기(과일마다 섭취 g를 받아 칼로리 출력): 03-2.py
  - 두 지점 사이 거리 구하기(x1, y1, x2, y2 입력받아 거리 출력): 03-3.py

- A04
  - x, y를 입력받아 사사분면 출력하기: 04-1.py
  - 03-2.py에서 칼로리 계산 프로그램을 딕셔너리로 이용: 04-2.py
  - 03-1.py에서 반지름을 입력받아 원의 둘레와 면적 구하기: 04-3.py

- A05
  - 숫자를 입력받아, 구구단을 출력하는 gugudan(dan)함수 제작: 05-1.py
  - 섭씨를 화씨로 바꾸는 c2f(t_c)함수 제작: 05-2.py
  - 숫자 n이 주어졌을 때, 1부터 n까지의 합을 구하는 sum_n(n)함수 제작: 05-3.py

- A06
  - 숫자 리스트를 받아 평균을 구하는 average(nums)함수 제작: H0601.py
  - 1~n까지 리스트를 돌려주는 range_list(n)함수 제작: H0602.py
  - 연도(y)를 주면, 윤년인지(True) 아닌지(False)알려주는 is_leap_year(y)함수 제작: H0603.py
    - 조건: 4로 나누었을때 나누어 떨어지면 윤년, 4로 나누어떨어지더라도 100으로 나누어 떨어진다면 윤년아님<br>

- A07
  - text2list(input_text), average(nums), median(nums)함수를 이용하여 아래 코드 실행되도록 제작: H07.py
    ```python
    def main():
      input_text = "5 10 3 4 7"
      nums = text2list(input_text)
      print("주어진 리스트는", nums)
      print("평균값은 {:.1f}".format(average(nums)))
      print("중앙값은 {}".format(median(nums))) # 단, 갯수가 짝수일 경우 중앙에 위치한 두 값 중 큰 값 이용
    ```

- A08
  - 숫자가 여러줄에 걸쳐서 저장되있는 경우 각 숫자를 읽어와 아래 조건 출력: H08.py
      - 총 숫자의 개수
      - 주어진 숫자의 평균
      - 주어진 숫자의 최댓값
      - 주어진 숫자의 

- A09
  - 수업시간에 다룬 코드를 완성하고, 추가로 아래 질문에 답 출력: H09.py
      - 총 강수량: sum(rainfall) -> 함수 따로 만들지 않고 메인에서 값 확인
      - 강우일수: count_rain_days(rainfall)
      - 여름철(6~8월) 총 강수량: sumifs(rainfall, months, selected=[6, 7, 8])
      - 최장연속강우일수: longest_rain_days(rainfall)
      - 강우이벤트 중 최대 강수량: maximum_rainfall_event(rainfall)
      - 일교차가 가장 큰 날짜와 해당일자의 일교차(최고기온과 최저기온의 차이): maximum_temp_gap(dates, tmax, tmin) -> [2021, 1, 20], 23.2
      - 5월부터 9월까지의 적산온도(5도 이상의 온도 합): gdd(dates, tavg) -> 2050.5

- A10
  - 코드를 이용해 2020년 전주 측후소 주소를 다운받아 저장: H10.py
      - "https://api.taegon.kr/stations/146/?sy=2020&ey=2020&format=csv"
      - 파일이 있는 경우 기존에 받은 파일을 이용
      - 결과는 화면에 출력하지 않고 파일에 저장

- A11
  - 관측이래 전주에서 가장 더웠던 날의 최고기온과 날짜, 가장 추웠을 때 최저기온과 날짜 구하기: H11.py
      - "https://data.kma.go.kr/stcs/grnd/grndTaList.do?pgmNo=70"
      - 결과는 LMS참고 서버로 전송(hw11_submission.submit("홍길동", "2021-08-15", 40.1, "1978-01-04", -32.5))

- A12
  - 숫자를 입력받아 리스트 출력: H12.py
      - 숫자는 정수만 입력받고 자연수가 아닌 값은 무시
      - "-1"을 입력하면 입력을 더 이상 받지않고 현재까지 입력받은 값 출력

- A13
  - 구구단 문제를 제출하고, 정답 개수를 출력해 점수 출력: gugudan.py
      - random.randint(start, end)
  - 숨겨진 단어를 맞추는 행맨게임: hangman.py
      - random.choice(list)
  - 로또번호 추출기: lotto.py
      - 1~45숫자 중 중복되지않게 6개 추출

- A14(mid-term)
  - 2022년 3월 기준 연령별 남녀 인구분포표 그리기: H14_population.py
      - Option1: 전북 전체, 전북 내 전체 시군구에 대한 그래프 저장
      - Option2: 지역을 사용자가 입력하면, 해당 지역의 그래프를 화면에 표시
  - 특정 날짜를 입력하면, 40년간 평균기온(1982-2021)의 그래프를 그리고, 해당 일자가 40년 기간 중 몇 번째 높은 기온인지 출력: H14_weather.py
      - 2020년 5월 15일 선택시, 5월 15일 평균기온 그리기
      - 몇번째 높은 온도인지 표시하고, 그래프상에는 수평선을 그려서 강조하기

- A15
  - 도형 클래스 완성하기: H15_shape.py</a><br>
      - class Rectangle(Shape)
      - class Triangle(Shape)
      - class Circle(Shape)
      - class RegularHexagon(Shape)
      - 도전과제: 도형 클래스에 draw메소드를 추가하고 구현
  - 연령별 인구그래프를 클래스 형태로 변환: H15_population.py

- A16
  - ASCII코드를 이용해 입력받은 문자열 변환: H1601.py
      - 대문자는 소문자로, 소문자는 대문자로
      - toggle_text(text:str) -> str
  - ASCII코드를 이용해 카이사르 암호 구현: H1602.py
      - caesar_encode(text:str, shift:int =3) -> str
      - caesar_decode(text: str, shift:int =3) -> str
  - 유니코드를 이용한 초성게임 완성: H1603.py
      - 주어진 단어 뭉치에서 단어를 하나 선택하고 초성 제시
      - 사용자는 주어진 초성을 보고 주어진 단어를 맞추는 게임

- A17
  - GUI프로그램을 활용하여 카이사르 암호를 GUI로 구현: H1701.py</a><br>
  - 초성게임의 input()대신 gui_input()활용하여 구현: H1702.py</a><br>

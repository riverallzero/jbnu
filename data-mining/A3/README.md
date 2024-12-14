수업시간에 배운 Content-based recommendation, Collaborative filtering, Latent factor model 등을 구현하여 test data에 일정 성능 이상(private data에 대해 RMSE 1.0이하) 달성하는 것이 목표입니다.

1. Kaggle 에 가입 (이미 가입한 사람은 skip)
2. https://www.kaggle.com/t/bfe1d62966fe45558bb2f6b05a625538 에 접속하여, competition 참여
3. Team 명을 학번으로 변경 (필수)
4. train.csv 파일로 입력으로 추천 모델 구현 및 test.csv를 입력받아 rating 예측
5. 예측한 파일을 업로드 (제출 양식은 submission.csv 참고)

---

- 제출기한: 12월 4일 11:59 PM
- 주의사항: 추천과 관련된 3rd party 라이브러리는 사용할 수 없음.
  - 예를 들어, automatic differentiation (gradient descent)를 위해 pytorch를 사용할 수 있으나, pytorch/torchrec 같은 라이브리러는 사용할 수 없음.
- 제출파일:
  - 작성 코드 (작성한 코드는 다음과 같이 실행되어야 함)
    - 파이썬으로 작성한 경우,
        python 202312123_DM_hw3.py --train train.csv --test test.csv을 수행하면, 구현한 추천 시스템 모델과 함께 submission.csv 파일이 생성되어야 함
    - 파이썬 언어도 위와 같이 train.csv와 test.csv 파일을 매개변수들로 받아서 동작할 수 있도록 하여야 함.
    - 보고서에 자세히 기술해야하며, 설명만 보고 수행이 불가능한 경우, 점수가 없음
  - 결과 보고서 (추천 설명 및 성능을 달성하기 위한 문서, 최소 5페이지 이상 작성, GPT로 100% 작성한 경우 cheating으로 간주)
    - 코드 실행 방법!! (반드시 추가)
    - 실험 결과를 위해 일부 코드를 보고서에 추가하여 설명할 수 있지만, 전체 코드를 보고서에 추가하지 말것
    - 다양한 실험 결과들을 추가하기 바람. 예를 들어, content-based filtering을 어떻게 수행하니, public 스코어에서 어떤 점수가 나왔으며, latent-factor model에서 factor를 변화하면서 public 스코어에 대한 성능을 보여준다던지, global effect를 추가한 것과 추가하지 않은 것에 대한 성능 등을 기술하여야 함
- 파일형식: 학번_DM_hw3.zip 
  - 작성 코드와 결과 보고서를 하나의 파일로 압축하여 제출 
  - 학번이 202112123인 학생은 반드시 제출파일 이름이 202112123_DM_hw3.zip 이어야 함
  - 파일형식이 달라 점수를 못받는 것은 제출한 본인의 책임임

import csv
from collections import Counter
from itertools import combinations
import time

class APriori():
    def __init__(self, filename, s, c, i) -> None:
        self.pass_ctr_list = []
        self.filename = filename
        self.s = s
        self.c = c
        self.i = i
        self.total_length = 0
        """
        pass_ctr_list: list
            각 PASS에서 아이템을 카운팅한 결과, dict(pair, count)
        filename: str
            데이터 파일 경로
        s: int
            support threshold
        c: float
            confidence threshold
        i: float
            interest threshold
        total_length: int
            데이터의 총 바구니 개수
        """

    def makeComb(self, item_list, length):
        """
        n개 원소의 조합 리스트를 인자로 받아 n+1개 원소의 조합을 생성

        item_list: list
            이전 단계에서 생성된 항목의 리스트
        length: int
            생성할 조합의 길이 ex.PASS1 --> 2원소 조합 생성, PASS2 --> 3원소 조합 생성
        input_length: int
            item_list에서 각 아이템이 이루는 튜플의 길이
        all_items: set
            item_list에 포함된 모든 고유 항목들의 집합
        valid_combs: list
            생성된 조합 중 유효한 조합
        """
        # 길이가 2보다 작거나 item_list가 비어있다면 빈 리스트 반환
        if length < 2 or not item_list:
            return []

        # 입력이 개별 항목의 리스트인 경우 2원소 조합 생성
        elif length == 2:
            return list(combinations(item_list, length))

        # 입력이 튜플의 리스트인 경우
        input_length = len(item_list[0])
        if input_length != length - 1:
            return [] 

        # 입력 튜플을 정렬하여 집합으로 만들어 빠른 조회를 가능하게 함
        input_set = set(tuple(sorted(item)) for item in item_list)

        # 모든 고유 항목을 정렬하여 가져옴
        all_items = sorted(set(item for tup in item_list for item in tup))

        # 유효한 조합인지 확인하는 함수
        def is_valid(comb):
            # comb의 모든 (length-1)-부분집합이 입력 집합에 있는지 확인
            for subset in combinations(comb, length - 1):
                if tuple(sorted(subset)) not in input_set:
                    return False
            return True

        # 모든 조합을 확인하고 유효한 조합만 반환
        valid_combs = []
        for comb in combinations(all_items, length):
            if is_valid(comb):
                valid_combs.append(comb)

        return valid_combs

    def cPhase(self, comb_list, phase):
        """
        이전 PASS에서 생성된 조합 별 빈도 계산

        comb_list: list
            빈도를 계산할 조합 리스트
        phase: bool
            0: 단일 항목 빈도 계산 
            1: 두 개 이상의 항목 조합 빈도 계산
        cntr: dict
            생성된 조합 리스트를 key로, 각 조합별 빈도수를 value로 가짐
        """
        with open(self.filename, newline='') as csvfile:
            csv_reader = list(csv.reader(csvfile))

            cntr = Counter()

            # 단일 아이템의 빈도를 계산하는 경우 각 row의 항목들을 카운터에 추가
            if phase == 0:
                for row in csv_reader:
                    cntr.update(row)
                    self.total_length += 1
                return cntr
            
            # 2개 이상의 조합 빈도를 계산하는 경우: comb_list의 각 조합에 대한 빈도 수를 저장할 리스트 초기화
            comb_cntr = [0 for _ in range(len(comb_list))]

            for row in csv_reader:
                # comb_list의 각 조합을 row와 비교
                for cp in range(len(comb_list)):
                    # comb_list의 각 조합이 row의 부분집합인지 확인
                    if set(comb_list[cp]).issubset(set(row)):
                        comb_cntr[cp] += 1
            
            # 조합과 조합의 빈도수를 반환
            cntr = dict(zip(comb_list, comb_cntr))
            
            return cntr
        
    def lPhase(self, c_results, s):
        """
        cPhase에서 빈도수가 s번 이상 나타난 조합을 탐색

        l_list: list
            C단계에서 만들어진 조합 중 s회 이상 나타나는 조합을 포함
        """
        l_list = []

        # s회 이상 나타나는 조합을 반환
        for key, value in c_results.items():
            if value >= s:
                l_list.append((key))

        return l_list

    def clPass(self):
        """
        조합이 만들어지는 최대 PASS와 그 조합을 탐색

        pass_ctr: int
            완료된 PASS 단계 카운트
        li_comb: list
            L 단계를 거친 후 아이템으로 생성한 조합
        """
        pass_ctr = 0
        li_comb = None

        while True:
            # C_i 단계: 조합 생성 및 빈도수 체크
            # PASS1에서는 개별 아이템을 세므로 li_comb를 None으로 초기화 후 실행
            c_i = self.cPhase(li_comb, pass_ctr)
            if li_comb is None:
                self.pass_ctr_list.append(c_i)
            else:
                self.pass_ctr_list.append({tuple(sorted(k)): v for k, v in c_i.items()})
            
            # L_i 단계: s회 이상 나타나는 조합만 남겨둠
            l_i = self.lPhase(c_i, self.s)

            # 다음 PASS를 위해 조합 생성
            li_comb = self.makeComb(l_i, pass_ctr + 2)  

            # 결과 출력
            # print(f'PASS {pass_ctr + 1}: {li_comb}')
            print(f'=> PASS {pass_ctr + 1} Done !')
            
            # 만약 li_comb 빈 리스트라면 반복 종료
            if not li_comb:  
                return l_i
            
            pass_ctr += 1  # 패스 카운터 증가

    @staticmethod
    def makeRule(items):
        """
        clPass에서 찾은 최대 원소의 조합을 가지고 세부 조합 규칙을 생성

        results: list
            1부터 아이템의 개수까지의 각 조합
        combo: tuple
            먼저 선택된 조합
        remaining_items: tuple
            아이템 중 combo를 제외한 나머지 조합
        """
        results = []
        
        # 조합의 크기를 1부터 아이템의 개수까지 설정하여 각 조합을 생성하고 선택된 조합을 제외한 나머지 아이템을 리스트에서 찾음
        for r in range(1, len(items)):  
            for combo in combinations(items, r):
                remaining_items = [item for item in items if item not in combo]
                results.append((combo, remaining_items))
        
        return results

    def calConfidence(self, pass_set, rules):
        """
        makeRule에서 찾은 규칙들의 confidnece 계산하고, confident한 규칙만 남겨두며 interesting한지 계산 후 조합과 confidence, interest를 출력

        I: tuple
            생성된 규칙에서 왼쪽에 있는 조합
        j: tuple
            생성된 규칙에서 오른쪽에 있는 조합
        sorted_pass_set: tuple
            PASS에서 생성된 결과를 정렬
        sup_I_J: int
            전체 바구니에서 I∪j가 나타난 개수
        sup_I: int
            전체 바구니에서 I가 나타난 개수
        confidence: float
            confidence(I→j)=Support(I∪j)/Support(I)
        P_j: float
            전체 바구니에서 j가 나타난 개수/전체 바구니 개수
        interest: float
            |confidence - P_j|
        """
        for rule in rules:
            I = rule[0]
            j = rule[1]

            sorted_pass_set = tuple(sorted(pass_set))

            sup_I_j = self.pass_ctr_list[len(sorted_pass_set)-1][sorted_pass_set]

            # PASS1인 경우 개별 아이템이므로 key값을 이용해 바로 value 얻음
            # 그 외의 경우 순서에 상관받지 않도록 key값을 정렬해 얻음
            if len(I) == 1:
                sup_I = self.pass_ctr_list[0][I[0]]
            else:
                sorted_I = tuple(sorted(I))
                sup_I = next((i[sorted_I] for i in self.pass_ctr_list if sorted_I in i), 0)

            if len(j) == 1:
                sup_j = self.pass_ctr_list[0][j[0]]
            else:
                sorted_j = tuple(sorted(j))
                sup_j = next((j[sorted_j] for j in self.pass_ctr_list if sorted_j in j), 0)

            confidence = sup_I_j / sup_I

            # confident한 경우 interesting한지 추가적으로 검사 후 도출된 연관 규칙과 관련 점수 출력
            if confidence >= self.c:            
                P_j = sup_j / self.total_length
                interest = abs(confidence - P_j)

                if interest >= self.i:
                    is_interest = '** interesting **'
                else:
                    is_interest = '** not interesting **'

                print(f' o {set(I)} --> {set(j)}: {is_interest} :confidence({confidence:.2f}) interest({interest:.2f})')

    def run(self):
        pass_results = self.clPass()

        print('\n| Association Rules')
        for pass_result in pass_results:
            pass_rules = self.makeRule(pass_result)
            self.calConfidence(pass_result, pass_rules)

if __name__ == '__main__':
    apriori = APriori('market.csv', s=15, c=0.5, i=0.5)

    start_time = time.time()
    apriori.run()
    end_time = time.time()

    print(f'mining time: {end_time-start_time}s')

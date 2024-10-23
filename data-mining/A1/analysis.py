import re

data = """
 o {'chocolate', 'frozen vegetables', 'ground beef', 'milk'} --> {'mineral water'}: ** interesting ** :confidence(0.75) interest(0.51)
 o {'chocolate', 'mineral water', 'frozen vegetables', 'ground beef'} --> {'milk'}: ** not interesting ** :confidence(0.60) interest(0.47)
 o {'chocolate', 'frozen vegetables', 'mineral water', 'milk'} --> {'ground beef'}: ** not interesting ** :confidence(0.50) interest(0.40)
 o {'chocolate', 'mineral water', 'ground beef', 'milk'} --> {'frozen vegetables'}: ** interesting ** :confidence(0.60) interest(0.50)
 o {'milk', 'mineral water', 'frozen vegetables', 'ground beef'} --> {'chocolate'}: ** not interesting ** :confidence(0.54) interest(0.37)
 o {'chocolate', 'frozen vegetables', 'mineral water', 'milk'} --> {'spaghetti'}: ** not interesting ** :confidence(0.50) interest(0.33)
 o {'chocolate', 'frozen vegetables', 'spaghetti', 'milk'} --> {'mineral water'}: ** not interesting ** :confidence(0.58) interest(0.34)
 """

total_rules = 0
left_set_count = {} # I의 아이템 개수별 빈도수
right_set_count = {} # j의 아이템 개수별 빈도수
interesting_count = 0
not_interesting_count = 0

for line in data.strip().split('\n'):
    total_rules += 1

    # 집합 추출
    match = re.search(r'({.*?})\s*-->\s*({.*?})', line)
    if match:
        left_side = match.group(1)
        right_side = match.group(2)

        left_size = len(eval(left_side)) # I의 아이템 개수
        right_size = len(eval(right_side)) # j의 아이템 개수

        left_set_count[left_size] = left_set_count.get(left_size, 0) + 1 
        right_set_count[right_size] = right_set_count.get(right_size, 0) + 1 

    if '** interesting **' in line:
        interesting_count += 1
    else:
        not_interesting_count += 1

print(f'생성된 규칙의 총 개수: {total_rules}')
for key in left_set_count.keys():
    value = left_set_count[key]
    print(f'  o I의 {key}가지 아이템의 비율: {value/total_rules*100:.2f}')
for key in right_set_count.keys():
    value = right_set_count[key]
    print(f'  o j의 {key}가지 아이템의 비율: {value/total_rules*100:.2f}')
print(f'  o interesting한 아이템의 비율: {interesting_count/total_rules*100:.2f}')
print(f'  o not interesting한 아이템의 비율: {not_interesting_count/total_rules*100:.2f}')

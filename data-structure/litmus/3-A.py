'''
문제) 사용자가 입력한 정수의 평균을 계산하는 프로그램을 작성하자. 
- 사용자가 0을 입력하기 전까지 정수를 계속해서 입력받는다. 
- 결과는 전체 입력받은 숫자의 평균을 계산하여 출력한다.
 
<INPUT>
2
5
0 
 
<OUTPUT>
3.5
'''



class Mean():
    def get_input_and_calculate(nums):
        return (sum(nums) / len(nums))
    

def main():
    nums = []
    
    while True:
        num = int(input())

        if num == 0:
            break
        
        nums.append(num)

    nums_mean = Mean.get_input_and_calculate(nums)
    print(nums_mean)


if __name__ == '__main__':
    main()

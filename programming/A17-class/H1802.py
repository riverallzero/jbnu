import random
import tkinter as tk
from tkinter import simpledialog


class ChosungGame:
    CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
    def __init__(self, word_list = None):
        if word_list is None:
            self.wordlist = ['포도', '사과', '바나나', '키위', '딸기', '오렌지', '자몽', '레몬', '체리', '복숭아', '수박', '블루베리']
        else:
            self.wordlist = word_list.copy()

        self.window = tk.Tk()
        self.window.withdraw()


    def gui_input(self, text: str) -> str:
        return simpledialog.askstring(title="답안 입력", prompt=text)


    def chosung_game(self):

        choicelist = random.choice(self.wordlist)
        secret = choicelist
        answer = ['_' for i in range(len(secret))]
        trial = 5

        choseonglist = []
        for word in choicelist:
            if '가' <= word <= '힣':
                choseong = (ord(word) - ord('가')) // (21 * 28)
                choseonglist.append(self.CHOSUNG_LIST[choseong])

        while trial > 0:
            print('시도 {}) 과일 {} : ' .format(6-trial, choseonglist)+''.join(answer))
            letter = self.gui_input('답안 입력 = ')

            if letter in secret:
                for i in range(len(secret)):
                    if letter == secret[i]:
                        answer[i] = letter
                        trial -= 1
            else:
                trial -= 1

            if '_' not in answer:
                break

        if trial > 0:
            print('{}, 정답!'.format(secret))

        else:
            print('오답! 정답은 {} 입니다.' .format(secret))

def main():
    game = ChosungGame()
    game.chosung_game()
if __name__ == '__main__':
    main()

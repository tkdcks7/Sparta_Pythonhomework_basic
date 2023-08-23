import random

def main():
    win_record = [0,0,0,0]
    while True:
        switch_char = input(f"현재 전적: {win_record[0]}판 중 {win_record[1]}승 {win_record[2]}무 {win_record[3]}패. 가위바위보 게임을 시작하시겠습니까? Y/N : ")
        if (switch_char == 'Y' or switch_char == 'y'):
            win_record = rsp_game(win_record)
        elif (switch_char == 'N' or switch_char == 'n'):
            print("가위바위보 게임을 종료합니다.")
            break
        else:
            print("잘못 입력하셨습니다. Y/N 중 하나만 입력해 주세요.")
            continue


def rsp_game(win_record):
    rspd = {'S':1, 'R':2, 'P':3}
    random_rsp = random.randint(1, 3)
    print("가위바위보 게임을 시작하겠습니다.")
    while True:
        rsp = input(f"[Round {win_record[0]+1}] S/R/P 중 하나를 입력하세요(소문자도 가능): ").upper()

        if rsp.upper() not in ['S','R','P']:
            print("제대로 입력해 주세요. 가위/바위/보 만 입력할 수 있습니다.")
            continue
        jcount = random_rsp-rspd[rsp]
        if (jcount == 0):
            print("Draw! 무승부입니다.")
            win_record[0] = win_record[0]+1
            win_record[2] = win_record[2]+1
            return win_record
            break
        elif (jcount == -1 or jcount == 2):
            print("Win! 이겼습니다!")
            win_record[0] = win_record[0]+1
            win_record[1] = win_record[1]+1
            return win_record
            break
        elif (jcount == -2 or jcount == 1):
            print("Lose... 졌습니다...")
            win_record[0] = win_record[0]+1
            win_record[3] = win_record[3]+1
            return win_record
            break

main()
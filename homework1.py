import random
def main():
    record = 101
    cnt = 1
    while True:
        switch_char = input("숫자 맞추기 게임을 시작하시겠습니까? Y/N : ")
        if (switch_char == 'Y'):
            cnt = number_game(cnt)
            if (cnt < record):
                record = cnt
        elif (switch_char == 'N'):
            if (record == 101):
                print(f"게임을 해보시지 않으시다니, 아쉽군요. 숫자 맞추기 게임을 종료합니다.")
            else:
                print(f"최저 시도 횟수는 {record}회 입니다. 숫자 맞추기 게임을 종료합니다.")
                with open(__file__, 'r',encoding='UTF-8') as f:
                    lines = f.read().split('\n')
                    new_line = f'    record = {record}'
                    new_file = '\n'.join(lines[0:2] + [new_line] + lines[3:])
                with open(__file__, 'w',encoding='UTF-8') as f:
                    f.write(new_file)
            break
        else:
            print("잘못 입력하셨습니다. Y/N 중 하나만 입력해 주세요.")
            continue


def number_game(cnt):
    cnt = 1
    random_number = random.randint(1, 100)
    valid_range = range(1,101)
    number_max = 100
    number_min = 1
    number = 0
    print("숫자 맞추기 게임을 시작하겠습니다!")
    while True:
        number = input(f"[Round {cnt}] 1~100 사이의 정수를 입력하세요: ")
        if number not in list(map(str, valid_range)):   
            try:
                if (int(float(number)) != float(number)):
                    print("정수값이 아닙니다! 정수를 입력하세요.")
                    continue
                elif ((int(number) < 1) or (100 < int(number))):
                    print("범위를 벗어난 수입니다. 1~100 사이의 정수를 입력하세요.")
                    continue
            except ValueError:
                print("이상한 값 입력하지 마시고, 1~100 사이의 정수를 입력하세요.")
                continue
        elif ((int(number) >= number_max) or (int(number) <= number_min)):
            print(f"그 값은 당연히 아니죠... {number_min}~{number_max} 사이의 정수를 입력하세요. 봐드립니다.")
            continue
        elif (int(number) == random_number):
            print(f"정답입니다! {cnt}번만에 정답을 맞추셨습니다!")
            return cnt
            break
        elif (int(number) > random_number):
            print("Down! 더 작은 수를 입력하셔야 합니다.")
            cnt += 1
            number_max = int(number)
        elif (int(number) < random_number):
            print("Up! 더 큰 수를 입력하셔야 합니다.")
            cnt += 1
            number_min = int(number)

main()
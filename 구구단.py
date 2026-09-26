"""구구단 출력 프로그램"""


def 구구단_출력(단):
    """입력받은 단의 구구단을 출력한다"""
    for 곱수 in range(1, 10):
        print(f"{단} x {곱수} = {단 * 곱수}")


def 전체_구구단_출력():
    """2단부터 9단까지 전체 구구단을 출력한다"""
    for 단 in range(2, 10):
        구구단_출력(단)
        print()


def 메인():
    while True:
        입력값 = input("출력할 단을 입력하세요 (2~9, 전체는 0, 종료는 q): ").strip()

        if 입력값.lower() == "q":
            print("프로그램을 종료합니다.")
            break

        if 입력값 == "0":
            전체_구구단_출력()
            continue

        if not 입력값.isdigit() or not (2 <= int(입력값) <= 9):
            print("2에서 9 사이의 숫자, 0(전체), q(종료) 중 하나를 입력하세요.")
            continue

        구구단_출력(int(입력값))
        print()


if __name__ == "__main__":
    메인()

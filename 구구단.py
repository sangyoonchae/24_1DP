def 구구단_출력(단):
    # 2단부터 9단까지 중 하나의 단을 출력한다
    for 곱하는수 in range(1, 10):
        print(f"{단} x {곱하는수} = {단 * 곱하는수}")


if __name__ == "__main__":
    for 단 in range(2, 10):
        구구단_출력(단)
        print()

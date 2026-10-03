def collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps


def demo():
    n = int(input("Pick a starting number: "))
    print(f"{n} takes {collatz_steps(n)} steps to reach 1.")

def countdown(start):
    text = ""
    for n in range(start, 0, -1):
        text += str(n) + "... "
    return text + "LIFTOFF! 🚀"


def demo():
    import time
    start = int(input("Count down from what? "))
    line = countdown(start)
    for chunk in line.split(" "):
        print(chunk, end=" ", flush=True)
        time.sleep(0.4)
    print()

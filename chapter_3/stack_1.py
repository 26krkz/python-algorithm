MAX = 5
stack = [0] * MAX
sp = 0


def push(d):
    global sp
    if sp < MAX:
        stack[sp] = d
        sp += 1
        print(f"push {d}")
    else:
        print("can not push this data")


def pop():
    global sp
    if sp > 0:
        sp -= 1
        return stack[sp]
    else:
        print("not exist popping data")
        return None


for i in range(6):
    push(i)

for i in range(6):
    d = pop()
    print(f"popping data is {d}")

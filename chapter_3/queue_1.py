MAX = 6
que = [0] * MAX
head = 0
tail = 0


def enqueue(d):
    global tail
    nt = (tail + 1) % MAX

    if nt == head:
        print("can not enqueue more data")
    else:
        que[tail] = d
        tail = nt
        print(f"done enqueue data {d}")


def dequeue():
    global head
    if head == tail:
        print("not exist dequeuing data")
        return None
    else:
        d = que[head]
        head = (head + 1) % MAX
        return d


for i in range(6):
    enqueue(i)

for i in range(6):
    d = dequeue()
    print(f"dequeued data, {d}")

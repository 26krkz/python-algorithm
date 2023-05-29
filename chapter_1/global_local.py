total = 0


def test_func():
    global total
    loops = 20
    for i in range(loops):
        total += 10


print(f"totalの初期値{total}")
test_func()
print(f"関数実行後のtotalの値{total}")

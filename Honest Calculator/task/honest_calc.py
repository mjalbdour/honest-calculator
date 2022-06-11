# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
msg_ = [msg_0,
        msg_1,
        msg_2,
        msg_3,
        msg_4,
        msg_5,
        msg_6,
        msg_7,
        msg_8,
        msg_9,
        msg_10,
        msg_11,
        msg_12]
memory = 0.0


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


def is_one_digit(v):
    return -10 < v < 10 and v.is_integer()


continue_calc = "y"
while continue_calc == "y":
    print(msg_0)
    calc = input()
    x, op, y = calc.split()
    result = 0.0

    if x == "M":
        x = memory
    if y == "M":
        y = memory

    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_1)
    else:
        if op in {"+", "-", "*", "/"}:
            check(x, y, op)
            if op == "+":
                result = x + y
            elif op == "-":
                result = x - y
            elif op == "*":
                result = x * y
            elif op == "/":
                if y == 0:
                    print(msg_3)
                    continue
                else:
                    result = x / y
        else:
            print(msg_2)
            continue

        print(result)

        while True:
            print(msg_4)
            to_store = input()
            if to_store == "y":
                if is_one_digit(result):
                    msg_index = 10
                    while True:
                        print(msg_[msg_index])
                        answer = input()
                        if answer == "y":
                            if msg_index < 12:
                                msg_index = msg_index + 1
                            else:
                                memory = result
                                break
                        elif answer == "n":
                            break
                else:
                    memory = result
                break
            elif to_store == "n":
                break

        while True:
            print(msg_5)
            continue_calc = input()
            if continue_calc == "y":
                break
            elif continue_calc == "n":
                continue_calc = "n"
                break

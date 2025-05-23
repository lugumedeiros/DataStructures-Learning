# Not ideal because I just want to create the algoriithm, so I made using power 10
import time

def mult_normal(a, b):
    sum = 0
    less, great = (a,b) if a < b else (b,a)
    for _ in range(less):
        sum += great
    return sum

def mult_rec(a, b):
    if a is None:
        return b
    if b is None:
        return a
    if a < 10 or b < 10:
        return a*b

    a_str = str(a)
    b_str = str(b)

    max_len = max(len(a_str), len(b_str))
    if max_len % 2 != 0:
        max_len += 1

    a_str = a_str.zfill(max_len)
    b_str = b_str.zfill(max_len)

    a1 = int(a_str[:max_len // 2])
    a2 = int(a_str[max_len // 2:])
    b1 = int(b_str[:max_len // 2])
    b2 = int(b_str[max_len // 2:])

    power = len(b_str) if len(b_str) > len(a_str) else len(a_str)
    n = 1
    for _ in range(power//2):
        n = n*10

    calc1= n*n*mult_rec(a1, b1)
    calc2 = n*mult_rec(a1,b2)
    calc3 = n*mult_rec(a2,b1)
    calc4 = mult_rec(a2, b2)
    result = calc1 + calc2 + calc3 + calc4

    return result

def mult_karatsuba(a, b):
    if a is None:
        return b
    if b is None:
        return a
    if a < 10 or b < 10:
        return a*b

    a_str = str(a)
    b_str = str(b)

    max_len = max(len(a_str), len(b_str))
    if max_len % 2 != 0:
        max_len += 1

    a_str = a_str.zfill(max_len)
    b_str = b_str.zfill(max_len)

    a1 = int(a_str[:max_len // 2])
    a2 = int(a_str[max_len // 2:])
    b1 = int(b_str[:max_len // 2])
    b2 = int(b_str[max_len // 2:])
    
    power = len(b_str) if len(b_str) > len(a_str) else len(a_str)
    n = 1
    for _ in range(power//2):
        n = n*10

    calc1= mult_karatsuba(a1, b1) 
    calc2 = mult_karatsuba(a1+a2,b1+b2)
    calc3 = mult_karatsuba(a2, b2)
    result = n*n*(calc1) + n*(calc2 - (calc1 + calc3)) + calc3

    return result

if __name__ == "__main__":
    a = 1234123412341234123412341234
    b = 5678567856785678567856785678

    # e = time.perf_counter()
    # print(mult_normal(a, b))
    # print(f"in {time.perf_counter() - e}")

    e = time.perf_counter()
    print(mult_rec(a, b))
    print(f"in {time.perf_counter() - e}")

    e = time.perf_counter()
    print(mult_karatsuba(a, b))
    print(f"in {time.perf_counter() - e}")

    e = time.perf_counter()
    print(a * b)
    print(f"in {time.perf_counter() - e}")
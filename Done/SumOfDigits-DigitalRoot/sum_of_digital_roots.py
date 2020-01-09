def digital_root(n):
    if n%9 is 0:
        return 0 if n is 0 else 9
    return n%9

print(digital_root(0))
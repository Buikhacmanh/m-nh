n = int(input("Nhập số nguyên cần tính: "))

def Songuyen(n):
    if n == 0:
        return 0
    return n + Songuyen(n - 1)

print(Songuyen(n))
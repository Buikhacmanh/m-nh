print ("Giải phương trình bậc 2: ax ^ 2 + bx + c = 0")
a = float (input ("Nhập a:"))
b = float (input ("Nhập b:"))
c = float (input ("Nhập c:"))

nếu a == 0:
    nếu b == 0:
        nếu c == 0:
            print ("Vô nghiệm phương pháp!")
        khác:
            print ("Phương trình vô nghiệm!")
    khác:
        nếu c == 0:
            print ("Phương trình có 1 nghiệm x = 0")
        khác:
            print ("Phương trình có 1 nghiệm x =", -c / b)
khác:
    delta = b ** 2 - 4 * a * c
    nếu delta <0:
        print ("Phương trình vô nghiệm!")
    elif delta == 0:
        print ("Phương trình có 1 nghiệm x =", -b / (2 * a))
    khác:
        print ("Phương trình có 2 phân biệt nghiệm!")
        print ("x1 =", float ((- b - sqrt (delta)) / (2 * a)))
        print ("x2 =", float ((- b + sqrt (delta)) / (2 * a)))
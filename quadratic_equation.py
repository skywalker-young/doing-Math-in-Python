import math
# def getRoots(a,b,c):
#     D=math.sqrt(b*b-4*a*c)
#     x1=(-b+D)/(2*a)
#     x2=(-b-D)/(2*a)
#
#     return [x1,x2]
#
# print(getRoots(1,2,1))

def is_sqr(x):  # 判断D开方后是否为整数
    num1 = math.sqrt(x)
    return int(num1) == num1
def sqr(x):     # 将开方后的D取整
    num2 = math.sqrt(x)
    return int(num2)

def getRoots(a,b,c):
    D = (b * b - 4 * a * c)
    if D<0:
        print("没有实数解")
    elif D==0:
        print("      ", -b, "\n", "X =-------", "\n", "      ", 2 * a, sep="")  # 强制转化为分数形式
    elif D>0:
        if is_sqr(D): #平方根为整数
            x1=(-b+sqr(D))/(2*a)
            x2=(-b-sqr(D))/(2*a)
            if x1%(2*a)==0 and x2%(2*a)==0: #都为整数根
                print('x1=%d,x2=%d'%(x1,x2))
            elif x1 % (2*a) == 0 and x2 % (2*a) != 0:  # 有一根为整数
                print("X1 = ", x1, "\n", )
                print("      ", -b - math.sqrt(D), "\n", "X2 =-------", "\n", "      ", (2*a), "\n", sep="")
            elif x1 % (2*a) != 0 and x2 % (2*a) == 0:  # 有一根为整数
                print("      ", -b + math.sqrt(D), "\n", "X1 =-------", "\n", "      ", (2*a), "\n", sep="")
                print("X2 = ", x2, "\n", )
            else:  # 两根都为浮点数时
                print("      ", -b + math.sqrt(D), "\n", "X1 =-------", "\n", "      ", (2*a), "\n", sep="")
                print("      ", -b - math.sqrt(D), "\n", "X2 =-------", "\n", "      ", (2*a), "\n", sep="")
        else: # 当D为开不尽平方根时
            print("      ", -b, "+ √", D, "\n", "X1 =-------", "\n", "      ", (2*a), "\n", sep="")
            print("      ", -b, "- √", D, "\n", "X2 =-------", "\n", "      ", (2*a), "\n", sep="")


print(getRoots(1,3,-2))

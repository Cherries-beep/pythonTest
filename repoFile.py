
def print_goods(*args):
    count = 0
    countNeg = 0
    flag = 0
    for i in args:
        if ((type(i)== str)) and (len(i)>0):
           count = count + 1
           print(f"{count}.{i}")
    for i in args:
        if ((type(i) != str)) or (len(i) < 0):
         countNeg = countNeg + 1
        if countNeg == len(args):
            print('Нет товаров')

a = ('watermelon','peach', True, 5)
print_goods(*a)

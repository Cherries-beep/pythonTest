flag = 0

def f(*args):

   for i in args:
       global flag
       if i > 0:
           glag = 1
           print(True)
           break
       elif i<0:
            flag=0
            print(False)
            break

a= (-2,-5,-5,-5,5)
f(*a)
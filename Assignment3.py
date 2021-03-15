# quadratic 
'''
x=(-b(+ or -)(b^2 -4ac)^0.5)/2a
x=-b/2a  + or - D/2a

'''


a= int(input('Enter a :'))
b= int(input('Enter b :'))
c= int(input('Enter c :'))

D =  (b**2 - 4*a*c)**0.5
x1=0
x2=0
if(a!=0 and b!=0 and c!=0):
    x1 = (-b+D)/2*a
    x2 = (-b-D)/2*a
else:
    print('Math Error')
    exit()



print(x1,x2)
# print(typ(x1))

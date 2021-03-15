# Write a program that prompts the user to enter a, b, c, d, e, and f and display the
# result. If ad – bc is 0, report that The equation has no solution.
"""
ax + by = e
cx + dy = f
x =(ed - bf)/(ad - bc)
y =(af - ec)/(ad - bc)

"""
values=[]

x=0
keys=["a","b","c","d","e","f"]
while x<6:
    try:
        number = int(input(f'Enter value for {keys[x]} :'))
        zero=1/number
        values.append(number)
        x+=1

    except:
        print('Input Error')

a=values[0]
b=values[1]
c=values[2]
d=values[3]
e=values[4]
f=values[5]

x =(e*d - b*f)/(a*d - b*c)
y =(a*f - e*c)/(a*d - b*c)

print(x,y)
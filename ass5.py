
list_num=input('Enter Number Btw 0 - 1000 : ')
int_num=int(list_num)
if int_num>0 and int_num <1000:
    lis='Error due to invalid number'
    if len(list_num)==3:
        lis=int(list_num[0])+int(list_num[1])+int(list_num[2])
    if len(list_num)==2:
        lis=int(list_num[0])+int(list_num[1])
    if len(list_num)==1:
        lis=int(list_num[0])            
    print(lis)
else:
    print('Number must be btw 0 - 1000 \n(note : 1000 is not included)')
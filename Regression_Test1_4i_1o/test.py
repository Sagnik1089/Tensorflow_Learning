pred_inp=input("Enter 4 number separated with , : " )
values=pred_inp.split(',')
for ind, i in values:
    values[ind]=int(i)
print(values)
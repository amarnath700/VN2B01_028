#  how to create table of any number  we created 12
table_12=[]
for i in range(1, 121):
    if i % 12 == 0:
        table_12.append(i)
print(table_12)

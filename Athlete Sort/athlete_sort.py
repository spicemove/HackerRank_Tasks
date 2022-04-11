no_of_rows_and_columns = input()

N = int(no_of_rows_and_columns.split()[0])
M = int(no_of_rows_and_columns.split()[1])

lst = []
row = []

for i in range(N):
    nums = input()

    row = []

    for i in nums.split():
        row.append(int(i))
        
    lst.append(row)
    
K = int(input())

selected_attribute_lst = []

for i in lst:
    selected_attribute_lst.append(i[K])
    
selected_attribute_lst.sort()

remove_duplicate = []

for i in selected_attribute_lst:
    if i not in remove_duplicate:
        remove_duplicate.append(i)
        
sorted_lst = []

for i in remove_duplicate:
    for j in lst:
        if i == j[K]:
            sorted_lst.append(j)
            
sorted_lst_str = []

for i in sorted_lst:
    x = ''
    for j in range(len(i)):
        x = x + " " + str(i[j])

    print(x.strip())
        

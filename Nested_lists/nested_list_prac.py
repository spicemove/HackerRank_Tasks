lst = []

no_of_students = int(input())

for i in range(no_of_students):
    lst.append([input(),float(input())])

list_var = lst

lst_marks = []

for item in lst:
    lst_marks.append(item[1])

lst_marks_sorted = []

for item in lst_marks:
    lst_marks_sorted.append(item)

lst_marks_sorted.sort()

min_lst_marks_sorted = lst_marks_sorted[0]

second_lowest_value = 0

index = 1

while (index <= len(lst_marks_sorted)-1):
    if (lst_marks_sorted[index] == min_lst_marks_sorted):
        index = index + 1
        continue
    else:
        second_lowest_value = lst_marks_sorted[index]
        break


lst_name = []

for i in range(len(lst_marks)):
    if second_lowest_value == lst_marks[i]:
        lst_name.append(list_var[i][0])


lst_name.sort()

for i in lst_name:
    print(i)
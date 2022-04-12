input_values = input()
polinomical_exp =input()

lst = []
lst = input_values.split()

x = int(lst[0])
k = int(lst[1])

p = eval(polinomical_exp)

if p == k:
    print(True)
else:
    print(False)

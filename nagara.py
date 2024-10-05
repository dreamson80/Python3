number = int(input())
list_vorodi = []
list_miyangin = []

for i in range(1, number + 1):
    vorodi = input().split()
    for i in range(len(vorodi)):
                   vorodi[i] = int(vorodi[i])
    list_vorodi.append(vorodi)

for i in range(len(list_vorodi)):
    list_miyangin.append(int(sum(list_vorodi[i]) / len(list_vorodi[i])))

min_lm = min(list_miyangin)

string_lm = []

for i in range(len(list_miyangin)):
    string_lm.append(str(list_miyangin[i]))

my_index = string_lm.index(str(min_lm)) + 1

print(min_lm, my_index)

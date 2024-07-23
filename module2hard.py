number_ = int(input('Введите число от 3 до 20:  '))
list_ = []

for i in range(1, 20):
    for j in range(1, 20):
        k = i + j
        if i != j and number_ % k == 0:  # узнаем ВСЕ пары какие нам подходят впринципе.
            if i < j:
                list_.append([i, j])     # расставляем значения в списках-парах по возрастанию, для проврки повторов.
            else:
                list_.append([j, i])

list_2 = []
for i in list_:
    if i not in list_2:                  # удаляем повторы
        list_2.append(i)

print(f'Для числа', number_, 'подойдут следующие пары: ', *list_2)

# ну или в странном виде, как в задании было.
str_ = str()
for i in list_2:
    for j in i:
        str_ += str(j)
print(f'Для числа', number_, 'подойдут следующие пары: ', str_)



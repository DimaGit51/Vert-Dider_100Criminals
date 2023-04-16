#Допустим, есть сотня заключенных. Они пронумерованы от 1 до 100 (в программе от 0 до 99 для удобаства)
#Листочки с этими номерами раскладывают в коробки случайным образом в отдельной комнате
#Заключенный заходят в комнату по одному и за 50 попыток должны найти свой номер
#Потом они закрывают коробки и выходят (и молчат)
#Если все 100 участников найдут свои номера в коробках, то их всех отпустят. Если нет, то казнят!

#Вероятность, что все 100 заключенных найдут свой номер = 31%

#Эта программа создает 100 заключенных, которые ходят по стратегии из видео
#Можете проверить это сами

import random #Библиотека Рандом

criminals = 100 #Количество заключенных
box = [] #Коробки

#Присваиваем каждой коробке номер
for i in range(criminals):
    box.append(i)

print("Paper:",box)
random.shuffle(box) #Перемешиваем коробки
print("Paper random:",box)

GoNum = [] #Список для количества шагов всех 100 заключенных
for j in range(criminals):
    Go = [] #Список шагов одного заключенного
    LogicEnd = False #Логическая переменная выхода
    status = j #Присваиваем статусу переменную заключенного
    while not LogicEnd: #Пока логическая переменная Ложь
        Go.append(box[status]) #Добавить в список шагов номер внутри коробки
        if j == box[status]: #Если при вскрытии коробки номер коробки равен номеру заключенного
            LogicEnd = True #Логическая переменная Правда
        status = box[status] #Статус равен номеру коробки
    GoNum.append(len(Go)) #Все ходы заключенного завершены
    print(j, len(Go), Go) #Печатаем номер преступника, длины шагов, шаги

print("max:",max(GoNum)) #Маскимальная длина шагов всех преступников
print("min:",min(GoNum)) #Минимальная длина шагов всех преступников



#Программа генерации фейковых персонажей. Делалась для изучения работы генератора случайных чисел и списков.
import random

#Списки имен
name_man = ['Алан', 'Александр', 'Алексей', 'Анатолий', 'Андрей', 'Антон', 'Арсен', 'Арсений', 'Артем', 'Артемий', \
            'Артур', 'Богдан', 'Борис', 'Вадим', 'Валентин', 'Валерий', 'Василий', 'Виктор', 'Виталий', 'Владимир', \
            'Владислав', 'Всеволод', 'Вячеслав', 'Геннадий', 'Георгий', 'Герман', 'Глеб', 'Гордей', 'Григорий', 'Давид', \
            'Дамир', 'Даниил', 'Демид', 'Демьян', 'Денис', 'Дмитрий', 'Евгений', 'Егор', 'Елисей', 'Захар', 'Иван', \
            'Игнат', 'Игорь', 'Илья', 'Ильяс', 'Камиль', 'Карим', 'Кирилл', 'Клим', 'Константин', 'Лев', 'Леонид', \
            'Макар', 'Максим', 'Марат', 'Марк', 'Марсель', 'Матвей', 'Мирон', 'Мирослав', 'Михаил', 'Назар', \
            'Никита', 'Николай', 'Олег', 'Павел', 'Петр', 'Платон', 'Прохор', 'Рамиль', 'Ратмир', 'Ринат', \
            'Роберт', 'Родион', 'Роман', 'Ростислав', 'Руслан', 'Рустам', 'Савва', 'Савелий', 'Святослав', 'Семен',\
            'Сергей', 'Станислав', 'Степан', 'Тамерлан', 'Тимофей', 'Тимур', 'Тихон', 'Федор', 'Филипп',\
            'Шамиль', 'Эдуард', 'Эльдар', 'Эмиль', 'Эрик', 'Юрий', 'Ян', 'Ярослав'
            ]
name_woman = ['Агата', 'Агния', 'Аделина', 'Аида', 'Аксинья', 'Александра', 'Алена', 'Алина', 'Алиса', 'Алия',\
              'Алла', 'Альбина', 'Амелия', 'Амина', 'Анастасия', 'Ангелина', 'Анна', 'Антонина', 'Ариана', \
              'Арина', 'Валентина', 'Валерия', 'Варвара', 'Василина', 'Василиса', 'Вера', 'Вероника', 'Виктория',\
              'Виолетта', 'Владислава', 'Галина', 'Дарина', 'Дарья', 'Диана', 'Дина', 'Ева', 'Евангелина', \
              'Евгения', 'Екатерина', 'Елена', 'Елизавета', 'Есения', 'Жанна', 'Зарина', 'Злата', 'Илона', 'Инна', \
              'Ирина', ' Камилла', 'Карина', 'Каролина', 'Кира', 'Клавдия', 'Кристина', 'Ксения', 'Лариса', 'Лейла', \
              'Лиана', 'Лидия', 'Лилия', 'Лина', 'Лия', 'Любовь', 'Людмила', 'Майя', 'Маргарита', 'Марианна', \
              'Марина', 'Мария', 'Мелания', 'Мила', 'Милана', 'Милена', 'Мирослава', 'Надежда', 'Наталья', 'Нелли',\
              'Ника', 'Нина', 'Оксана', 'Олеся', 'Ольга', 'Полина', 'Регина', 'Сабина', 'Светлана', 'София', \
              'Стефания', 'Таисия', 'Тамара', 'Татьяна', 'Ульяна', 'Эвелина', 'Элина', 'Эльвира', 'Эльмира', \
              'Эмилия', 'Юлия', 'Яна', 'Ярослава']

#Списки фамилий
surname_man = ['Смирнов', 'Иванов', 'Кузнецов', 'Попов', 'Соколов', 'Лебедев', 'Козлов', 'Новиков', 'Морозов', \
               'Петров', 'Волков', 'Соловьёв', 'Васильев', 'Зайцев', 'Павлов', 'Семёнов', 'Голубев', 'Виноградов', \
               'Богданов', 'Воробьёв', 'Фёдоров', 'Михайлов', 'Беляев', 'Тарасов', 'Белов', 'Комаров', 'Орлов', \
               'Киселёв', 'Макаров', 'Андреев', 'Ковалёв', 'Ильин', 'Гусев', 'Титов', 'Кузьмин', 'Кудрявцев',\
               'Баранов', 'Куликов', 'Алексеев', 'Степанов', 'Бирюков', 'Шарапов', 'Никонов', 'Щукин', 'Дьячков', \
               'Одинцов', 'Сазонов', 'Якушев', 'Яковлев', 'Сорокин', 'Сергеев']
surname_woman = ['Ковалёва', 'Ильина', 'Гусева', 'Титова', 'Кузьмина', 'Кудрявцева', 'Баранова', 'Куликова', \
                 'Алексеева', 'Степанова', 'Яковалева', 'Сорокина', 'Сергеева', 'Романова', 'Захарова', 'Борисова', \
                 'Королева', 'Герасимова', 'Пономарева', 'Григорьева', 'Лазарева', 'Медведева', 'Ершова', \
                 'Никитина', 'Соболева', 'Рябова', 'Полякова', 'Цветкова', 'Данилова', 'Жукова', 'Фролова', \
                 'Журавлева', 'Николаева', 'Путина', 'Молчанова', 'Крылова', 'Максимова', 'Сидорова', 'Осипова', \
                 'Белоусова', 'Федотова', 'Дорофеева', 'Егорова', 'Панина', 'Матвеева', 'Боброва', 'митриева', \
                 'Калинина', 'Анисимова', 'Петухова', 'Пугачева', 'Антонова', 'Тимофеева', 'Никифорова', 'Веселова',\
                 'Филиппова', 'Романова', 'Маркова', 'Большакова', 'Суханова', 'Миронова', 'Александрова', \
                 'Коновалова', 'Шестакова', 'Казакова', 'Ефимова', 'Денисова', 'Громова', 'Фомина', 'Андреева',\
                 'Давыдова', 'Мельникова', 'Щербакова', 'Блинова', 'Колесникова', 'Иванова', 'Смирнова', 'Кузнецова', \
                 'Попова', 'Соколова', 'Лебедева', 'Козлова', 'Новикова', 'Морозова', 'Петрова', 'Волкова',\
                 'Соловьева', 'Васильева', 'Зайцева', 'Павлова', 'Семенова', 'Голубева', 'Виноградова', 'Богданова', \
                 'Воробьева', 'Федорова', 'Михайлова', 'Беляева', 'Тарасова', 'Белова']

#Запрашиваем пол генерируемого персонажа
sex = str(input('Генерируем мужчину или женщину? : '))
if sex == 'мужчину':
    print ('Сгенерированне мужские данные:\n')
    serial = []
    serial = random.sample('абвгдеёжзийклмнопрстуфхцчшщъыьэюя', 2)
    serial_1 = serial[0]
    serial_2 = serial[1]
    serial = serial_1 + serial_2
    number_pass = random.randrange (100000, 999999)
    print ('Серия и номер паспорта: {} {}'. format(serial.upper(), number_pass))
    quantity_name = len(name_man)
    quantity_random_name = (random.randrange(0, quantity_name))
    print ('Имя: ', (name_man[quantity_random_name]))
    quantity_name = len(surname_man)
    quantity_random_name = (random.randrange(0, quantity_name))
    print ('Фамилия: ', surname_man[quantity_random_name])
    print ('Возраст: ', random.randrange(18, 65))
else:
    print ('Сгенерированные женские данные:\n')
    serial = []
    serial = random.sample('абвгдеёжзийклмнопрстуфхцчшщъыьэюя', 2)
    serial_1 = serial[0]
    serial_2 = serial[1]
    serial = serial_1 + serial_2
    #print (serial)
    number_pass = random.randrange (100000, 999999)
    print ('Серия и номер паспорта: {} {}'. format(serial.upper(), number_pass))
    quantity_name = len(name_woman)
    quantity_random_name = (random.randrange(0, quantity_name))
    print ('Имя: ', (name_woman[quantity_random_name]))
    quantity_name = len(surname_woman)
    quantity_random_name = (random.randrange(0, quantity_name))
    print ('Фамилия: ', surname_woman[quantity_random_name])
    print ('Возраст: ', random.randrange(18, 65))

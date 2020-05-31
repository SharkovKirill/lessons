class Lesson():
    all_lessons = []
    def __init__(self,day,time,person,name,type,room):
        self.day = day
        self.time = time
        self.person = person
        self.name = name
        self.type = type
        self.room = room
    def __str__(self):
        return '|' + '%-14s' % self.day + '|' + \
               '%-6s' % self.time + '|' + \
               '%-18s' % self.person + '|' + \
               '%-20s' % self.name + '|' + \
               '%-17s' % self.type + '|' + \
               '%-19s' % self.room + '|'

    def __repr__(self):
        return self.__str__()

def load_lessons(file_name):
    with open(file_name,encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            sp = line.split(';')
            room=sp.pop()
            Lesson.all_lessons.append(Lesson(*sp, room[:-1]))

def show():
    print('-' * 101)
    print('| День недели  |Начало| Преподаватаель   |      Предмет       | Лекция/Практика |       Кабинет     |')
    print('=' * 101)
    for lessons in Lesson.all_lessons:
        print(lessons)
    print('-' * 101)

load_lessons('lessons.txt')
show()


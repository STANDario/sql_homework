from datetime import datetime, date, timedelta
from faker import Faker
from random import randint
import sqlite3


disciplines = [
    "Вища математика",
    "Дискретна математика",
    "Лінійна алгебра",
    "Програмування",
    "Теорія імовірності",
    "Історія України",
    "Англійська мова"
]

groups = ["42-ЄС1", "42-ЛЗ2", "12-ЄС3"]
NUMBER_TEACHERS = 5
NUMBER_STUDENTS = 50
MAX_NUMBERS_OF_GRADES = 20
fake = Faker("uk-UA")
connect = sqlite3.connect("homework.db")
cur = connect.cursor()


def seed_teachers():
    teachers = [fake.name() for _ in range(NUMBER_TEACHERS)]
    sql = "INSERT INTO teachers(fullname) VALUES(?);"
    cur.executemany(sql, zip(teachers,))


def seed_disciplines():
    sql = "INSERT INTO disciplines(name, teacher_id) VALUES(?, ?);"
    cur.executemany(sql, zip(disciplines, iter(randint(1, NUMBER_TEACHERS) for _ in range(len(disciplines)))))


def seed_groups():
    sql = "INSERT INTO groups(name) VALUES(?);"
    cur.executemany(sql, zip(groups,))


def seed_students():
    students = [fake.name() for _ in range(NUMBER_STUDENTS)]
    sql = "INSERT INTO students(fullname, group_id) VALUES(?, ?);"
    cur.executemany(sql, zip(students, iter(randint(1, len(groups)) for _ in range(len(students)))))


def seed_grades():
    start_date = datetime.strptime("2022-09-01", "%Y-%m-%d")
    end_date = datetime.strptime("2023-06-15", "%Y-%m-%d")
    sql = ("INSERT INTO grades(disciplines_id, student_id, grade, date_of) VALUES(?, ?, ?, ?);")

    def get_list_date(start: date, end: date):
        result =[]
        current_date = start
        while current_date <= end:
            if current_date.isoweekday() < 6:
                result.append(current_date)
            current_date += timedelta(1)
        return result

    list_dates = get_list_date(start_date, end_date)

    grades = []
    student_grades_count = {}

    for day in list_dates:
        random_discipline = randint(1, len(disciplines))
        random_students = [randint(1, NUMBER_STUDENTS) for _ in range(4)]
        for student in random_students:
            if student not in student_grades_count:
                student_grades_count[student] = 0
            if student_grades_count[student] < MAX_NUMBERS_OF_GRADES:
                grades.append((random_discipline, student, randint(1, 12), day.date()))
                student_grades_count[student] += 1
    cur.executemany(sql, grades)


if __name__ == '__main__':
    try:
        seed_teachers()
        seed_disciplines()
        seed_groups()
        seed_students()
        seed_grades()
        connect.commit()
    except sqlite3.Error as error:
        print(error)
    finally:
        connect.close()

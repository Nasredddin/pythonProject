from collections import namedtuple
student = namedtuple("student", "name age mark city")
students = (
    student("Андрей", 19, 6.5, "Винница"),

    student("Игорь", 18, 8.0, "Харьков"),

    student("Виктор", 20, 5.1, "Мариуполь"),

    student("Виктория", 19, 8.5, "Одесса"),

    student("Наталья", 21, 7.3, "Киев"),

    student("Катя", 20, 9.1, "Львов"),

    student("Никита", 19, 8.7, "Николаев")
)

marks = 0
for i in range(1, len(students) + 1):
    var = students[i - 1][2]
    marks += var
# print(marks)

m_marks = marks / len(students)
# print(m_marks)

good_students = [student.name for student in students if student.mark >= m_marks]
print("Ученики", ", ".join(good_students), "в этом семестре хорошо учатся!")

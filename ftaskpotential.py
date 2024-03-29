import csv

with open('students.csv', encoding='utf8') as file:
    reader = csv.reader(file, delimiter=',')
    answer = list(reader)[1:]
    count_class = {}
    sum_class = {}
    for id, name, titleProject_id, level, score in answer:
        if 'Хадаров Владимир' in name:
            print(f'Ты получил: {score}, за проект - {titleProject_id}')
        count_class[level] = count_class.get(level, 0) + 1
        sum_class[level] = sum_class.get(level, 0) + (int(score) if score != 'None' else 0)

    for el in answer:
        if el[-1] == 'None':
            el[-1] = round(sum_class[el[-2]] / count_class[el[-2]], 3)

with open('student_new.csv', 'w', encoding='utf8', newline='') as file:
    w = csv.writer(file)
    w.writerow(['id', 'Name', 'titleProject_id', 'class', 'score'])
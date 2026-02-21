def filter_excellent_students(file_name, file_autput_name = None):
    with open(file_name , "r", encoding="utf-8") as file:
        lines = file.readlines()
        # print(lines)
    processed_students = []
    for line in lines :
        line = line.strip()
        name,grade_str = line.split(",")
        grade = int(grade_str)
        processed_students.append(name, grade)
    print(processed_students)
filter_excellent_students("students.txt")
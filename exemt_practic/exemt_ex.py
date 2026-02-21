def filter_excellent_students(file_name, file_autput_name):
    with open(file_name , "r", encoding="utf-8") as file:
        lines = file.readlines()
        # print(lines)
    processed_students = []
    for line in lines :
        line = line.strip()
        if not line:
            continue
        if "," not in line:
            continue
        try:
            name,grade_str = line.split(",")
            grade = int(grade_str)
            processed_students.append((name, grade))
        except ValueError:
            continue
    excellent_students =[]
    for name , grade in processed_students:
        if grade >= 90 :
            excellent_students.append(name)
        else:
            continue
    with open(file_autput_name, "w" ,encoding="utf-8") as f :
        for name in excellent_students:
            f.write(name + "\n")
    print(processed_students)
    print("file redus secssed ", file_autput_name)

# filter_excellent_students("students.txt", "excellent.txt")




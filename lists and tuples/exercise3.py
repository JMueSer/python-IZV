subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
marks = []
for subject in subjects:
    mark = float(input(f"What is your mark in {subject}? "))
    marks.append(mark)
for x in range(len(subjects)):
    print(f"In {subjects[x]} you have a {marks[x]}")
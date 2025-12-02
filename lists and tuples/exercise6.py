subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
passed = []
for subject in subjects:
    mark = float(input(f"What is your mark in {subject}? "))
    if mark >= 5:
        passed.append(subject)
for subject in passed:
    subjects.remove(subject)
if subjects:
    print(f"You need to recover: {subjects}")
else:
    print("You passed everything")
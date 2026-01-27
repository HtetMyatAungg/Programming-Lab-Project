import pandas as pd
import matplotlib.pyplot as plt

def getgrade(marks):
    if marks >= 70:
       return "A" 
    elif marks >= 60:
        return "B"
    elif marks >= 50:
        return "C"
    elif marks >=40:
        return "D"
    else:
        return"F"

def pass_fail(marks):
    return "Pass" if marks >= 40 else "Fail"

def average_mark(marks):
    return sum(marks)/len(marks)
    
modules = {"Programming Lab": 0,
           "Mathematical Structures": 0,
           "OOP1": 0,
           "Machine Fundamentals": 0}
for module in modules:
    while True:
        try:
           marks = float(input(f"Input Grade {module}: "))
           if 0 <= marks <= 100:
                modules[module] = marks
                break
           else:
                print("Grades must be between 0 & 100")
        except ValueError:
            print("Input a valid number")

marks_list = list(modules.values())
average = average_mark(marks_list)
minimum = min(marks_list)
maximum = max(marks_list)

progression = "Progress" if average >= 50 else "Do Not Progress"
print("Result")
print("-"*50)

results = []

for module, marks in modules.items():
    grade = getgrade(marks)
    status = pass_fail(marks)
    results.append([module, marks, grade, status])
    print(f"{module}: {marks}%, Grade: {grade}, {status}")
print(f"Average: {average}%, {progression}")
print("-"*50)
data = pd.DataFrame(results, columns=["Module", "Mark", "Grade", "Status"])
print("Table")
print(data)

data.to_csv("student_results.csv", index=False)

plt.bar(modules.keys(), modules.values())
plt.xlabel("Modules")
plt.ylabel("Marks (%)")
plt.title("Student Marks by Module")
plt.ylim(0, 100)
plt.show()
    
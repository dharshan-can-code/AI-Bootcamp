import csv

students = [

    ["Name", "Grade", "Score"],

    ["Priya", 9, 97],

    ["Marcus", 9, 84],

]

with open("new_students.csv", "w",

          newline="") as file:

    writer = csv.writer(file)

    writer.writerows(students)
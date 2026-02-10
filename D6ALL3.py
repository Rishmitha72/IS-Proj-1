name = input("Enter your name: ")
goal = input("Enter your Daily Goal: ")

with open("journal.txt", "w") as file:
    file.write(f"{name} - {goal}\n")

print("Your entry has been saved!")

Name,Grade,Status
Alice,A,Pass
Bob,B,Pass
Charlie,F,Fail

import csv

with open("studentsD6T2.csv", "r") as file:
    reader = csv.DictReader(file)  

    for row in reader:
        if row["Status"] == "Pass":  
            print(row["Name"])       
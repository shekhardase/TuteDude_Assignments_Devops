# marks = int(input("Enter your marks:\n "))
# grade = ""

# if marks > 90:
#     grade = "A"
# elif marks < 90:
#     grade = "B"
# elif marks < 80:
#     grade = "C"
# elif marks < 70:
#     grade = "D"
# else:
#     grade = "F"


# print(grade)


grades = {"Shekhar": "A", "Pintu": "B", "Adya": "C", "Chotu": "D"}

print(grades)


grades.update({"Abhishek": "F"})
grades["Buddhu"] = "A++"

print(grades)

print(grades["Pintu"])

print(len(grades))

for i in grades:
    print(i, grades[i])


print("\n")

F_I_L_E = open("Dem.txt")

print(F_I_L_E.read())

F_I_L_E.close()

# f = open("Newfile.txt", "x+t")

# f.write("This is new created file for checking how actually it works")

# print(f.read())
# f.close()


file = open("new.txt", "r")

print(file.read())

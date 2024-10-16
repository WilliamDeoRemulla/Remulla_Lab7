pregrade = int(input("Preliminary Period Grade: "))
midgrade = int(input("Midterm Period Grade: "))
figrade =  int(input("Final Period Grade: "))

if pregrade < 40 or midgrade < 40 or figrade < 40:
    print("Error")
    exit()
if pregrade > 100 or midgrade > 100 or figrade > 100:
    print("Error")
    exit()


FGrade = ((pregrade+midgrade+figrade)//3)
print("Final Grade:", FGrade,"%" )

if FGrade >= 99 and FGrade <= 100:
    print("Grade Points: 1.00 Excellent")
if FGrade >= 96 and FGrade <= 98:
    print("Grade Points: 1.25 Outstanding")
if FGrade >= 93 and FGrade <= 95:
    print("Grade Points: 1.50 Superior")
if FGrade >= 90 and FGrade <= 92:
    print("Grade Points: 1.75 Very Good")
if FGrade >= 87 and FGrade <= 89:
    print("Grade Points: 2.00 Good")
if FGrade >= 84 and FGrade <= 86:
    print("Grade Points: 2.25 Satisfactory")
if FGrade >= 81 and FGrade <= 83:
    print("Grade Points: 2.50 Fairly Satisfactory")
if FGrade >= 78 and FGrade <= 80:
    print("Grade Points: 2.75 Fair")
if FGrade >= 75 and FGrade <= 77:
    print("Grade Points: 3.00 Passed")
if FGrade < 75:
    print("Grade Points: 5.00 Failed")
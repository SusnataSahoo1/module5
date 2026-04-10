student= {
          'John':80,
          'Harry':90,
          'Colin':76,
          'Ron':67,
          'Gerry':72
}

inputStudent = input("Enter student's name")
if inputStudent not in student:
    print("Student not found")
else:
    outputMark = student[inputStudent]
    print(f"{inputStudent}'s mark : {outputMark}")




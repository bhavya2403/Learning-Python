
def gradingStudents(grades):
    arr = []
    for i in grades:
        if i >= 35:
            if i % 5 >= 3:
                i += 5 - (i % 5)
        arr.append(i)

    return arr

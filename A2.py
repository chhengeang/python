def student():
    subject = input("Input subject:")
    score =float(input("Input score:"))
    grade = ""
    fail_value=""
    passs=""
    if score >= 90:
        grade = "A"
        passs="you are passed"
    elif score >= 80:
        grade = "B"
        passs = "you are passed"
    elif score >= 70:
        grade = "C"
        passs = "you are passed"
    elif score >= 60:
        grade = "D"
        passs = "you are passed"
    else:
        grade = "F"
        fail_value="You are failed"

    result = "Subject="+subject +"\n" + "Score="+str(score) + "\n" + fail_value + "\n"+"you got grade" +grade + "\n" + passs
    return result
print(student())


#program of finding score

score=int(input("enter your score"))
if score >= 90 and score <= 100:
    print("you have A grade")
elif score >= 80 and score <=89:
    print("you have B grade")
elif score >= 70 and score <=79:
    print("you have C grade")
elif score >= 60 and score <=69:
    print("you have D grade")
elif score >= 50 and score <=59:
    print("you have F grade")
else:
    print("you have entered invalid score")
max_score = 0
min_score = 101
total_score = 0
alert_scores = ""

i = 0

while i < 10:
    score = int(input("test score no." + str(i + 1) + ": "))

    if score > 100:
        alert_scores = alert_scores + " " + str(score) + " "

    if score >= max_score:
        max_score = score

    if score <= min_score:
        min_score = score

    i += 1
    total_score += score

if len(alert_scores) > 0 :
    print("You input score more than 100 => " + alert_scores)

print("Max score:", max_score)
print("Min score:", min_score)
print("Average score:", total_score/10)
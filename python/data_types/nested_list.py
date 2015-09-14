student_score = []
students = []
scores = []
for i in range(int(raw_input())):
    student = raw_input()
    score = float(raw_input())
    students.append(student)
    scores.append(score)
    my_list = [student, float(score)]
    student_score.append(my_list)
sorted_unique_scores = sorted(set(scores))
second_lowest = list(sorted_unique_scores)[1]
second_lowest_students = []
for i in range(len(student_score)):
    if student_score[i][1] == second_lowest:
        second_lowest_students.append(student_score[i][0])
for i in sorted(second_lowest_students):
    print i

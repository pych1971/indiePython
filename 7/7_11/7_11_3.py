subject_marks = [('English', 88), ('Science', 90), ('Maths', 88),
                 ('Physics', 93), ('History', 78), ('French', 78),
                 ('Art', 78), ('Chemistry', 88), ('Programming', 91)]
a = sorted(subject_marks, key=lambda x: x[0])
a = sorted(a, key=lambda x: x[1], reverse=True)

for i in a:
    print(i[0], i[1])

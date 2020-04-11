my_dict = {}


def my_func(name):
    if name[0] == '-':
        name[0] = 0
    else:
        name[0] = int(name[0])


with open('les6.txt', 'r') as init_f:
    for line in init_f:
        name, lecture, practical, laboratory = line.split()
        lecture = lecture.split('(')
        practical = practical.split('(')
        laboratory = laboratory.split('(')

        my_func(lecture)
        my_func(practical)
        my_func(laboratory)

        clock = (int(lecture[0]) + int(practical[0]) + int(laboratory[0]))
        my_dict.update({name: clock})

print(my_dict)

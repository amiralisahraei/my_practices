from cgi import print_arguments
from pickletools import pystring
from time import process_time_ns

from pydantic import NumberNotGeError
from data import teams


d = " 3 - 2 * 3"
d = d.split()


def calculater(input_string):
    my_string = input_string
    for index, value in enumerate(my_string):

        # if value.isdigit() == True:
        #     result = int(value)

        if value == '**' and index != 0 and index != (len(my_string)-1):
            final = int(my_string[index-1]) ** int(my_string[index+1])
            my_string[0] = str(final)
            del my_string[1:index+2]
            try:
                if(all(isinstance(int(x), int) for x in my_string)) == True:
                    print(my_string)
            except:
                calculater(my_string)

        if value == '*' and index != 0 and index != (len(my_string)-1):
            final = int(my_string[index-1]) * int(my_string[index+1])
            # print(f"this is final : {final}")

            my_string[0] = str(final)
            del my_string[1:index+2]
            # print(f"this is my string : {my_string}")

            try:
                if(all(isinstance(int(x), int) for x in my_string)) == True:
                    print(my_string)
            except:
                calculater(my_string)

        if value == '/' and index != 0 and index != (len(my_string)-1):
            final = int(my_string[index-1]) / int(my_string[index+1])
            my_string[0] = str(int(final))
            del my_string[1:index+2]
            try:
                if(all(isinstance(int(x), int) for x in my_string)) == True:
                    print(my_string)
            except:
                calculater(my_string)

        if value == '+' and index != 0 and index != (len(my_string)-1):
            final = int(my_string[index-1]) + int(my_string[index+1])
            my_string[0] = str(final)
            del my_string[1:index+2]
            try:
                if(all(isinstance(int(x), int) for x in my_string)) == True:
                    print(my_string)
            except:
                calculater(my_string)

        if value == '-' and index != 0 and index != (len(my_string)-1):
            final = int(my_string[index-1]) - int(my_string[index+1])
            my_string[0] = str(final)
            del my_string[1:index+2]
            try:
                if(all(isinstance(int(x), int) for x in my_string)) == True:
                    print(my_string)
            except:
                calculater(my_string)


# calculater(d)
####################################################


def parse_result(team):

    output = list([0, 0, 0])
    for text in team['result']:
        if text == "w":
            output[0] += 1
        if text == "d":
            output[1] += 1
        if text == "l":
            output[2] += 1
    return {
        'name': team['name'],
        'win': output[0],
        'draw': output[1],
        'lose': output[2],
        'pos_goals': team['pos_goals'],
        'neg_goals': team['neg_goals']
    }


def calculate_score(team):
    score = (team['win'] * 3) + team['draw']
    team['score'] = score
    return team


def check_score(team):
    return team['score'] >= 50


def calculate_goal_difference(team):
    different = team['pos_goals'] - team['neg_goals']
    team['goal_difference'] = different
    return team


tmp_score_board = list(map(parse_result, teams))

score_board = list(map(calculate_score, tmp_score_board))

passed_teams = list(filter(lambda t: t['score'] >= 50, score_board))

goal_difference = list(map(calculate_goal_difference, score_board))


# score_board = sorted(score_board, key=lambda x: (
#     x['score'], x['goal_difference']), reverse=True)
# for index, team in enumerate(score_board):
#     print(index+1, team)
#     print("-------------------------")

words = ['hello', 'hell asd', 'hello world']

tmp = ''
ziped = list(zip(*words))
for i in ziped:
    if len(set(i)) != 1:
        break
    tmp += i[0]

# print(tmp)
# ////////////////////////////////////////////
# user_input = input("enter your number")

# try:
#     user_age = int(user_input)
# except:
#     print("except fired")
# else:
#     print("else fired")
# finally:
#     print("finally fired")
# /////////////////////////////////////////////////

# def number_generator():
#     for i in range(100):
#         if i % 7 == 0:
#             yield i
    
#     print("finished")

# list_number = number_generator()
# for i in list_number:
#     print(i)

# with open("amirali.csv", 'w') as f:
#     for i in range(100):
#         f.write(f"sample user data : {i} \n")

# def reader(filename):
#     file_ = open(filename, 'r')
#     data = file_.read().split('\n')
#     file_.close()
#     return data

# for i in reader('amirali.csv'):
#     print(i)

# def reader_generator(filename):
#     for i in open(filename, 'r'):
#         yield i

# for i in reader_generator('amirali.csv'):
#     print(i)

def counter_generater():
    for i in range(100):
        if i % 2 == 0:
            yield i

def counter():
    for i in range(100):
        if i % 2 == 0:
            print(i)

for i in counter():
    print(i)

# ///////////////////////////////////////////////////////

# VALIDATING ANSWERS
import json

#JSON filepath
filename1 = 'correct_ans.json'
filename2 = 'user_answers.json'

#Load JSON data 
def load_correct_answers(filename1):
    with open(filename1, 'r') as file:
        correct_answers = json.load(file)
    return correct_answers



#Load user_answers from JSON
def load_user_answers(filename2):
    with open(filename2, 'r') as file:
        user_answers = json.load(file)
    return user_answers



correct_answers = load_correct_answers(filename1)
answers_list = list(correct_answers.values()) #convert the dict(correct_answers) into an item type


user_answers = load_user_answers(filename2)
user_answers_list = list(user_answers.values()) #convert the dict(user_answers) into an item type


score = 0
#loop over range of the length of user provided answers
for i in range(len(user_answers_list)):
        #Test for correct answers and increment score value by 1
        if user_answers_list[i] == answers_list[i]:
             score += 1

#Print test scores
print(f"TOTAL TEST SCORE : {score} out of {len(answers_list)}")

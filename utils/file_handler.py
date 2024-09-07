import json
# Function to handle file read and write
# Reading the questions and writing the answers to JSON file

#filepath 
filename = 'quiz_data.json'
filename2 = 'user_answers.json'


print("THIS IS AN ASSESSMENT TEST")
print("Input (A,B,C,D) as your correct option!")



#function to load JSON into dict
def load_quiz_data(filename):
    """Load JSON data"""
    with open(filename, 'r') as file:
        dataDict = json.load(file)
    return dataDict #returns a Dictionary



quiz_questions = load_quiz_data('quiz_data.json')


#Get user_inputs for quiz questions
for quiz_question in quiz_questions.values():
    ans_1 = input(f"{quiz_question[0]} ").upper()
    ans_2 = input(f"{quiz_question[1]} ").upper()
    ans_3 = input(f"{quiz_question[2]} ").upper()
    ans_4 = input(f"{quiz_question[3]} ").upper()
    ans_5 = input(f"{quiz_question[4]} ").upper()
    ans_6 = input(f"{quiz_question[5]} ").upper()
    ans_7 = input(f"{quiz_question[6]} ").upper()
    ans_8 = input(f"{quiz_question[7]} ").upper()
    ans_9 = input(f"{quiz_question[8]} ").upper()
    ans_10 = input(f"{quiz_question[9]} ").upper()


#Save user_inputs as dict key-value pairs
users_answers = {
    'q1': ans_1,
    'q2': ans_2,
    'q3': ans_3,
    'q4': ans_4,
    'q5': ans_5,
    'q6': ans_6,
    'q7': ans_7,
    'q8': ans_8,
    'q9': ans_9,
    'q10': ans_10
}

#Write the users_answers in dict to JSON
def write_to_json(filename2):
    with open(filename2, 'w') as file:
        json.dump(users_answers, file, indent=4)
    return users_answers
    

users_answer = write_to_json('user_answers.json')
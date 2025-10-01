import random

quizz = [
    {'question': 'Combien de fois la France a gagné la coupe du monde', 'response': '2'},
    {'question': 'Quand a été fondée Apple ?', 'response': '1976'},
    {'question': 'Qui a fondé Space X', 'response': 'Elon Musk'},
]

number_of_lives = 3
failed_response = 0


def print_remained_lives():
    print(f"Dommage ! Il te reste {number_of_lives} chance(s)")

def select_new_question_response():
    # select a random question from the quizz list
    len_quizz = len(quizz)
    random_quizz_item_indice = random.randint(0, len_quizz - 1)
    question = quizz[random_quizz_item_indice]['question']
    response = quizz[random_quizz_item_indice]['response'].lower()
    # remove the question from the quizz list so that won't be asked again
    quizz.remove(quizz[random_quizz_item_indice])
    # return question and response
    return question, response

def can_try_again():
    if failed_response == number_of_lives:
        print_remained_lives()
        return False
    else:
        return True

def ask_the_question(question):
    user_response = input(f" question : {question}")
    return user_response

def check_answer(response, user_response):
    if user_response.lower() == response:
        return True
    else:
        global failed_response
        failed_response += 1
        return False

print("Welcome to your quizz!")
print(f"You have {number_of_lives} lives.")

while len(quizz) > 0 and failed_response < number_of_lives:
    # print(f"longueur du quizz : {len(quizz)}")
    question, response = select_new_question_response()

    user_response = ask_the_question(question)
    next_question = check_answer(response, user_response)

    if next_question == False:
        while failed_response < number_of_lives and next_question == False:
            user_response = ask_the_question(question)
            next_question = check_answer(response, user_response)

if failed_response < number_of_lives:
    print("Bravo tu as gagné le quizz")
else:
    print("Oh non ! Tu as perdu le jeu")
def test_quiz(lives = 3):
    questions = {"Combien de fois la france a gagné la coupe du monde ? ":"2", "Quand a été fondé Apple ? ":"1976" , "Qui a fondé SpaceX ? ":"elon musk"}

    for question, answer in questions.items():
        while True:
            user_input = input(question)
            if user_input.lower() == answer.lower():
                print("Good job, this is the right answer !")
                break
            else:
                lives -= 1
                if lives <= 0:
                    print("Too bad, you lost the game...")
                    return
                print(f"Wrong answer, you have {lives} lives left. Try again !")

    print("Congratulations ! You completed the quiz.")

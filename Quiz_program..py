# this program will run a short quiz
# first, establish 'QUESTIONS' variable and put the questions in a list
# there are 12 questions in total, with a comma when moving on to the next question
list_of_questions = ("1. Whose assassination caused the outbreak of WW1? ",
    "2. how many Ulster championship titles has Tyrone GAA won in Gaelic Football?: ",
    "3. What is this application called?: ",
    "4. The first Pokemon games were released (In Japan) in what year?: ",
    "5. who painted 'Starry Starry Night'?: ",
    "6. in DC Comics, how many main colours of power (lantern) ring exist?",
    "7. What company manufactured the TT Coupe?: ",
    "8. What was the first game released on the original Xbox?: ",
    "9. How many secondary schools are there in Magherafelt? (excluding the Regional Colleges): ",
    "10. Which of these characters was added to Super Smash Bros first?: ",
    "11. What country in Europe has the most islands?: ",
    "12. The Marvel Comics superhero 'Wolverine' made his first appearance in what series?",
    "13. Who is the main character of the Die Hard movies?: ",
    "14. What counties in Ireland are home to the headquarters of each brand of Tayto?: ")

# here are the options that the user can pick for each question
options = (("A. Archduke Franz Ferdinand ", "B. Grigori Rasputin ", "C. Kaiser Wilhelm II "),
           ("A. 10", "B. 7", "C. 16"),
           ("A. CodeIt ", "B. PyCharm ", "C. Prgrm "),
           ("A. 1996 ", "B. 1998 ", "C. 1999 "),
           ("A. Vincent Van Gogh", "B. Pablo Picasso ", "C. Georgia O'Keefe "),
           ("A. 2", "B. 9", "C. 6"),
           ("A. Audi", "B. BMW", "C. Chevrolet"),
           ("A. Forza Motorsport", "B. Fable", "C. Halo Combat Evolved"),
           ("A. 3", "B. 6", "C. 5"),
           ("A. Marth", "B. Ness", "C. Shulk"),
           ("A. Greece", "B. Sweden", "C. Italy"),
           ("A. X-Men", "B. The Incredible Hulk", "C. Fantastic Four"),
           ("A. Ethan Hunt", "B. Jack Reacher", "C. John McClane"),
           ("A. Armagh and Meath", "B. Antrim and Dublin", "C. Tyrone and Cork"))

# the answers to each question
# guesses [] is for the user inputs
answers = ("A", "C", "B", "A", "A", "B", "A", "C", "C", "B", "B", "B", "C", "A")
guesses = []
# 0 is the default score
# the score will increase every time the user answers a questions correctly
score = 0
question_num = 0
answer_options = ("A", "B", "C")

# for loop to iterate the questions and options

for question in list_of_questions:
    print("--------------")
    print(question)
    # index in the 2nd for loop is used for question_num, because it is a 2d tuple
    # this will increase each question numbers from 1 to 2, 2 to 3, 3 to 4 etc.
    for option in options[question_num]:
        print(option)

    # .upper() method ensures that the user enters A, B, C, or D in uppercase, not lowercase
    # while True offers input validation to ensure the user can't progress unless A, B or C are entered

    while True:
        guess = input("Enter an option (A, B or C): ").upper()
        if guess in answer_options:
            break
        else:
            print("Incorrect input, try again with A, B or C!")

    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct answer!")
    else:
        print("Incorrect answer!")
        print(f"{answers[question_num]} is the correct answer!  ")
    # this variable will change the options for each question
    question_num += 1

# now to print out the results
print("--------------------------------")
print("     AND THE RESULTS ARE....    ")
print("--------------------------------")

# this piece of code will iterate the answers
print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()
# this for loop will print the guesses the user inputted
print("guesses: ", end="")
for guess in guesses:
    print(guess, end="")
print()

# this equation will figure out the user's score for the quiz
# dividing score by amount of question with len
# multiply by 100 to get a percentage score,

score = (int(score / len(list_of_questions) * 100))
# now to print the user's score, user % to get the score as a percentage
print(f"Your score is {score}%, thanks for playing my quiz! ")

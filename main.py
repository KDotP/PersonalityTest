basic_score = 0
question_num = 0

def Display_Ending(ending_name, ending_lore):
    print("\n")
    print("-----------------------------------")
    print(f"You are the: {ending_name}")
    print("-----------------------------------")
    for line in ending_lore:
        print(line)
    print("-----------------------------------")
    print("Press enter if you would like to take the test again.", end=" ")
    input()
    main()

# This is the basic question/answer function
# Will be reused by wrappers that expand upon the basic function
def Choice(question, answer1, answer2, answer3):
    global question_num
    question_num += 1
    print("")
    print("----------------------------------")
    print(f"Question {question_num}: {question}")
    print(f"1: {answer1}")
    print(f"2: {answer2}")
    print(f"3: {answer3}")
    print("----------------------------------")
    while True:
        choice = input("Your answer: ")
        if choice == "1":
            return 0
        elif choice == "2":
            return 1
        elif choice == "3":
            return 2
        else:
            print("Invalid input. Please enter 1, 2, or 3.")

# Only return 1 if the user selects the target answer, otherwise return 0
def Targeted_Choice(question, answer1, answer2, answer3, target_answer):
    ref = Choice(question, answer1, answer2, answer3)
    if ref == target_answer - 1: # Subtract 1 since an answer of 1 corresponds to a return value of 0
        return 1
    else:
        return 0

def Display_Beginning():
    print("Welcome to the world's only accurate personality test. This will be a grueling and difficult test, but if you can make it through, you will be provided with unprecidented incite into your very heart and soul.")
    print("The test will consist of a number of questions. Each question will have 3 possible answers. You will be asked to choose the answer that best describes you.")
    print("To answer a question, simply type the number of the answer you choose and press enter. For example, if you choose the first answer, you would type '1' and press enter.")
    print("Please do not type any other characters or words, as the such an answer will be rejected and you will be asked to answer the question again.")
    print("To begin, press enter.", end=" ")

def main():
    Display_Beginning()
    bread_rank = Choice("What are your thoughts on banana bread?", "It's not the worst", "I fear giving my true feelings", "Burn it in the holy flames")
    if bread_rank == 0:
        Display_Ending("RAT - Vermin", [
            "You are lesser than man. Merely vermin among beasts. You are a blight upon the world and a stain on the name of humanity.",
            "No one will mourn your passing. Some may even rejoice. To name your positivities would be an empty page, to name your negativities would require so many lines it would take week to compile.",
            "Do not pass go. Do not collect $200. Do not attempt to cheat the truth by changing your answers. You are a rat, and history will remember you as such."
        ])
    
    # Do not record score, I do not care
    Choice("Sorry about that, had to filter the freaks. Do you prefer working alone or in groups?", "I prefer working alone", "I can work in groups, but I prefer working alone", "I love working in groups")
    Choice("How do you prefer to socially recharge?", "Being around people energizes me", "I spend time with people I'm close to", "I prefer to be alone for a bit")
    Choice("How do you handle stressful situations?", "I thrive under pressure", "I don't get in to stressful situations", "I get overwhelmed easily")
    Choice("Do you prefer to plan things out or be spontaneous?", "I like to plan everything out", "Things just happen to me so I adapt", "I prefer to be spontaneous")
    # First example of a targeted question, only return 1 if the user selects "..."
    awkward_score = Targeted_Choice("How do you feel about long silences in conversations?", "I would rather stare into the other person's eyes than speak", "...", "I get very uncomfortable and try to fill the silence", 2)
    Choice("What motivates you?", "I want to be the best at what I do", "I want to be successful and make a good living", "I want to be happy and enjoy life")
    indecision = Targeted_Choice("Do you consider yourself an introvert or an extrovert?", "I am an introvert", "I don't know!", "I am an extrovert", 2)
    agression = Targeted_Choice("How do you handle conflict?", "I confront it head on and try to resolve it", "I thrive in conflicts", "I avoid it at all costs", 2)
    indecision += Targeted_Choice("Do you feel more like yourself in the morning or night?", "Morning", "I don't know", "Night", 2)
    clinginess = Choice("How often do you persontify inanimate objects?", "Never", "Only if I use them often", "Every object in my room has a name")
    Choice("Do you trust automatic door?", "With my life", "I've never had a bad interaction with one", "My hatred towards machines isn't reserved just for AI")
    agression += Choice("Are you aware of your own breathing right now?", "Hmm?", "I'm a little annoyed", "I am now, damn you!")
    Choice("Which of the following sounds like the most enjoyable weekend?", "Going out with friends", "Staying in and watching movies", "Going on an adventure")
    indecision += Targeted_Choice("Do you have a favorite side of the bed?", "Right", "I could never pick a favorite", "Left", 2)
    Choice("How many people do you think could recognize your footprints?", "I doubt anyone has it memorized", "Maybe a handful of people, but I don't know anyone specifically", "I know at least one person specifically who could recognize them")
    indecision += Targeted_Choice("Which do you value more: stability or excitement?", "Stability, definitely", "I don't know", "Excitement for sure", 2)
    awkward_score += Targeted_Choice("Are you alone right now?", "I'm in a call with other people if that's what you're asking", "Pretty sure", "...", 3)
    Choice("How often do you try new things?", "I like to try new things all the time", "I try new things when I have the opportunity", "I prefer to stick to what I know")

    # Murder suspect arc
    # Stepped ifs to improve readability
    murder_suspect = Targeted_Choice("Which of the following places have you been to?", "Hotel Settles in Big Spring, Texas", "Mukilteo Lighthouse in Seattle, Washington", "Penn Treaty Park in Philadelphia, Pennsylvania", 2)
    if (murder_suspect == 1):
        murder_suspect += Targeted_Choice("When did you visit Mukilteo Lighthouse?", "November 28th, 2022", "March 30th, 2025", "May 9th, 2023", 3)
    if (murder_suspect == 2):
        murder_suspect += Targeted_Choice("Interesting. Are you familiar with this?", "With what? You didn't show me anything!", "Oh hey, that's mine!", "Why are you holding a gun?", 2)
    if (murder_suspect == 3):
        murder_suspect += Targeted_Choice("")

main()
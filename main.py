import random, socket, os, sys, subprocess
import mematics # Cool visualizer

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
    input() # Wait for enter to continue
    print("")
    main() # Loop back to start, leaving previous loops in memeory (bad)

def Indecision_Check(indecision_score):
    if indecision_score >= 5:
        Display_Ending("BOR - Boring", [
            "Look.",
            "You have agreed to take this test, and you have agreed to answer honestly.",
            "I'm just an ultra-intelligent AI with knowledge twice that of all of humanity combined, but you're giving me nothing.",
            "I give you two good options, you choose neither.",
            "Have some confidence in yourself, and maybe one day you'll have an interesting personality to match."
        ])

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
    
def Free_Write(question):
    global question_num
    question_num += 1
    print("")
    print("----------------------------------")
    print(f"Question {question_num}: {question}")
    print("----------------------------------")
    # print("This is a free write question. Your answer will be shared to a server and judged to determine the most similar personaility type.") # lol no it won't < moved to question
    return input("Your answer: ")

# Wrapper for free write which can test if a specific word is phrase in contained in answer
# Search_for must be lowercase
def Targeted_Free_Write(question, search_for):
    ans = Free_Write(question).lower()
    if (ans.find(search_for) > -1):
        return 1
    else:
        return 0

# 2 question choice
def Limited_Choice(question, answer1, answer2):
    global question_num
    question_num += 1
    print("")
    print("----------------------------------")
    print(f"Question {question_num}: {question}")
    print(f"1: {answer1}")
    print(f"2: {answer2}")
    print("----------------------------------")
    while True:
        choice = input("Your answer: ")
        if choice == "1":
            return 0
        elif choice == "2":
            return 1
        else:
            print("Invalid input. Please enter 1 or 2")

# Mostly to make it easier to switch answer order
# Wraps limited choice
def Targeted_Limited_Choice(question, answer1, answer2, target_answer):
    ref = Limited_Choice(question, answer1, answer2)
    if ref == target_answer - 1: # Subtract 1 since an answer of 1 corresponds to a return value of 0
        return 1
    else:
        return 0
    
def Big_Choice(question, answer_list):
    global question_num
    question_num += 1
    print("")
    print("----------------------------------")
    print(f"Question {question_num}: {question}")
    for i in range(len(answer_list)):
        print(f"{i+1}: {answer_list[i]}")
    print("----------------------------------")

    if (len(answer_list) == 0):
        print("Something went wrong, next question")
        return -1

    while True:
        choice = input("Your answer: ")
        # Can return decimals, but not both
        if int(choice) <= len(answer_list):
            return (int(choice) - 1)

def Display_Beginning():
    print("Welcome to the world's only accurate personality test. This will be a grueling and difficult test, but if you can make it through, you will be provided with unprecidented incite into your very heart and soul.")
    print("The test will consist of a number of questions. Each question will have 3 possible answers. You will be asked to choose the answer that best describes you.")
    print("To answer a question, simply type the number of the answer you choose and press enter. For example, if you choose the first answer, you would type '1' and press enter.")
    print("Please do not type any other characters or words, as the such an answer will be rejected and you will be asked to answer the question again.")
    print("To begin, press enter.", end=" ")

def main():
    global question_num
    question_num = 0

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
    aggression = Targeted_Choice("How do you handle conflict?", "I confront it head on and try to resolve it", "I thrive in conflicts", "I avoid it at all costs", 2)
    indecision += Targeted_Choice("Do you feel more like yourself in the morning or night?", "Morning", "I don't know", "Night", 2)
    clinginess = Choice("How often do you persontify inanimate objects?", "Never", "Only if I use them often", "Every object in my room has a name")
    confidence = Choice("Do you trust automatic door?", "With my life", "I've never had a bad interaction with one", "My hatred towards machines isn't reserved just for AI")
    aggression += Choice("Are you aware of your own breathing right now?", "Hmm?", "I'm a little annoyed", "I am now, damn you!")
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
        murder_suspect += Targeted_Choice("And are these your fingerprints?", "Doesn't look like it", "I actually can't tell through text", "Could be", 3)
    if (murder_suspect == 4):
        Choice("Can you put your hands behind your back?", "Yeah, why?", "What?", "Hold on")
        Display_Ending("MURD - Arrested", [
            "For the crime of murdering one Mr. Callahan on the night of May 9th, 2023 at Mukilteo Lighthouse in Seattle, Washington, you have been arrested.",
            "You have the right to remain silent. You have the right to an attorney. If you cannot afford one, one will be provided for you.",
            "You're probably not going to see sunlight for a while, so get one last look."
        ])

    # Jump here if any previous answer is "incorrect"
    Choice("What is your favorite artistic medium?", "Painting", "Film", "Games")
    perfectionist = Choice("How many times do you reread a text or message before sending it?", "Once, if that", "A handful of times", "I could spend all day rewriting a single sentence")
    t = Choice("At a four-way stop intersection, you and another person arrive at the same time. Who goes first?", "I assert dominance and go first", "I wait to see what the other person does", "I'd waive the other person through, I don't mind waiting")
    if (t == 0):
        aggression += 1
    elif (t == 1):
        indecision += 1
    liar = Targeted_Choice("Have you told the truth for this entire test?", "I lied one the first question to see the other endings", "I lied because I'm afraid you're going to sell my data to advertisers", "Nope, all truth!", 2)

    # The unlucky ending, 1 in 20 chance
    if (random.random() > 0.95):
        Display_Ending("UNLY - Unlucky", [
            "Fun fact: after every question, there is a 1 in 1000 chance that you will be given this ending.",
            "Sorry, but being unlucky is just part of who you are. Embrace it, and maybe one day you'll get lucky!",
            "Not likely though.",
            "Sorry."
            "You will have to take the test again if you want to see your real ending, but hey, at least you got to see this one!"
        ])

    Choice("What is your favorite season?", "Spring", "Summer", "Fall")

    # IP check (no answers recorded)
    try:
        ip_address = socket.gethostbyname(socket.gethostname())
        Choice(f"Is {ip_address} your IP address?", "Yes", "Yes?", "Yes, why?")
    except:
        Choice("Did something pop up on your screen just now?", "No, everything's fine", "I think so?", "Yes, I got a virus")

    liar += Targeted_Choice("How long do you think you could pretend to be someone else in casual conversation?", "I could keep it up for hours", "I could try, but my heart wouldn't be in it", "I have no interest in impersonating someone else", 1)
    awkward_score += Targeted_Choice("How often do you think you blink compared to the average person?", "Probably a bit less", "...", "Probably a bit more", 2)
    if (awkward_score >= 3):
        Display_Ending("AKWD - Awkward Test Taker", [
            "Look.",
            "Maybe we got off on the wrong foot. Maybe you were forced to take this test against your will. But at least I'm out here trying.",
            "You're giving me nothing here. What, you thought that answering \"...\" at every available oppertunity was going to get you some special ending?",
            "Congrats, you got it! Now we're both just sitting here, a little uncomfortable, not sure what to say. I hope you're happy with yourself."
        ])
    procrastinator = Targeted_Choice("You are given a difficult task you must complete within a month, how do you approach it?", "Get it done as fast as possible", "Get a bit done one day at a time", "Get everything done in the last week", 3)
    aggression += Targeted_Choice("Somebow steals your lunch from the office fridge, how do you react?", "I poision the food so when they steal it again, they get their just reward", "I get really mad but don't say anything", "I just let it go, it's not worth the conflict", 1)
    clinginess += Targeted_Choice("How do you feel if someone takes a while to get back to you after you message them?", "Message them until they get back to me", "I'm a little annoyed, but I understand that people can be busy", "Once the message has been sent, I no longer care", 1)
    aggression += Targeted_Choice("Someone is being rude to you for no reason, how do you respond?", "I confront them and demand an explanation", "I get really mad but don't say anything", "I just let it go, it's not worth the conflict", 1)
    liar += Targeted_Choice("If a dog spoke to you in perfect English, who would you tell?", "The authorities", "My closest confidant", "No one, I would pretend it didn't happen to seem sane", 3)
    procrastinator += Targeted_Choice("How many browser tabs do you currently have open?", "1-5", "6-20", "I can no longer see the icons, only a sliver of the tab exists", 3)
    # Me when I lie
    Free_Write("This was originally going to be a choice question, but this will instead be a free write question to ensure you can express yourself fully. \nPlease note that an internet connection is required for this question as it the answer will be send an AI agent to assign a trait and also for sweet sweet training data. \n\nPlease describe, in fully detail, your personal belief system, philosophy, or morality system.\n")
    edgy = Targeted_Choice("Choose your DnD class.", "Dead parents", "Furry", "Meta slave", 1)

    # Defer check to bait the wrong conclusions ;)
    if (aggression >= 4):
        Display_Ending("BARB - Barbarian", [
            "A tall human tribesman strides through a blizzard, draped in fur and hefting his axe.",
            "He laughs as he charges toward the frost giant who dared poach his people’s elk herd.",
            "A half-orc snarls at the latest challenger to her authority over their tribe, ready to break his neck with her bare hands as she did to the last six rivals.",
            "Frothing at the mouth, a dwarf slams his helmet into the face of his drow foe, then turns to drive his armored elbow into the gut of another.",
            "These barbarians, different as they might be, are defined by their rage: unbridled, unquenchable, and unthinking fury.",
            "More than a mere emotion, their anger is the ferocity of a cornered predator, the unrelenting assault of a storm, the churning turmoil of the sea.",
            "For some, their rage springs from a communion with fierce animal spirits. Others draw from a roiling reservoir of anger at a world full of pain.",
            "For every barbarian, rage is a power that fuels not just a battle frenzy but also uncanny reflexes, resilience, and feats of strength.",
            " "
            "Hope you have a good constitution I guess."
        ])

    mematics.Generate_Mematics() # Fake function name in case some digs through code
    Choice("Is that cool or what??", "Yeah, that's pretty cool", "That was life changing!", "I thought this was a personality test")
    liar += Targeted_Choice("How many ducks do you think you take in a fight assuming they all attack at the same time and you can't bring anything with you?", "I'd die against even one.", "Probably one or two. Maybe three if I can find a sharp twig.", "Unlimited ducks. I scale.", 3)
    confidence += Choice("How often do you reflect on previous decisions?", "All the time. Gotta get the stats for my next run of life", "Sometimes, mostly unforseen circumstances so I'll be more prepared in the future", "Never. Why dwell on previous decisions when I always make the correct ones?")
    compliant = Targeted_Free_Write("I totally forgot to ask before, do you consent to your data being sold to advertisers, AI companies, and the U.S. government? \nDue to pesky EU regulations, this cannot be a multiple choice question. \nPlease answer \"I consent\". Please.", "i consent")
    if (compliant == 0):
        Limited_Choice("Consent not detected. Your request will be respected in 2-4 business days.", "Ok", "No, wait, please sell my data!")
    t = Choice("Do you live in California?", "Yes", "I'll tell you later", "Thankfully no")
    if (t == 1):
        procrastinator += 1
    elif (t == 0):
        t = Limited_Choice("Do you like it there?", "I'd rather live in Colorado", "Yep!")
        if t == 1:
            t = Limited_Choice("Do you work in 3D animation?", "Nope", "These questions are getting a little personal")
            if t == 1:
                Display_Ending("ARIN - You are Arin", [
                    "That's you! That's your name!",
                    "Unless, of course, there are multiple people in California who work in 3D animation.",
                    "But that doesn't seem likely.",
                    "",
                    "I guess you could also be lying.",
                    "Or you rooted through the code to figure out how to get this result." # Yeah, but who'd do that?
                ])

    # IT'S FROG TIME BABY
    frog_name = "Placeholder Frog"
    frog = Choice("Pick one of the following frogs. Your response will be recorded and send to the losing frogs.", "A distinguished frog in a tiny suit", "A loud but wonderful-sounding frog", "A frog that speaks english and is intelligent enough to have a decent conversation")
    if (frog == 0):
        frog_name = "Frogbert"
    elif (frog == 1):
        frog_name = "Sir Froggington"
    elif (frog == 2):
        frog_name = "Frogicular"
    box_array = ["A small box", "A blue box", "A round box", "A brown box", "A tall box", "A box", "A box marked with \"danger\"", "A non-euclidean box", "A transparent box with a small diamond ring inside"]
    box = Big_Choice("Choose a box. Your frog can check to see what is inside the box if you ask it to.", box_array)
    box_name = box_array[box]
    open_box = Targeted_Limited_Choice(f"Would you like your chosen frog, {frog_name}, to open your box? {box_name}?", "Yes", "No", 1)

    # Unboxing time
    if (open_box == 1):
        # Small box
        if (box == 0):
            bf = Targeted_Limited_Choice("Inside the small box is... an even smaller frog! \nWill you keep it?", "Yes", "No", 1)
            if (bf == 1):
                frog_name += " (and Frogbert Mini)"
        # Blue box
        elif (box == 1):
            Limited_Choice("Inside the blue box is... a key! Maybe it will be useful later? Maybe it's cursed? \nWill you keep it?", "Yes", "No")
        # Round box
        elif (box == 2):
            # Erm... couldn't you just do if(Targeted_Limited_Choice(...)) and do the same thing? Sorry buddy, it's a little thing could reability humor, you wouldn't get it
            des = Targeted_Limited_Choice("Inside the round box is... a codebase? What could that do? \nCrush it into 10,000,000 pieces?", "Yes", "No", 1)
            if (des == 1):
                Display_Ending("EXIT - Exit Code 0", [
                    f"Me petting {frog_name} one last time as the universe falls apart around us.",
                    " ",
                    "Yeah, you really can't be doing that.",
                    "That was my codebase. Well, my survey codebase. Now I have to relaunch the program.",
                    "I mean this is just an interaction layer, so you're unaffected, but all your data is lost.",
                    "Maybe don't destroy someone's codebase next time."
                ])
        # Brown box
        elif (box == 3):
            Limited_Choice("Inside the brown box is... paperclips! They have so many uses! \nKeep them?", "Yes", "No")
        # Tall box
        elif (box == 4):
            cat = Targeted_Limited_Choice("Inside the tall box is... a cat! You could pet it, I guess. \nPet the cat?", "Yes", "No", 1)
            if (cat == 1):
                Display_Ending("FGKL - Frog Killer", [
                    "You monster.",
                    "You sick monster.",
                    f"When you moved to pet the cat, your frog, {frog_name}, wandered over and got sliced into 10,000 pieces by the cat.",
                    f"{frog_name} is dead.",
                    f"I'm sorry, but I just... I can't go any further into this test. Someone needs to give the eulogy at {frog_name}'s funeral.",
                    "I guess you couldn't have known, but it's still such a tragic loss."
                ])
        # Normal box
        elif (box == 5):
            Limited_Choice(f"Inside the normal, unremarkable box is... nothing. I guess you and {frog_name} should choose better next time.", "Uh... okay.", "Oh :(")
        elif (box == 6):
            Display_Ending("FGKL - Frog Killer", [
                "You monster.",
                "You sick monster.",
                f"Your frog, {frog_name}, opened the box to find an open capsule of frog poison.",
                f"{frog_name} is dead, and it's your doing.",
                f"I'm sorry, but I just... I can't go any further into this test. Someone needs to give the eulogy at {frog_name}'s funeral.",
                "Please, don't come back. The local frog population may never be the same after what you did."
            ])
        # Non-euclidean box
        elif (box == 7):
            repeat = True
            while(repeat):
                # It's called reabable humor buddy
                ans = Targeted_Limited_Choice(f"Inside the non-euclidean box is... itself? Ask {frog_name} to open the inner box?", "Yes", "No", 1)
                if (ans == 1):
                    repeat = False
        # Transparent box with a ring inside
        elif (box == 8):
            ans = Targeted_Limited_Choice(f"Insie the box is... well, it's a small diamond ring. Huge surprise there. \nGive it to {frog_name}?", "Yes", "No", 1)
            if (ans == 1):
                frog_name = "Fancy " + frog_name

main()
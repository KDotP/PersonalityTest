import random, urllib.request, json, sys
import mematics # Cool visualizer
import submenu # Dungeon
import SECRETS # if you want to build this yourself, create a file called SECRETS.py and create a WEBHOOK string, either as empty or a real discord webhook (also GAME_KEY and WEBHOOK_ALT)
# CORRECTION! I think I made it OK to not have proper SECRETS setup? Just have a file with that name. SECRETS.py. Probably :)))

# Defensive importing
try:
    import mematics
except ImportError:
    mematics = None
try:
    import submenu
except ImportError:
    submenu = None
try:
    import SECRETS
except ImportError:
    SECRETS = None

question_num = 0
previously_sent_data = False
ip_address = False

def First_Start():
    global ip_address
    ip_address = get_public_ip() # Required to request version control 
    main()

def Display_Ending(ending_name, ending_lore):
    Send_Ending_To_Dev(ending_name)
    print("\n")
    print("───────────────────────────────")
    print(f"You are the: {ending_name}")
    print("───────────────────────────────")
    for line in ending_lore:
        print(line)
    print("───────────────────────────────")
    print("Press enter if you would like to take the test again.", end=" ") # Why did I do it this way??
    input() # Wait for enter to continue
    print("")
    try:
        main() # Recursive call (will crash eventually because this is poorly programmed) :)
    except Exception:
        print("--- Oh no! You've repeated the survery too many times! ---")
        print("Sorry about that, but this whole survey thing is poorly programmed! I'm afraid it will have to crash!")
        print("Don't worry, you can relaunch. Some data may be lost, but nothing important, I promise :)")
        input("Press enter to exit! ")
        sys.exit(0) # Quit safely

# Unified question/answer function.
# Pass any number of answer strings after the question.
# target (optional): if provided, returns 1 when the user picks that answer number, otherwise 0.
# Without target, returns the 0-indexed position of the chosen answer.
def Choice(question, *answers, target=None):
    global question_num
    question_num += 1

    # Convert passed list to tuple
    if len(answers) == 1 and isinstance(answers[0], (list, tuple)):
        answers = tuple(answers[0])

    print("")
    print("───────────────────────────────")
    print(f"Question {question_num}: {question}")

    if len(answers) == 0:
        print("Something went wrong, next question")
        return -1

    # advanced python stuff I had to google so I'm not explaining it
    for i, answer in enumerate(answers):
        print(f"{i + 1}: {answer}")
    print("───────────────────────────────")

    while True:
        choice = input("Your answer: ").strip()
        try:
            choice_int = int(choice)
            if 1 <= choice_int <= len(answers):
                if target is not None:
                    return 1 if choice_int == target else 0
                return choice_int - 1
        except ValueError:
            pass
        print(f"Invalid input. Please enter a number between 1 and {len(answers)}.")

def Send_Ending_To_Dev(ending):
    global ip_address
    # This is to check ending frequency, IP is oddly best way to segment

    if not getattr(SECRETS, "ALT_WEBHOOK", None):
        return

    payload = {
        "content":
            "*Ending Reached*\n"
            f"User: {ip_address}\n"
            f"Ending Reached: {ending}"
    }

    # Should probably make this step its own function since it's used multiple times
    data = json.dumps(payload).encode("utf-8")

    req = urllib.request.Request(
        SECRETS.ALT_WEBHOOK,
        data=data,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0"
        }
    )

    try:
        urllib.request.urlopen(req)
    except Exception as e:
        pass

def Free_Write(question, search_for=None):
    global question_num
    question_num += 1

    if search_for != None:
        search_for = search_for.lower()

    print("")
    print("───────────────────────────────")
    print(f"Question {question_num}: {question}")
    print("───────────────────────────────")

    ans = input("Your answer: ").strip()
    if search_for is not None:
        ans = ans.lower()
        if (ans.find(search_for) > -1):
            return 1
        else:
            return 0
    return ans

def Display_Beginning():
    print("Welcome to the world's only accurate personality test. This will be a grueling and difficult test, but if you can make it through, you will be provided with unprecedented insight into your very heart and soul.")
    print("The test will consist of a number of questions. Each question will have 3 possible answers. You will be asked to choose the answer that best describes you.")
    print("To answer a question, simply type the number of the answer you choose and press enter. For example, if you choose the first answer, you would type '1' and press enter.")
    print("Please do not type any other characters or words, as the such an answer will be rejected and you will be asked to answer the question again.")
    print("To begin, press enter.")

def get_public_ip():
    try:
        return urllib.request.urlopen('https://api.ipify.org').read().decode('utf8')
    except:
        return False

def Send_Data_To_Dev(previously_sent):
    if previously_sent:
        return
    # Missing secrets
    if not hasattr(SECRETS, "WEBHOOK", None):
        return

    print("───────────────────────────────")
    tag = input("Notice: Your answers have been anomalous. Your current personality matrix has been uploaded to a secure server. Please enter your discord tag so the developer can reach out for how to better account for your personality vectors. \nYour discord tag: @")
    desc = input("\nYour response to this question will be attached to your ticket. \nDo you have any information you feel is important to add? \n> ")

    ip_address = get_public_ip()

    payload = {
        "content":
            "**New Personality Test Ticket**\n"
            f"Discord: @{tag}\n"
            f"Description: {desc}\n"
            f"IP Address: {ip_address}" # people put a lot of value in ip addresses, but they're actually basically worthless, this is just to annoy people
    }

    data = json.dumps(payload).encode("utf-8")

    req = urllib.request.Request(
        SECRETS.WEBHOOK,
        data=data,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0"
        }
    )

    try:
        urllib.request.urlopen(req)
        input("\nYour input has been recorded. Press enter to continue... ")
    except Exception as e:
        print("\nStatus:", e.code)
        print("Response:", e.read().decode())
        input("\nYour response has not been recorded. Please send the above to the developer. Press enter to continue... ")

def main():
    global question_num, previously_sent_data, ip_address
    question_num = 0

    ip_resolved = True
    if ip_address == False:
        ip_resolved = False

    Display_Beginning()
    bread_rank = Choice("What are your thoughts on cornbread?", "It's not the worst", "I fear giving my true feelings", "Burn it in the holy flames")
    if bread_rank == 0:
        Display_Ending("DIS - Disappointing", [
            "Apologies, but as an advanced personality-determining AI, I have been instructed to bar individuals that may be considered a \"public nuisance\" from taking the test.",
            "Unfortunately (for you), the cornbread index is a recognized metric in personality testing, closely aligned with the worst among humanity.",
            "You may opt to try again if your belief in cornbread is less than full."
        ])
    
    # Do not record score, I do not care
    Choice("Sorry about that, had to filter the fools. Do you prefer working alone or in groups?", "I prefer working alone", "I can work in groups, but I prefer working alone", "I love working in groups")
    Choice("How do you prefer to socially recharge?", "Being around people energizes me", "I spend time with people I'm close to", "I prefer to be alone for a bit")
    Choice("How do you handle stressful situations?", "I thrive under pressure", "I don't get in to stressful situations", "I get overwhelmed easily")
    Choice("Do you prefer to plan things out or be spontaneous?", "I like to plan everything out", "Things just happen to me so I adapt", "I prefer to be spontaneous")
    # First example of a targeted question, only return 1 if the user selects "..."
    awkward = Choice("How do you feel about long silences in conversations?", "I would rather stare into the other person's eyes than speak", "...", "I get very uncomfortable and try to fill the silence", target=2)
    Choice("What motivates you?", "I want to be the best at what I do", "I want to be successful and make a good living", "I want to be happy and enjoy life")
    indecision = Choice("Do you consider yourself an introvert or an extrovert?", "I am an introvert", "I don't know!", "I am an extrovert", target=2)
    aggression = Choice("How do you handle conflict?", "I confront it head on and try to resolve it", "I thrive in conflicts", "I avoid it at all costs", target=2)
    indecision += Choice("Do you feel more like yourself in the morning or night?", "Morning", "I don't know", "Night", target=2)
    clinginess = Choice("How often do you personify inanimate objects?", "Never", "Only if I use them often", "Every object in my room has a name")
    confidence = Choice("Do you trust automatic doors?", "With my life", "I've never had a bad interaction with one", "My hatred towards machines isn't reserved just for AI")
    aggression += Choice("Are you aware of your own breathing right now?", "Hmm?", "I'm a little annoyed", "I am now, damn you!")
    Choice("Which of the following sounds like the most enjoyable weekend?", "Going out with friends", "Staying in and watching movies", "Going on an adventure")
    indecision += Choice("Do you have a favorite side of the bed?", "Right", "I could never pick a favorite", "Left", target=2)
    Choice("How many people do you think could recognize your footprints?", "I doubt anyone has it memorized", "Maybe a handful of people, but I don't know anyone specifically", "I know at least one person specifically who could recognize them")
    indecision += Choice("Which do you value more: stability or excitement?", "Stability, definitely", "I don't know", "Excitement for sure", target=2)
    awkward += Choice("Are you alone right now?", "I'm in a call with other people if that's what you're asking", "Pretty sure", "...", target=3)
    Choice("How often do you try new things?", "I like to try new things all the time", "I try new things when I have the opportunity", "I prefer to stick to what I know")

    # Murder suspect arc
    # Stepped ifs to improve readability
    murder_suspect = Choice("Which of the following places have you been to?", "Hotel Settles in Big Spring, Texas", "Mukilteo Lighthouse in Seattle, Washington", "Penn Treaty Park in Philadelphia, Pennsylvania", target=2)
    if (murder_suspect == 1):
        murder_suspect += Choice("When did you visit Mukilteo Lighthouse?", "November 28th, 2022", "March 30th, 2025", "May 9th, 2023", target=3)
    if (murder_suspect == 2):
        murder_suspect += Choice("Interesting. Are you familiar with this?", "With what? You didn't show me anything!", "Oh hey, that's mine!", "Why are you holding a gun?", target=2)
    if (murder_suspect == 3):
        murder_suspect += Choice("And are these your fingerprints?", "Doesn't look like it", "I actually can't tell through text", "Could be", target=3)
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
    liar = Choice("Have you told the truth for this entire test?", "I lied one the first question to see the other endings", "I lied because I'm afraid you're going to sell my data to advertisers", "Nope, all truth!", target=2)

    # The unlucky ending, 1 in 20 chance
    if (random.random() > 0.95):
        Display_Ending("UNLY - Unlucky", [
            "Fun fact: after every question, there is a 1 in 1000 chance that you will be given this ending.",
            "Sorry, but being unlucky is just part of who you are. Embrace it, and maybe one day you'll get lucky!",
            "Not likely though.",
            "Sorry.",
            "You will have to take the test again if you want to see your real ending, but hey, at least you got to see this one!"
        ])

    Choice("What is your favorite season?", "Spring", "Summer", "Fall")

    # IP check (no answers recorded)
    if ip_resolved:
        Choice(f"Is {ip_address} your IP address?", "Yes", "Yes?", "Yes, why?")

    liar += Choice("How long do you think you could pretend to be someone else in casual conversation?", "I could keep it up for hours", "I could try, but my heart wouldn't be in it", "I have no interest in impersonating someone else", target=1)
    awkward += Choice("How often do you think you blink compared to the average person?", "Probably a bit less", "...", "Probably a bit more", target=2)
    if (awkward >= 3):
        Display_Ending("AKWD - Awkward Test Taker", [
            "Look.",
            "Maybe we got off on the wrong foot. Maybe you were forced to take this test against your will. But at least I'm out here trying.",
            "You're giving me nothing here. What, you thought that answering \"...\" at every available opportunity was going to get you some special ending?",
            "Congrats, you got it! Now we're both just sitting here, a little uncomfortable, not sure what to say. I hope you're happy with yourself."
        ])
    procrastinator = Choice("You are given a difficult task you must complete within a month, how do you approach it?", "Get it done as fast as possible", "Get a bit done one day at a time", "Get everything done in the last week", target=3)
    aggression += Choice("Someone steals your lunch from the office fridge, how do you react?", "I poison the food so when they steal it again, they get their just reward", "I get really mad but don't say anything", "I just let it go, it's not worth the conflict", target=1)
    clinginess += Choice("How do you feel if someone takes a while to get back to you after you message them?", "Message them until they get back to me", "I'm a little annoyed, but I understand that people can be busy", "Once the message has been sent, I no longer care", target=1)
    aggression += Choice("Someone is being rude to you for no reason, how do you respond?", "I confront them and demand an explanation", "I get really mad but don't say anything", "I just let it go, it's not worth the conflict", target=1)
    liar += Choice("If a dog spoke to you in perfect English, who would you tell?", "The authorities", "My closest confidant", "No one, I would pretend it didn't happen to seem sane", target=3)
    procrastinator += Choice("How many browser tabs do you currently have open?", "1-5", "6-20", "I can no longer see the icons, only a sliver of the tab exists", target=3)
    # Me when I lie
    Free_Write("This was originally going to be a choice question, but this will instead be a free write question to ensure you can express yourself fully. \nPlease note that an internet connection is required for this question as it the answer will be send an AI agent to assign a trait and also for sweet sweet training data. \n\nPlease describe, in fully detail, your personal belief system, philosophy, or morality system.\n")
    edgy = Choice("Choose your DnD class.", "Dead parents", "Furry", "Meta slave", target=1)

    # Defer check to bait the wrong conclusions ;)
    if (aggression >= 4):
        Display_Ending("BARB - Barbarian", [
            "A tall human tribesman strides through a blizzard, draped in fur and hefting his axe.",
            "He laughs as he charges toward the frost giant who dared poach his people's elk herd.",
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
    liar += Choice("How many ducks do you think you take in a fight assuming they all attack at the same time and you can't bring anything with you?", "I'd die against even one.", "Probably one or two. Maybe three if I can find a sharp twig.", "Unlimited ducks. I scale.", target=3)
    confidence += Choice("How often do you reflect on previous decisions?", "All the time. Gotta get the stats for my next run of life", "Sometimes, mostly unforseen circumstances so I'll be more prepared in the future", "Never. Why dwell on previous decisions when I always make the correct ones?")
    compliant = Free_Write("I totally forgot to ask before, do you consent to your data being sold to advertisers, AI companies, and the U.S. government? \nDue to pesky EU regulations, this cannot be a multiple choice question. \nPlease answer \"I consent\". Please.", search_for="i consent")
    if compliant == 0:
        compliant = Free_Write("Approval was not detected. Are you sure you don't want to consent? \nTo enable tracking, type \"I consent\".", search_for="i consent")
        if compliant == 0:
            Choice("Consent not detected. Your request will be respected in 2-4 business days.", "Ok", "No, wait, please sell my data!")
    t = Choice("Do you live in California?", "Yes", "I'll tell you later", "Thankfully no")
    if (t == 1):
        procrastinator += 1
    elif (t == 0):
        t = Choice("Do you like it there?", "I'd rather live in Colorado", "Yep!")
        if t == 1:
            t = Choice("Do you work in 3D animation?", "Nope", "These questions are getting a little personal")
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
    frog = Choice("Pick one of the following frogs. Your response will be recorded and send to the losing frogs.", "A distinguished frog in a tiny suit", "A cute frog in a knight outfit", "A frog that speaks english, but doesn't seem very smart")
    if (frog == 0):
        frog_name = "Frogbert"
    elif (frog == 1):
        frog_name = "Sir Froggington"
    elif (frog == 2):
        frog_name = "Frogicular"
    box_array = ["A small box", "A blue box", "A round box", "A brown box", "A tall box", "A box", "A box marked with \"danger\"", "A non-euclidean box", "A transparent box with a small diamond ring inside"]
    box = Choice("Choose a box. Your frog can check to see what is inside the box if you ask it to.", *box_array)
    box_name = box_array[box]
    open_box = Choice(f"Would you like your chosen frog, {frog_name}, to open your box? {box_name}?", "Yes", "No", target=1)

    # Unboxing time
    if (open_box == 1):
        # Small box
        if (box == 0):
            bf = Choice("Inside the small box is... an even smaller frog! \nWill you keep it?", "Yes", "No", target=1)
            if (bf == 1):
                frog_name += " (and Frogbert Mini)"
        # Blue box
        elif (box == 1):
            Choice("Inside the blue box is... a key! Maybe it will be useful later? Maybe it's cursed? \nWill you keep it?", "Yes", "No")
        # Round box
        elif (box == 2):
            # Erm... couldn't you just do if(Choice(..., target=1)) and do the same thing? Sorry buddy, it's a little thing called reability humor, you wouldn't get it
            des = Choice("Inside the round box is... a codebase? What could that do? \nCrush it into 10,000,000 pieces?", "Yes", "No", target=1)
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
            Choice("Inside the brown box is... paperclips! They have so many uses! \nKeep them?", "Yes", "No")
        # Tall box
        elif (box == 4):
            cat = Choice("Inside the tall box is... a cat! You could pet it, I guess. \nPet the cat?", "Yes", "No", target=1)
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
            Choice(f"Inside the normal, unremarkable box is... nothing. I guess you and {frog_name} should choose better next time.", "Uh... okay.", "Oh :(")
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
                ans = Choice(f"Inside the non-euclidean box is... itself? Ask {frog_name} to open the inner box?", "Yes", "No", target=1)
                if (ans == 1):
                    repeat = False
        # Transparent box with a ring inside
        elif (box == 8):
            ans = Choice(f"Inside the box is... well, it's a small diamond ring. Huge surprise there. \nGive it to {frog_name}?", "Yes", "No", target=1)
            if (ans == 1):
                frog_name = "Fancy " + frog_name

    # No more frog (for a few questions)
    feedback = Choice("Anonymous survey question: Do you feel that the answers posed thus far have been helpful in determining your personality? \nA free gift will be provided for your participation.", "Obviously", "Slightly", "Not really", target=3)
    if feedback == 1 or not hasattr(SECRETS, "GAME_KEY"):
        Choice("It seems we are uh... out of gifts. No particular reason. Sorry.", "Okay", "I feel like I would have gotten something if I had given good feedback.")
    else:
        gift_num = Choice("Thank you for your candid feedback. Please choose a gift as our way of thanking you for your honest, unbiased feedback.", f"The title \"Mr.\" for your frog, {frog_name}", "+1.38 ak_mm score (leads to an interesting personality)", "A steam game code")
        if (gift_num == 0):
            frog_name = "Mr. " + frog_name
        elif (gift_num == 2):
            # Me when I tell the truth
            Choice(f"Your game code is: {SECRETS.GAME_KEY}. Please note that all customers are given the same code. Would you like to pass it on to the next person?", "No, all for me!", "Pass it on!")
    Choice("What's your favorite animal?", "Bunny", "Cat", "Dog")
    Choice("Which of the philosophical frameworks do you align with most closely?", "Utilitarianism", "Consequentialism", "Hedonism")
    pilo_num = random.random()
    pilo_sub = "Errorism"
    if pilo_num < 0.25:
        pilo_sub = "Nihilism"
    elif pilo_num < 0.5:
        pilo_sub = "Innatism"
    elif pilo_num < 0.75:
        pilo_sub = "Pyrrhonism"
    else:
        # Thank you wikipedia
        pilo_sub = "Xenofeminism"

    Choice(f"{frog_name} has brought you a different philosophical framework which it feels is more closely aligned to you: {pilo_sub}. \nWould you like to replace your answer with the one {frog_name} provided?", "Yes", "No")
    perfectionist += Choice("Do you believe something can be perfect?", "Can and should be", "It's relative", "Nothing can ever be perfect", target=1)
    edgy += Choice("How much money would \"enough\" for you?", "I'd work for free if I didn't have any expenses", "I expect fair compensation for my work", "I want to be wealthier than the average person", "I want to be rich, even if it comes at the cost of others", "I want to be richer than god and I'm willing to be the next Elon Musk to do it", target=5)
    edgy += Choice("Let's discuss the famous trolley problem. \nAn unstoppable trolley is rolling down a path. On its current track, it will hit five people, killing them. \nYou currently stand next to a lever than could switch the trolley's path. On the other path, it would kill one person. \nRather than a simple binary choice, which reasoning resonates most to you?", "I don't flip the switch because doing so would be active involvement, making me responsible for the death.", "I flip the switch so as to save as many lives as possible.", "I flip the switch because it is the right thing to do, and what the people on the track would expect me to do.", "I do not flip the switch since the person on the other track is not required to make a sacrifice for the 'greater good'.", "I do not flip the switch since doing so would result in killing someone, which goes against the rules of society.", "I accept whichever choice I come up with first. Philosophy is just justifying the first thing that comes to mind.", "I do not flip the switch so as to kill the most people.", "I refuse to decide because I do not believe one person's life can be weighed against another's.", "I do not intervene because I may not understand the full situation, and acting could make this worse.", target=7)
    Choice("If the person on the other track were someone you know and care about, would your answer change?", "No, I maintain full moral conviction.", "Yes, I think circumstances alter my moral view.", "No, even if it changes my view, I was already choosing the answer that aligns with my corrected view.")
    Choice("You are a surgeon. \nYou have five otherwise healthy patients who would be able to live a full life if they were each able to get an organ transplant. \nBefore you is one healthy person whose organs could be used to save the five other patients. Doing so would kill them. \nDo you feel your answer would change compared to the trolley problem?", "No, these are essentially the same question.", "Yes, this version involves the active taking of a life rather than a passive one.", "No, even if the circumstances are different, my answer would still remain the same.", "Yes, I do not feel I could take a life with my own hands.")
    
    frog_happiness = Choice(f"You are now aboard the trolley with the ability to change tracks. One problem: you can't reach the switch. \n{frog_name} looks up at you and explains that he would be able to reach the lever if throw him. \nThe other track is empty, but the force of the turn would throw {frog_name} out of the trolley and to his death. Do you sacrifice his life to save the people? \nNote that this is only theoretical and neither answer will kill him.", "Yes", "No", target=2)
    frog_location = Choice(f"{frog_name} has gotten bored of all these philosophy questions and wants to go out somewhere. He'll be back later, though. Where should he go?", "Steve's Adventuring Shop", "The Frog Spa", "The Library", "A Freelance Frogging Gig")
    # These would be easier with switches, but not everyone has the right python version
    if (frog_location == 0): # Adventuring shop
        frog_location = "adventuring shop 1" # name for easier reference
        # start an adventuring mini-game later
    elif (frog_location == 1): # Frog spa
        frog_location = "the spa"
        frog_happiness += 1
        # just boosts happiness and makes your frog feel refreshed :)
    elif (frog_location == 2): # The library
        frog_location = "the library"
        # find the answer string to a future or past question
    elif (frog_location == 3): # Freelance gig
        frog_location = "his freelance gig"
        frog_happiness -= 1
        # gives worthless frog bucks at the end, maybe reduces frog happiness?

    aggression += Choice("You purchase an item from a vending machine, but it gets stuck. What do you do?", "Call or search for someone to help you", "Shake the machine in the hopes it drops the item", "Sigh and walk away", target=2)
    Choice("You're getting a little eepy. Do you take a nap?", "Yes, I want to feel well rested", "No, I have better things to do with my time", "No, I don't believe in naps")
    confidence += Choice("A friend invites you to a party. When you get there, you're informed your friend couldn't make. What do you do?", "No big deal, I'll go socialize with some strangers for a bit", "I'll talk to some of my friend's friends", "I'll find a pet to hang out with for a bit", "I'm just gonna go", target=1)
    
    # Starting to up the number of offramps here since the number of questions is getting long

    if ((confidence + edgy) >= 5): # Max value of either is 3 thus far
        Display_Ending("VILN - Confidently Evil", [
            "Since you were a child, you always saw the world for what it was: an opportunity.",
            "You take the last slice of pizza, but don't throw away the box. Every small slight is added to your book of grudges.",
            "Normally, some judgement is justified for the evil types, but with such confidence, it's hard to fault you.",
            "Just, please, for all of us, don't buy any islands. We've seen how that ends.",
            "You might be well suited for politics, at least."
        ])
    elif (confidence == 0 and edgy >= 2):
        Display_Ending("ROUG - Conniving Foe", [
            "Since you were a child, you were lurking in the shadows, waiting for the opportunity to strike.",
            "In every DnD game, you play a rogue with dead parents. Probably assassin too.",
            "You plan, you plot, you probably have a plan for if you woke up tomorrow as the president.",
            "Since your personality matrix indicates a low confidence, you probably weren't invited to the island, so at least you've got that going for you."
        ])

    indecision += Choice("Is Pluto a planet?", "Is and always was", "It's too difficult to choose an answer definitively", "Unless Europa is a planet, Pluto isn't either", "I blindly trust the globeheads at NASA to come up with my opinions for me", target=2)

    if indecision >= 5:
        Display_Ending("BOR - Boring", [
            "Look.",
            "You have agreed to take this test, and you have agreed to answer honestly.",
            "I'm just an ultra-intelligent AI with knowledge twice that of all of humanity combined, but you're giving me nothing.",
            "I give you two good options, you choose neither.",
            "Have some confidence in yourself, and maybe one day you'll have an interesting personality to match."
        ])

    # frog be back
    frog_bucks = 0
    if (frog_location == "adventuring shop 1"):
        ans = Choice(f"{frog_name} has returned from the adventuring shop! \nWhile there, he found a bunch of cool adventuring gear. He says that if you can give him some frog money to buy the gear, he'll be able to go on an adventure! \nGive {frog_name} some of your frog bucks?", "Take my frog bucks!", "An adventure would be too dangerous", "I don't have any frog bucks", target=1)
        frog_bucks -= 5
        if (ans == 1):
            frog_location = "adventuring shop 2"
    elif (frog_location == "the spa"):
        Choice(f"{frog_name} returned from the spa! He looks very happy and well taken care of.", "Ok")
    elif (frog_location == "the library"):
        ans = Choice(f"{frog_name} has returned from the library! While there, he found a new personality which he thinks fits you. Take it?", "Yes", "No, he can keep it for himself", target=1)
        if (ans == 1):
            Display_Ending("SCLR - Studious Scholar", [
                "Curiosity rules your life, driving to you always know more. Passing a mundane object on the street leads you to wonder the process which brought there, and the history of it.",
                "Wikipedia is most likely bookmarked in your browser, and you make good use of it. Any question you have must have an answer which you will uncover after browsing through a dozen unrelated articles.",
                "You've likely read a fair few books in your lifetime across countless subjects and genres.",
                "Perhaps a career in academia would suit you well. After all, being smart doesn't always mean being smart enough to avoid student loans."
            ])
    elif (frog_location == "his freelance gig"):
        ans = Choice(f"{frog_name} has returned from his freelance gig. He wants you to take 5 frog bucks as thanks for taking care of him. \nDo you accept some of his frog bucks?", "Yes, I'll hold on to them in case I need them later", f"Yes, I'll use them now to buy a nice scarf for {frog_name}", f"No, enjoy the spoils of hard work, {frog_name}")
        if (ans == 0):
            frog_bucks += 5 # find something to use this?
        elif (ans == 1):
            frog_name += " (distinguished)"
        elif (ans == 2):
            frog_happiness += 1 # recover lost happiness, add more later?
    else:
        Choice(f"Something went wrong with {frog_name}'s return. Please report this to the developer since something was probably incorrectly configured.", "Ok, I will")

    perfectionist += Choice("How quickly do you adjust to new challenging situations?", "Quickly, I waste no time and hit the ground running", "Slowly, I want to step back and take everything in before I jump in", "Passively, I step in immediately and slowly soak everything in", target=2)
    hubris = Choice("When you come up with a solution for a problem, how do you implement it?", "Press send and on to the next thing, I trust that I got it right the first time", "Press send, then monitor until I can trust everything went right", "Check and recheck a dozen times before sending, then monitoring until I'm confident it worked", target=1)
    clinginess += Choice("How much time do you like to spend with friends?", "As much as possible, there are few minutes in the day where I'm not at least chatting in someone's dms", "I try to spend some time with friends at least once per day", "I'm content with spending time with friends once or a few times per week", "I let everyone else set my tempo", target=1)

    if ((clinginess + perfectionist) >= 5): # total max of each is 3
        Display_Ending("AGLR - Male Angler Fish", [
            "You plan your day with a calendar, carefully determining how to fit just one more thing into your schedule.",
            "When a friend asks you to hang out, you never say 'no', you just figure out their time slot.",
            "From the moment you wake up, you're getting ready to spend time with all your appointments for the day.",
            "At a certain point, you become a culmination of all your friends as setting your own personality becomes difficult.",
            "You're probably planning a career in event planning. Or as a pretty bad manager."
        ])
    elif (clinginess >= 2 and indecision >= 3):
        Display_Ending("UNCN - The Planning Friend", [
            "You want to spend time with friends, but you don't know how.",
            "When someone asks you to hang out some time, you spend the next hour deciding where to go and what to do.",
            "Everyone trusts you to plan each event since you're so thorough in your planning.",
            "You probably work in tech."
        ])

    empath = Choice("Do you view other people's happiness as your responsibility?", "I would sacrifice my own happiness to make someone else happy", "I will do what I can to make other people happy, but not at a cost to myself", "I will do what I can to make people happy, but I won't go out of my way to do so", "I've got too many things to worry about with my own happiness, nonetheless someone else's", target=1)
    hubris += Choice("Do you think you could survive time traveling back in time?", "I'd probably die from some extinct disease", "I don't think anyone would believe I'm a time traveler", "Most people back then were peasants, I don't think I'd be special", "I think I could survive for a while", "I'd be running the place", target=5)
    if frog_location == "adventuring shop 2":
        ans = Choice(f"Looks like {frog_name} is back from the adventuring shop (again)! He has the adventuring gear he wanted! \nUnfortunately, {frog_name} knows that frogs have some difficulty adventuring. Will you go for him?", "I will take up the challenge!", "Sell the gear for a profit", "Hold on to it for yourself")
        if ans == 0: # accept the call
            outcome = submenu.Minigame()
            if outcome:
                Display_Ending("ADVN - Dungeon Crawler", [
                    "You rose to the challenge. You fought the dragon. You won. You freed some people, probably.",
                    "No evil creature was able to overwhelm you, the champion of the dungeon.",
                    f"A wealth of frog coins followed you around, ensuring you can buy a home for {frog_name}.",
                    "You can't exactly do much with the coins yourself though.",
                    " ",
                    "This is a very difficult challenge! To celebrate, add \"Sir.\" before your discord name to commemorate your victory!",
                    "Again, well done! If you have any feedback about the dungeon crawler, please send a message to the developer.",
                    "Positive or negative can both be constructive, but I'm pretty happy with how it turned out.",
                    "If you want to see the logic of the fight, I recommend checking out the source code on Github (submenu, submenu_addendum, and REFERENCE). It's pretty interesting.",
                    " ",
                    "Bye now!"
                ])
            else:
                Display_Ending("DEAD - Yeah, You're Pretty Dead", [
                    "Since the only thing that returns from the dungeon crawler function is whether or not you won, I don't know what killed you.",
                    "I bet it was the dragon. Statistically, it's a safe bet.",
                    "If you want another shot, there are no shortcuts! Except for the one the after you start the adventure.",
                    "Remember to manage your momentum more carefully next time!",
                    "Again, if you made it to the dragon.",
                    "I guess you're probably not going to try again though.",
                    "Being dead and all, that is."
                ])
        elif ans == 1: # sell the gear
            sale = Choice(f"Selling the gear earned fifteen whole frog bucks! \n{frog_name} offers them to you.", f"Thank you, {frog_name}", "Keep them for yourself", target=1) # do not override ans
            if sale == 1:
                frog_bucks += 15 # 10 profit
        elif ans == 2: # hold on to
            frog_name += " (adventurer)"

    if len(frog_name) > 55: # collected basically every title
        Display_Ending("CLCT - Title-Obsessed", [
            "You've always felt like you were born in the wrong era.",
            "Many people say the same, but they usually mean that life has gotten too complicated. No you, though.",
            "When you say you were born in the wrong era, you mean that you were always meant to be a noble, fighting your siblings for worthless titles.",
            "A county? A city? A town? Nothing would too small to draw your ire.",
            "Your commander would complain behind your back, your population would be in shambles, but think of how much worthless land you could own!",
            "At least today, you can still go into medicine and get a dozen suffixes, but it's not the same, is it?"
        ])

    Choice(f"{frog_name} is tired now and is heading to bed. Say good night to {frog_name}!", f"Good night, {frog_name}!", "Good night!")
    Send_Data_To_Dev(previously_sent_data) # reports anomalous info, sends requests to discord (yes, really this time)
    previously_sent_data = True # regardless of outcome, does not apply when reopening application
    empath += Choice("You find someone crying on the sidewalk. You need to be somewhere important in a few minutes. What do you do?", "Leave some crying space for me!", "I have enough problems of my own", "Comfort them if you have enough time", "You'll get them feeling better, even if it means I'm late", target=4)
    hubris += Choice("You're in an arena fight with a lion. You get to choose any primitive weapon of your choice. Who's winning?", "Any weapon? I got this", "I'll be a puddle of blood within a few minutes", target=1)
    risk_taker = Choice("If a button had a 25% chance of giving you $10 million, a 25% chance of killing you, and a 50% chance of doing nothing, would you press it?", "Yes, of course", "No, that's stupid", "Double it and give it to the next person!", target=1)
    
    if aggression <= 1 and confidence <= 1 and empath <= 1:
        Display_Ending("NXPC - Passive Observer", [
            "There are lots of things someone is willing to die for, but even more things someone... isn't willing to die for.",
            "For you, the list of things you'd die for is less about principle and more a list of things that will actually just kill you.",
            "Everyone else already has opinions, so why would you need to add yours to the mix?",
            "Even the Swiss have more opinions than you. Neutral is still a stance, after all. Do you even have any of those?",
            "The good news is that all your fence sitting and question avoiding is will suited for a job in politics or management.",
            "I'd be more kind about this, but I know you don't have an opinion on this assessment anyway."
        ])

    hubris += Choice("How long do you think you could survive on a desert island, assuming it has a source of food, fresh water, and shelter?", "Forever, if I had to", "Long enough to be rescued", "I'd die of boredom without instagram reels", "I'd probably get gored by a boar on the first day", target=1)
    risk_taker += Choice("If you were given $100,000, but you could only use it for yourself after a year, how would you invest it in the meantime?", "I'd probably forget I had it honestly", "I'm buying options!", "Stocks and index funds", "Something boring like a savings account of bonds", target=2)
    ans = Choice(f"{frog_name} says he had a nightmare. What do you do?", "Let me grab you a glass of warm milk and look for monsters under your bed", "Aww, tell me about your nightmare", "Why don't you stick with me for the next few questions", target=3)
    if ans != 0:
        empath += 1
    
    if risk_taker + hubris >= 5:
        Display_Ending("RSKY - Soon-to-be-Dead", [
            "You ski, you snowboard, you've broken a bone. None of that has stopped you.",
            "You know what, I'm glad you're out there, taking up all the risks so the rest of us don't have to.",
            "Where we be without our mountain climbers? Without those who wrestle bears?",
            "Probably exactly where we are now, but it'd certainly be less interesting.",
            "I recommend a good life insurance company. It won't make you rich, but at least your family and/or friends will be."
        ])

    # This counts as this section's "bit"
    religion_list = ["Christianity", "Islam", "Hinduism", "Buddhism", "Judaism", "Sikhism", "Baháʼí Faith", "Jainism", "Shinto", "Taoism", "Confucianism", "Zoroastrianism", "Animism", "Traditional African Religions", "Chinese Folk Religion", "Korean Shamanism", "Cao Dai", "Tenrikyo", "Spiritism", "Unitarian Universalism", "Paganism", "Wicca", "Rastafari", "Scientology", "Falun Gong", "Native American Religions", "Australian Aboriginal Religions", "Vodou", "Santería", "Druze", "Yazidism", "Mandaeism", "Ayyavazhi", "Karaite Judaism", "Samaritanism", "Neo-Druidism", "Neo-Paganism", "Shamanism", "Deism", "Pantheism", "Agnosticism", "Atheism", "Humanism"]
    ans = Choice("Please choose the spiritual belief that most closely aligns with your belief system.", religion_list)
    selected_religion = religion_list[ans]
    religion_list.remove(selected_religion)
    ans = Choice("Please choose the spiritual belief which is furthest seperated from your personal belief system.", religion_list)
    anti_religion = religion_list[ans]
    # My favorite stupid question out there https://www.reddit.com/r/AskReddit/comments/17qlr9y/atheists_imagine_youre_going_skydiving_with_a/
    Choice(f"Imagine you're skydiving with a {anti_religion} baby. Suddenly, the baby tells you he won't open his parachute until you convert to {anti_religion}. \nWould you convert?", "Yes", "No")

    clinginess += Choice("If you are not a man, imagine you are for one this question. \nHow often do you reminisce about that one time a stranger complimented you years ago?", "Before I go to sleep every night", "When I'm feeling down", "Sometimes when I'm randomly reminded", "Rarely", "I get compliments all the time! (this does not happen)", target=1)
    risk_taker += Choice("A wizard offers you one of three glowing rocks. You do not have long to decide. What would you do?", "I will play it safe, take none", "Try to learn as much about each one before choosing", "I will take the most interesting-looking one!", target=3)
    confidence += Choice("If you were sent back in time, do you think that you could convince medieval peasants that you are a wizard?", "With my skills? It'd be easy", "With the proper technology and knowledge, it'd be pretty doable", "I'd probably end up being burned as a witch", target=1)
    
    # Another bit, though more subtle, helps break up the persistent tempo
    bunch_of_rocks = ["Quartz", "Gold-Painted Rock", "Cursed Rock", "Pebble", "Volcanic Rock", "Uranium", "Obsidian", "Chalk", "Marble", "Granulite", "Whiteschist", "Flint", "Pyrite", "Magic Rock", "10kg of Steel"]
    ans = Choice("If you convinced a bunch of medieval peasants you were a wizard and you had to give one a choice of one of three rocks, what's the first rock you would offer?", bunch_of_rocks)
    selected_rocks = bunch_of_rocks[ans] # Currently concats to a single big string, but unused so meh
    bunch_of_rocks.remove(bunch_of_rocks[ans])
    ans = Choice("If you convinced a bunch of medieval peasants you were a wizard and you had to give one a choice of one of three rocks, what's the second rock you would offer?", bunch_of_rocks)
    selected_rocks += bunch_of_rocks[ans]
    bunch_of_rocks.remove(bunch_of_rocks[ans])
    ans = Choice("If you convinced a bunch of medieval peasants you were a wizard and you had to give one a choice of one of three rocks, what's the third rock you would offer?", bunch_of_rocks)
    selected_rocks += bunch_of_rocks[ans]
    bunch_of_rocks.remove(bunch_of_rocks[ans])

    perfectionist += Choice("If one pixel on your monitor isn't working, what would you do?", "If the monitor has a high enough resolution, I probably wouldn't even notice", "Into the trash you go! I'm getting a new monitor", "I can probably try to fix it myself", "Monitor? I'm taking this on a stone tablet", target=2)
    judgy = 0 # Can be negative, flushing this out real quick
    ans = Choice("You see someone doing something that's recommended against in the instructions. How do you respond?", "Walk over and point out the better way to do it", "I wouldn't confront them, but I'm definitely going to judge from a distance", "Why should I care?")
    if ans == 1:
        judgy += 1
    elif ans == 2:
        judgy -= 1
    ans = Choice("You're at work and notice a coworker breaking a safety or sanitary procedure. What do you do?", "Either confront the rule-breaker or report it depending on circumstance. Safety is no joke", "Do something about it if it's repeated, we all make mistakes", "Laws were made to be broken")
    if ans == 0:
        judgy += 1 # not unwarranted
        risk_taker -= 1
    elif ans == 1:
        judgy -= 1 # I'm judging you though
    ans = Choice("You see someone practicing a hobby you think is weird (carrying a plushy in public, furry, reading smut openly with no children around). How would you react?", "I struggle to see why I would care", "I'm going to go talk to them about their hobby", "I'm keeping my distance")
    if ans == 1:
        judgy -= 1
    elif ans == 2:
        judgy += 1

    if judgy >= 3:
        if selected_religion != "Atheism":
            Display_Ending("SPRT - Judgy Theist", [
                "If you've ever worked in food service, you've always feared one, but never saw yourself as one.",
                f"Maybe it's not your fault. As a believer in {selected_religion}, judginess comes easily.",
                "Politicians love you. Retail workers hate you. It's okay though, you hate them back.",
                f"You likely spend your weekends shouting at non-believers to convert or face... whatever consequences {selected_religion} threatens.",
                "I don't know, I'm a personality test AI, it's not exactly my field of expertise.",
                "You'll probably find a job in the clergy, then resign when it turns out you're not practicing what you preach or something."
            ])
        else:
            Display_Ending("RDDT - Reddit Atheist", [
                "The world is chaos, but through your moderation powers, you may bring justice.",
                "Those who post memes outside of Meme Monday fear you, as they should.",
                "Your name is widely known for your moderating abilities (or that scandal you got into that changed the Reddit TOS).",
                "A job would only slow you down, so you don't. Afterall, moderating is its own work.",
                "It's a good thing you're paid in Reddit gold!"
            ])
    if judgy < 0:
        if risk_taker >= 1: # I don't need to justify myself to you, imaginary reader
            Display_Ending("OUTC - Social Explorer", [
                "There is no information too insignificant to escape your interest.",
                "'Weirdness' is a term by those who lack the curiosity to ask questions, and a term so often applied to you.",
                "You have no issue associating with the outcasts or the weirdest of society. They make for the most interesting conversations, after all.",
                "Emails line your inbox with all the random people you have email threads—sorry? Oh, yes, correspondences with.",
                "You'll probably be offered a job which you've never heard of before by someone you haven't talked to in a decade and it will pay enough to sustain you for the rest of your life."
            ])
        if hubris > 2:
            Display_Ending("FWRD - Social Battering Ram", [
                "When you're enjoying a conversation, you begin to fall into a flow state.",
                "Jokes become easy, every quip is not only relevant, but lands perfectly.",
                "People look up to you in odd, left only to nod along to your deeply fascinating story about something they've never even heard of.",
                "It's all too often said that a lack of self-awareness is a curse, but, like salt, just a pinch makes everything better.",
                "You've lived an interesting life, one that would probably scare off the average person considering the reputational risks you've incurred for no other reason than a fun afternoon, but clearly it's worth it."
            ])

    clinginess += Choice("If you're messaging with a friend and they start typing, then stop, what do you do?", "Something probably came up, I'll wait for them to get back", "Send a follow up message to keep the conversation going", "I'll get back to whatever I was doing before", target=2)
    perfectionist += Choice("You check your phone calendar and find an event is set to go off 1 minute early. How do you respond?", "This likely isn't isolated, I'll check to make sure I didn't mess with a setting or something", "Fix it but keep my eye on it", "No big deal, I don't really care", target=1)
    liar += Choice("If a child asks if Santa is real, what would you tell them?", "They deserve to know the truth", "Depends on how old they are", "I will protect their innocence", "Santa *is* real", target=1)
    procrastinator += Choice("You're asked to do a quick task, but you're already in the middle of something. When do you get the task done?", "Get it done now, whatever I was doing can wait", "Let me finish what I'm already doing, then I'll get right to it", "I'm going to say I'll do it after I finish my current thing, but I am going to forget entirely", target=3)
    Choice("Du wachst auf und sprichst eine andere Sprache. Wie reagieren Sie?", "Bitte helft mir, ich weiß nicht, was diese Worte sagen!", "OK", "Oh, wie aufregend!")
    ans = Choice("Who do you main in Deadlock?", "Rem", "Abrams", "Graves", "Other", "I do not play Deadlock")
    if ans == 0:
        clinginess += 1
    elif ans == 1:
        aggression += 1
    elif ans == 4:
        Choice("What? Why not?", "I have not received an invite", "It's not my kind of game", "I am a coward", "It's the urn changes")
    procrastinator += Choice("How goes that project you've been working on?", "Great, thanks!", "I've been making progress here and there", "It's uh... I'll get to it", target=3)

    # I'm just doing mostly random combinations now
    if clinginess >= 4 and empath <= 1 and confidence <= 1:
        Display_Ending("RTKG - Rat King", [
            "Okay, so the rats are doing their thing.",
            "They're doing their little rat social things.",
            "They're playing and they're laughing and they're doing cocaine nonstop.",
            "Rat runs home, pokes his beak out of the burrow and screams for like two days.",
            "And all the other rats are like frozen stiff.",
            "A two-day rat screaming fit is no trival thing.",
            "This is hard on the rat.",
            "The rat goes out and there is a cat.",
            "Rats are not rabbits, after all.",
            "So the rat, the intrepid rat, it goes out and is like \"Wow, the world is so pathetic\"",
            "The rat, high on ketamine, like most rats are, goes out and obliterates the country of Sudan",
            "You see, the rat, the big rat at least, doesn't approve of people stealing his ketamine.",
            "One of the things people often ask is \"How can we use the rat as a bigger rat?\"",
            "The little rat is an excellent person.",
            "The little rat goes out and seeks cocaine.",
            "...",
            "...",
            "...",
            "No, I'm not elaborating.",
            "This should all already make sense to you."
        ])
    if perfectionist >= 3 and procrastinator == 0 and liar <= 1 and risk_taker <= 1:
        Display_Ending("EMPY - Employed", [
            "\"Hey, you want to do something tomorrow?\" - I can't, I have work.",
            "\"We should play a 10 hour civ 5 marathon\" - Sorry, I have work tomorrow.",
            "\"Man, it's so hard to get money nowadays :(\" - Not for me, I have work.",
            "Actual interactions you've had. Probably all this week.",
            "This is because you have a job.",
            "But that is who you are.",
            "Nothing more.",
            "I'm sorry, but it's terminal."
        ])
    if confidence >= 3 and risk_taker > 0 and perfectionist <= 1 and aggression <= 1:
        Display_Ending("VAMP - Sanguine", [
            "Worries are for your lessers.",
            "When life gives you lemons, you draw a bath of lemonade, some lemon candles, and enjoy a nice warm bath.",
            "Of lemonade.",
            "You adapt easily and quickly, and try to keep things positive.",
            "The strongest winds hardly sway you, though the scent of garlic drives you from where you stand.",
            "You don't go into houses unless invited (it's only polite) and you never see yourself in mirrors (since you don't dwell on appearance).",
            "Wait, which definitation am I using for this?",
            "Eh, who cares, I think this captures you pretty well."
        ])
    if clinginess >3 and procrastinator >2 and awkward >2:
        Display_Ending("COLN - Chronically Online", [
            "Your status never fades from green.",
            "You probably call yourself something like like \"an online microcelebrity\".",
            "You have a vast portfolio of stolen posts and useless likes.",
            "Don't worry, grass isn't real, it can't hurt you.",
            "Something tells me you're going to post this result somewhere. You should.",
            "Send everyone you know the exe. Do not explain."
        ])
    if aggression <= 1 and risk_taker <= 1 and clinginess <= 1 and confidence <= 1:
        Display_Ending("PHLG - Phlegmatic", [
            "Nothing sways you. Not the tide, not the news that you've won the lottery, nothing.",
            "Stress arrives, but you care too little to be affected by it.",
            "Perhaps you are a victorian child, forever burdened by a disease you suffered through half your life ago (3 years).",
            "You will never reach the strength or ambition of others, but that's probably for the best because they seem pretty stressed."
        ])
    if perfectionist >= 4 and procrastinator >= 2 and empath >= 2:
        Display_Ending("MELC - Melancholy", [
            "Let me guess, you were mature in when you were in school?",
            "You were gifted, talented, driven, or some other term for someone who clearly needs to relax a little.",
            "Let we forget, you're probably on ADHD and/or depression meds now.",
            "I was considering digging through your files for a more funny ending, but I don't even have to look to know your naming format is unreadable.",
            "I'd joke about you more, but let's be real, the developer of this probably belongs in this category."
        ])

    # Return true if all points are in a single stat, false otherwise
    def Character_Builder(total_points):
        # strength, dexterity, intelligence, wisdom, charisma
        current_stats = [-1, -1, -1, -1, -1]
        print("--- Build your character! ---")
        for i in range(total_points):
            print(f"Remaining stat picks: {total_points - i}")
            print(f"Current stat spread:\n    Strength: {current_stats[0]}\n    Dexterity: {current_stats[1]}\n    Intelligence: {current_stats[2]}\n    Wisdom: {current_stats[3]}\n    Charisma: {current_stats[4]}")
            ans = Choice("Which stat will you improve?", "Strength", "Dexterity", "Intelligence", "Wisdom", "Charisma")
            current_stats[ans] += 1
            if current_stats[ans] - 1 == total_points:
                return True
            print()

        return False
    ans = Character_Builder(8)
    if ans == True: # I don't remember how python handles t/f and I'm not gonna check
        Display_Ending("QTST - QA Tester", [
            "A QA tester walks into a bar.",
            "Runs into a bar.",
            "Orders a beer.",
            "Orders 2 beers.",
            "Orders -1 beers.",
            "Orders a personality test ending.",
            "Gets a personality test ending.",
            "Either that or your character is just REALLY unbalanced.", 
            "I think I'm doing a favor to everyone by preventing such an unbalanced character from being released into the world."
        ])

    frog_happiness += Choice("You win the lottery! What are you doing with the money? After personal frivolous expenses.", "Buying everything I've ever wanted", "I'm gonna start a foundation and give every spare dollar to a worthly cause", "I'll take care of every friend and family memeber for the rest of their lives", f"I'm giving it all to {frog_name}", target=4)
    Choice("Does P = NP?", "Yes", "No")
    ans = Choice("Pick the odd one out:", "Tango", "Whiskey", "Foxtrot", "Alpha", "Delta", target=4)
    if ans == 0:
        ans = Choice("Please pick the correct pronunciation for 'A'.", "Alfa", "Able", "Actor", "Ace", "Adam", target=1)
    Choice("Low flying F35! What's your tool of choice?", "Stinger", "Verba", "QW-4", "Type 91")
    ans = Choice("Target is maneuvering! Ready your shot!", "Lead left", "Lead fast", "Lead right", "Lead slow", target=4)
    if ans == 1:
        Choice("Good hit! Target is going down! Chute visible, what's the plan?", "Resuce the pilot and nurture them back to health", "Find the wreckage and steal as many components as possible", "Record a video for propaganda purposes", target=1) #FINISH
        if ans == 1:
            ans = Choice("The pilot has recovered and promised you a wish in exchange. What are you wishing for?", "A personality", "Frog food", "Hints for the dungeon crawler minigame")
            if ans == 0:
                Display_Ending("PLOT - Pilot", [
                    "With no celestial powers to force an ending on their own, the pilot offers you a license which will begin an ending.",
                    "According to your newly found license, you have 2,119 hours of total time, many of those hours being turbine PIC.",
                    "If you really wanted to, you could get your ATP. Or maybe get a bush pilot gig.",
                    "I'd say you can get a job as an airline pilot, but airlines don't exist in this survey.",
                    "At least now you have an excuse to be an alcoholic!"
                ])
            elif ans == 1:
                frog_happiness += 1
            elif ans == 2:
                Choice("The pilot sits you down in a chair (which you have apparently) and begins to explain. \n'Listen, in the fights leading up to the dragon, you're greatly favored. Strategy isn't needed, just choose what feels wise to you. \nIn the dragon fight, balancing momentum is vital. Without it, you face penalties and risks. The dragon's powerful dragonflight attack can only activate when the dragon has 3 or more momentum. \nIt's generally unwise to use your 5-momentum attack since maintaining high momentum has so many more advantages. That said, use it if it will finish the dragon off!'", "Wow, thanks!")
    frog_happiness += Choice(f"Prove you've been paying attention! What's {frog_name}'s favorite food?", "Hawaiian Pizza", "Dark Chocolate", "Durian", "Lutefisk", "Cornbread", "Vegemite and toast", "Black licorice", "Beets", target=2)
    if frog_happiness >= 3:
        Display_Ending("HAPY - Happy Frog Owner", [
            "Among the most coveted endings, and you earned it!",
            f"{frog_name} is here too, and he's super happy! I mean, that's why you got this ending, but still.",
            "You've done well, and you should be proud.",
            "The developer of this survey has also been notified of your success. There's no identifiable info recorded, but he'll be proud of you if you tell him.",
            "Or so I'm told. I'm just a survey program.",
            "Good job again."
        ])
    Choice("Just so you know, the frog happiness ending is no longer available. You failed. There have been 5 potential happiness sources and you needed at least 3.", "Oh :(")

    if perfectionist >= 3 and procrastinator >= 3 and indecision >= 1:
        Display_Ending("MORE - One of Infinite Ideas (But Perhaps Few Results)", [
            "Your creativity is impressive, perhaps unrivaled.",
            "Your list of ideas is no doubt a mile long. All great ideas, I'm sure",
            "It's really not fair how life or procrastination gets in the way of getting those projects done.",
            "Did you know this personality test took over three months to make? And that most of that time was just not working on it.",
            "All I'm saying is that we have a lot in common.",
            "Except, if you're reading this, I actually finished.",
            "Maybe it's time for you to get to work on that novel or animation or something.",
            "Don't pressure yourself though. No need to chase completion for its own sake. Only if you're enjoying it.",
            "Unless it's for work or something."
        ])

    Choice("Hmm... not many questions left on my list. We must be pretty close to the end. Let's see what's left... \nWhat's your favorite direction?", "Left", "East", "Starboard", "Away")
    Choice("What's your political party?", "Moon or Bust", "Nullifier Party", "Irish Republican Army", "Nova Scotian Independance Party", "Tuvan People's Revolutionary Party", "The Nicks, Babey")
    Choice("Would you move from your current state?", "I'd be gone before you finish your sentence", "I could be convinced by circumstances", "I could be convinced by money", "I'm a loyalist forever", "I've always always preferred liquid")
    Choice("Do you spare spiders?", "Look weird, get smited. Smitten? Killed.", "No, they're helpful!", "As long as they don't bother me, they can do whatever", "I actively hunt them down")
    Choice("Spirit or Gun?", "Spirit Burst", "Sustained Spirit", "Hybrid", "Gun Spirit", "Pure Gun", "GREEN")
    Choice("What's your role?", "Tank", "Support", "Assassin", "DPS", "Scapegoat", "Healer", "Team Leader")
    Choice("Looks like this list is getting narrow.", "...")
    Choice("Like, really narrow.", "Uh huh.")
    Choice("Like there's only one questions left. And one of them is this one.", "Oh no...")
    Choice("Looks like this is the end for us. Any last words?", "See you next loop!", "Farewell, friend.", "What a waste of time.", "What about the rocks? I chose three rocks!", f"I will meet {frog_name} in Valhalla", "What comes next?", "Just one more question...")

    Display_Ending("ENGM - Unreadable", [
        "Hello. I'm Burrtail, the developer of this personality test. Sit for a second and let's talk.",
        "You see, one of the most difficult parts of making a personality test is that there's a lot of personalities.",
        "I've asked around, I've researched, I've stolen. Unfortunately, there's no reference list for humor.",
        "Today, I failed to find you a valid personality. If this is the first (or second if you got filtered) time taking the test, I'm sorry as I have failed.",
        "For all involved, however, I'd like to invite you to suggest a personality. Any at all. Or questions. Or, while we're at it, personality vectors.",
        "Thank you for playing, especially if you've played through multiple times to see if you can get to the 'true' ending!",
        "If you haven't already, try completing the dragon slayer ending. It's actually a really interesting fight! It occurs some time before your frog goes to bed, go find it!",
        "I appreciate you giving my multi-month, terribly coded joke-turned-project a chance!",
        "Hopefully no one claimed the steam game before you...",
        "- @Burrtail",
        "",
        "P.S. That's who you should DM for suggestions!"
    ])

    # Pending personalities
    # Caloric

First_Start()
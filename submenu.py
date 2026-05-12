import time, random
import REFERENCE

LINE_BREAK = "──────────────────────────────────────────────────────────"

PLAYER_START_HEALTH = 10
PLAYER_HEALTH_GROWTH = 3
UNICORN_START_HEALTH = 6
GRYPHON_START_HEALTH = 11

def Minigame(frog_name="Testing Frog"):
    slow_print("You enter the dungeon, the cold and dank air hitting your nose immediately.")
    slow_print("The walls are decrepit and detritus crumbles from them when touched.")
    slow_print("You hear distant sounds of crackling. Fire, falling stone, or something more sinister.")
    slow_print("The moisture in the air is so thick it coats your skin.")
    pause(secs=1.5)
    print(REFERENCE.CORRIDOR_SPLIT)
    slow_print("You begin forward into the dungeon, watching the light of outside fade behind you.")
    slow_print("The stone walls begin to become uniform as press you on, occluded from the elements. Ahead, the path splits, both ways looking identical.")
    print("\nOnly enter the letter corresponding to an action, as indicated by the parentheses. E.g. for (r)ight, enter 'r'.")

    # Doesn't actually matter, but might as well make players feel like it does
    while True:
        ans = input("Do you go (l)eft? Or (r)ight? ").strip().lower()
        if ans == "l" or ans == "r":
            break
        print("\nInvalid input! Only enter the letter corresponding to an action, as indicated by the parentheses. E.g. for (r)ight, enter 'r'.")
    
    slow_print("You turn ", newline=False)
    if ans == "l":
        slow_print("left, lit now only by your torch.")
    else:
        slow_print("right, lit now only by your torch.")
    pause()
    slow_print("As you press onward, a chalky mass flickers at the edge of your light.")
    slow_print("You extend your torch forward, bringing the flame closer, the light glints off a reflective, almost mesmerizing horn.")
    # Fancy formatting
    slow_print("You snap out of your trance ", newline=False)
    slow_print("just in time", delay=0.005, newline=False)
    pause()
    slow_print(" barely dodging the unicorn's strike!")
    pause()
    slow_print("\nYou draw your sword and ready your stance. It's you or it.")
    pause(secs=1.5)

    # Begin first fight
    combat_outcome = Combat(static=REFERENCE.UNICORN_STATIC, charging=REFERENCE.UNICORN_CHARGING, reeling=REFERENCE.UNICORN_REELING, player_health_max=PLAYER_START_HEALTH, enemy_health_max=UNICORN_START_HEALTH, enemy_name="Unicorn", use_tutorial=True)
    if combat_outcome == False: # I go back and forth with if !cond or if cond == False
        print(f"        You             {hp_bar(0, PLAYER_START_HEALTH)}")
        slow_print("Your knees have grown weak. Your arms weaker.")
        pause()
        slow_print("You struggle to raise your sword. Now is your chance to fight back, but your energy is sapped. Your body is screaming for rest.")
        pause()
        slow_print("The unicorn charges one more time, but you know you lack the energy to fight back.")
        slow_print("You raise your shield one more time, but it suddenly feels much heavier. It's over.")
        pause(3)
        return False # Return to survey with failure. Dead ending?
    
    print(f"        Unicorn             {hp_bar(0, UNICORN_START_HEALTH)}")
    line_break()
    pause(2)
    slow_print("You blade strikes true one last time, sinking into the unicorn's neck.")
    pause(0.5)
    slow_print("The scuffle stops immediately. You've won.")
    pause()
    slow_print("You wipe your blade clean of blood, though not before removing the unicorn's horn as a trophy for yourself.")
    slow_print("There's little time to celebrate though, the sound of fighting no doubt drew the attention of other dungeon inhabitants.")
    pause(2)

    print(REFERENCE.CORRIDOR_BRANCHING)
    slow_print("After a short rest in a quiet corner, you delve deeper.")
    slow_print("It's not long before you're at another junction, this one splitting three ways.")

    # This is one more use away from becoming afunction
    while True:
        ans = input("Do you go (l)eft, (s) straight, or (r)ight? ").strip().lower()
        if ans == "l" or ans == "r" or ans == "s":
            break
        print("\nInvalid input! Only enter the letter corresponding to an action, as indicated by the parentheses. E.g. for (r)ight, enter 'r'.")
    
    # Same answer if left or right except for one word because who cares
    if ans == "l":
        slow_print("You head left. Holes litter the floor here, so you keep your eyes low to watch for traps. The trapmaker's art is a cruel one.")
        slow_print("Several stones shift as you step on them, but each time it ends up as nothing more than a loose stone.")
        slow_print("When the floor and walls begin to smooth, you take a few minutes to stop and snack on some nuts and dried beef.")
        pause()
        slow_print("Once you're back on your feet, you spot a larger area up ahead, for once feeling thankful that this path was uneventful.")
        pause()
    elif ans == "r":
        slow_print("You head right. Holes litter the floor here, so you keep your eyes low to watch for traps. The trapmaker's art is a cruel one.")
        slow_print("Several stones shift as you step on them, but each time it ends up as nothing more than a loose stone.")
        slow_print("When the floor and walls begin to smooth, you take a few minutes to stop and snack on some nuts and dried beef.")
        pause()
        slow_print("Once you're back on your feet, you spot a larger area up ahead, for once feeling thankful that this path was uneventful.")
        pause()

    elif ans == "s":
        slow_print("You head forward, pressing your ear to the door and listening. When no sound comes, you turn the knob and open the door.")
        slow_print("Inside, the 'room', if it could so be called, is mostly baren. The walls are slightly more intact here, but the door seems mostly cosmetic since the path keeps going forward.")
        slow_print("Something glints at the edge of your torch light, drawing your attention. ", newline=False)
        pause()
        slow_print("A chest!")
        pause(0.5)
        slow_print("You check for traps, but upon finding nothing, you crack open the lid...")
        slow_print("Inside you find... ", newline=False)
        pause()
        slow_print("Five frog bucks?") # No use
        pause()
        slow_print("You shrug and pocket the odd currency.")
        slow_print("With your pockets now slightly more stuffed, you return the path. You can already see a larger area up ahead.")
        pause()

    slow_print("The sound of wings pull your eyes upward.")
    pause()
    slow_print("The air near your ear wooshes as a talon passes all too close to your ear. ", newline=False)
    pause()
    slow_print("A gryphon! To arms!")
    pause(2)
    combat_outcome = Combat(static=REFERENCE.GRYPHON_STATIC, charging=REFERENCE.GRYPHON_CHARGING, reeling=REFERENCE.GRYPHON_REELING, player_health_max=PLAYER_START_HEALTH+PLAYER_HEALTH_GROWTH, enemy_health_max=GRYPHON_START_HEALTH, enemy_name="Gryphon")
    if combat_outcome == False:
        print(f"        You             {hp_bar(0, PLAYER_START_HEALTH+PLAYER_HEALTH_GROWTH)}")

# -- Main Combat Function --

def Combat(static="S", charging="C", reeling="R", player_health_max=10, enemy_health_max=6, enemy_name="Invalid Monster", use_tutorial=False):
    """
    Fight Design:
    Start in 'even footing'. 
    Both sides choose an attack type—Slash, Block, or Feint. 
    Slash beats feint, block beats slash, feint beats block. In this stage, display the static sprite.

    If either side wins, they deal 1 damage, then enter advantage state. Change sprite depending on advantage
    In advantage state, both sides again get 3 options, though they differ for attacking and defending.
    For the side with advantage ('charging'), they can Charge, Kite, or Heavy Attack
    For the side in disadvantage ('reeling'), they can Retreat or Dig In
    Charge beats retreat, dealing 2 extra damage, Kite only deals 1 extra damage, but can't be countered, and Heavy Attack beats Dig In, also dealing 2 extra damange.
    In the event that the defender chooses the correct counter (retreat against heavy, dig in against charge), they take no additional damage.
    In any case, both sides return to the even stance.

    Combat ends when either side runs out of health.
    """
    # Set currents and maximums at start
    # Also I know these look kinda like AI comments, but that's one thing AI got right
    enemy_health_current = enemy_health_max
    player_health_current = player_health_max
    use_tutorial_clash = use_tutorial
    use_tutorial_advantage = use_tutorial
    use_tutorial_disadvantage = use_tutorial

    if use_tutorial_clash:
        # Doesn't really matter between slow_print or combat_print since delay is manual but thematic ig
        tutorial_print("\nYou are about to enter combat, so here's a quick reminder:")
        tutorial_print("Both you and your opponent will chose to Slash, Block, or Feint.")
        tutorial_print("Slash beats Feint, Block beats Slash, Feint beats Block.")
        tutorial_print("Whoever wins the interaction will deal 1 damage to the other side, then enter advantage stance.")
        tutorial_print("More information will be provided as you enter each combat phase.")
        tutorial_print("\nTo enter your action, enter only the letter indicated before the action, such as 'b' for [B] Block.")
        tutorial_print("Press enter when you're ready to continue... ", newline=False)
        input()
        use_tutorial_clash = False

    # Repeat until one side runs out of health
    while True:
        # Reset to static when no other actions remain
        print(static)
        player_action = Static_Menu(enemy_name, enemy_health_current, enemy_health_max, player_health_current, player_health_max)
        enemy_action = Random_Attack()

        # TO DO: make dialog variable-based dialog instead of hard coding
        outcome = run_combat_event(player_action, enemy_action)

        if outcome == "advantage":
            if use_tutorial_advantage:
                tutorial_print("\nSince your attack was successful, you've dealt damage to your enemy and entered the advantage stance.")
                tutorial_print("Now you have thre choices: Charge, Kite, and Heavy Attack. Kite will always deal 1 extra damage.")
                tutorial_print("The opponent will have the choice to Retreat or Dig In. If you Charge and your enemy Digs In, you deal no extra damage, likewise for Heavy Attack and Retreat.")
                tutorial_print("If your opponent chooses the wrong counter, you deal 2 extra damage! If they choose the right counter, you deal 0 extra damage.")
                tutorial_print("In any case, you return to the neutral stance after your advantage attack.")
                tutorial_print("Press enter when you're ready to continue... ", newline=False)
                input()
                use_tutorial_advantage = False

            enemy_health_current -= 1
            if (enemy_health_current <= 0):
                return True

            print(reeling)
            player_action = Advantage_Menu(enemy_name, enemy_health_current, enemy_health_max, player_health_current, player_health_max)

            if player_action == "k": # Kite 1 damage, always successful
                combat_print("You hold your momentum, scoring several more cuts and bruises before the chase is over and you're back to even footing.")
                pause()
                enemy_health_current -= 1
                if (enemy_health_current <= 0):
                    return True

            else: # Non-kite, the beast counters
                enemy_action = Random_Attack(outcome)

                outcome = run_combat_event(player_action, enemy_action)
                if outcome == "success":
                    enemy_health_current -= 2
                    if (enemy_health_current <= 0):
                        return True

        elif outcome == "disadvantage":
            if use_tutorial_disadvantage:
                tutorial_print("\nYour opponent has scored a hit and now you are reeling. Your opponent will have a chance to deal extra damage, so prepare to defend yourself.")
                tutorial_print("You can either Retreat, defending against a Heavy Attack, or Dig In to defend against an opponent's Charge.")
                tutorial_print("If you choose right, you take no extra damage. Choose wrong, take an extra point of damage.")
                tutorial_print("In either case, you return to the neutral stance afterwards.")
                tutorial_print("Some enemies prefer certain attacks more than others, so pay attention to patterns.") # I love lying
                tutorial_print("Press enter when you're ready to continue... ", newline=False)
                input()
                use_tutorial_disadvantage = False

            player_health_current -= 1
            if (player_health_current <= 0):
                return False
            print(charging)
            player_action = Disadvantage_Menu(enemy_name, enemy_health_current, enemy_health_max, player_health_current, player_health_max)
            enemy_action = Random_Attack(outcome)

            outcome = run_combat_event(player_action, enemy_action)
            if outcome == "failure":
                player_health_current -= 1 # Player advantage
                if (player_health_current <= 0):
                    return False

        # Victory condition
        if enemy_health_current <= 0:
            return True
        
        if player_health_current <= 0:
            return False

# -- Action Menus --

# Display health and options, return valid answer
def Static_Menu(enemy_name, enemy_health_current, enemy_health_max, player_health_current, player_health_max, display_hint=False):
    Display_Stats(enemy_name, enemy_health_current, enemy_health_max, player_health_current, player_health_max)
    print("What will you do?")
    if display_hint:
        print("HINT: Only enter the letter shown before each action to take that one!")
    print("[S] Slash            [B] Block         [F] Feint")
    print()
    action = input("> ").strip().lower()
    if action == "s" or action == "b" or action == "f":
        return action
    else:
        # Reprompt on invalid input with added hint
        slow_print("Invalid action!")
        pause(1)
        return Static_Menu(enemy_name, enemy_health_current, enemy_health_max, player_health_current, player_health_max, display_hint=True)
    
def Advantage_Menu(enemy_name, enemy_health_current, enemy_health_max, player_health_current, player_health_max, display_hint=False):
    Display_Stats(enemy_name, enemy_health_current, enemy_health_max, player_health_current, player_health_max)
    print("The enemy is reeling! Press the advantage!")
    if display_hint:
        print("HINT: Only enter the letter shown before each action to take that one!")
    print("[C] Charge            [K] Kite          [H] Heavy Attack")
    print()
    action = input("> ").strip().lower()
    if action == "c" or action == "k" or action == "h":
        return action
    else:
        # Reprompt on invalid input with added hint
        slow_print("Invalid action!")
        pause(1)
        return Advantage_Menu(enemy_name, enemy_health_current, enemy_health_max, player_health_current, player_health_max, display_hint=True)
    
def Disadvantage_Menu(enemy_name, enemy_health_current, enemy_health_max, player_health_current, player_health_max, display_hint=False):
    Display_Stats(enemy_name, enemy_health_current, enemy_health_max, player_health_current, player_health_max)
    print("You're on the backfoot! How will you defend yourself?")
    if display_hint:
        print("HINT: Only enter the letter shown before each action to take that one!")
    print("[R] Retreat            [D] Dig In")
    print()
    action = input("> ").strip().lower()
    if action == "r" or action == "d":
        return action
    else:
        # Reprompt on invalid input with added hint
        slow_print("Invalid action!")
        pause(1)
        return Disadvantage_Menu(enemy_name, enemy_health_current, enemy_health_max, player_health_current, player_health_max, display_hint=True)
    
# -- Combat Helpers --

def Display_Stats(enemy_name, enemy_health_current, enemy_health_max, player_health_current, player_health_max):
    line_break()
    print(f"        {enemy_name}             {hp_bar(enemy_health_current, enemy_health_max)}")
    line_break()
    print(f"        YOU                    {hp_bar(player_health_current, player_health_max)}")

# I could have just rolled a d3 or d2 to determine outcomes, but I think this is still worth it since this is more modular
def Random_Attack(mode="static"):
    # It occurs to me now I could have just passed in options, then randomly selected from the list
    # At least you know this is human code
    if mode == "static":
        r = random.randint(1, 3)
        # I could also return both as numbers, but I think it's more readable this way
        if r == 1:
            return "s"
        if r == 2:
            return "b"
        if r == 3:
            return "f"
    elif mode == "advantage": # player advantage
        r = random.randint(1, 2)
        if r == 1:
            return "r"
        if r == 2:
            return "d"
    elif mode == "disadvantage": # player disadvantage
        # No kite for monsters, additional boost for players
        r = random.randint(1, 2)
        if r == 1:
            return "c"
        if r == 2:
            return "h"

# Runs the dictionary and returns the outcome
# Returns "clash", "advantage", or "disadvantage"
def run_combat_event(player_action, enemy_action):
    event = REFERENCE.combat_events.get((player_action, enemy_action))

    if not event:
        slow_print("Something about your action caused an error.")
        pause()
        slow_print("Maybe something to discuss with the developer?")
        slow_print("Try again, but do something differently this time.")
        pause()
        return

    for line in event["lines"]:
        combat_print(line)

    pause(secs=1.5)

    return event.get("result")

# -- Utilities --

def slow_print(text, delay=0.027, newline=True):
    for ch in text: # I keep forgetting you don't need parentheses in python
        print(ch, end='', flush=True) # Flush needs to be true or messes up
        time.sleep(delay)
    if newline:
        print()

# Wrapper with fast default read, better for keeping tempo in combat
def combat_print(text, delay=0.02, newline=True):
    slow_print(text, delay=delay, newline=newline)

# Another speed wrapper
def tutorial_print(text, delay=0.015, newline=True):
    slow_print(text=text, delay=delay, newline=newline)

def pause(secs=1):
    time.sleep(secs)

# Makes things look a little cleaner
def line_break():
    print(LINE_BREAK)

def hp_bar(current, maximum):
    bar = '['
    for i in range(maximum):
        if(i < current):
            bar += '█'
        else:
            bar += '░'
    bar += f"] {current}/{maximum}"
    return bar

def main():
    print("─── You are currently in testing mode ───")
    Minigame()

main()
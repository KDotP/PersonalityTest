# Since I've decided to make the test available as an exe, I don't think I'm going to try to conceal the context anymore :)
import time, random
import REFERENCE

LINE_BREAK = "──────────────────────────────────────────────────────────"

PLAYER_START_HEALTH = 10

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
        if (ans == "l" or "r"):
            break
        print("\nInvalid input! Only enter the letter corresponding to an action, as indicated by the parentheses. E.g. for (r)ight, enter 'r'.")
    
    slow_print("You turn ", newline=False)
    if (ans == "l"):
        slow_print("left, lit now only by your torch.")
    else: ## TO DO: this does not properly register invalid inputs! 
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
    combat_outcome = Combat(static=REFERENCE.UNICORN_STATIC, charging=REFERENCE.UNICORN_CHARGING, reeling=REFERENCE.UNICORN_REELING, player_health_max=PLAYER_START_HEALTH, enemy_health_max=6, enemy_name="Unicorn")
    if combat_outcome == False: # I go back and forth with if !cond or if cond == False
        slow_print("Your knees have grown weak. Your arms weaker.")
        pause()
        slow_print("You struggle to raise your sword. Now is your chance to fight back, but your energy is sapped. Your body is screaming for rest.")
        pause()
        slow_print("The unicorn charges one more time, but you know you lack the energy to fight back.")
        slow_print("You raise your shield one more time, but it suddenly feels much heavier.")
        pause(5) # SET TO 2 FOR REAL RUN
        return False # Return to survey with failure. Dead ending?
    slow_print("You wipe your blade clean of blood, though not before removing the unicorn's horn as a trophy for yourself.")
    pause(5) # REMOVE FOR REAL RUN

# -- Main Combat Function --

def Combat(static="S", charging="C", reeling="R", player_health_max=10, enemy_health_max=6, enemy_name="Invalid Monster"):
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
    use_tutorial_clash = True
    use_tutorial_advantage = True
    use_tutorial_disadvantage = True

    # Repeat until one side runs out of health
    while True:
        print(static)
        player_action = Static_Menu(enemy_name, enemy_health_current, enemy_health_max, player_health_current, player_health_max)
        enemy_action = Random_Attack()

        # TO DO: make dialog variable-based dialog instead of hard coding
        outcome = run_combat_event(player_action, enemy_action)

        if outcome == "advantage":
            enemy_health_current -= 1
            if (enemy_health_current <= 0):
                return True

            print(reeling)
            player_action = Advantage_Menu(enemy_name, enemy_health_current, enemy_health_max, player_health_current, player_health_max)

            if player_action == "k": # Kite 1 damage, always successful
                combat_print("You hold your momentum, scoring several more cuts and bruises before the chase is over and you're back to even footing.")
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
def combat_print(text, delay=0.022, newline=True):
    slow_print(text, delay=delay, newline=newline)

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
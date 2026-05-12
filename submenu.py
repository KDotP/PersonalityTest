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
    Fight_One(frog_name)

def Fight_One(frog_name):
    Combat(static=REFERENCE.UNICORN_STATIC, charging=REFERENCE.UNICORN_CHARGING, reeling=REFERENCE.UNICORN_REELING, player_health_max=PLAYER_START_HEALTH, enemy_health_max=6, enemy_name="Unicorn")

def Combat(static="S", charging="C", reeling="R", player_health_max=10, enemy_health_max=6, enemy_name="Testing Monster"):
    """
    Fight Design:
    Start in 'even footing'. 
    Both sides choose an attack type—Slash, Block, or Feint. 
    Slash beats feint, block beats slash, feint beats block. In this stage, display the static sprite.

    If either side wins, they deal 1 damage, then enter advantage state. Change sprite depending on advantage
    In advantage state, both sides again get 3 options, though they differ for attacking and defending.
    For the side with advantage ('charging'), they can Charge, Kite, or Heavy Attack
    For the side in disadvantage ('reeling'), they can Retreat or Riposte
    Charge beats retreat, dealing 2 extra damage, Kite only deals 1 extra damage, but can't be countered, and Heavy Attack beats Riposte, also dealing 2 extra damange.
    In the event that the defender chooses the correct counter (retreat against heavy, riposte against charge), they take no additional damage.
    In any case, both sides return to the even stance.

    Combat ends when either side runs out of health.
    """
    # Set currents and maximums at start
    # Also I know these look kinda like AI comments, but that's one thing AI got right
    enemy_health_current = enemy_health_max
    player_health_current = player_health_max

    # Repeat until one side runs out of health
    while True:
        print(static)
        player_action = Static_Menu(enemy_name, enemy_health_current, enemy_health_max, player_health_current, player_health_max)
        enemy_action = Random_Static_Attack()

        # TO DO: make dialog variable-based instead of hard coding!
        run_combat_event(player_action, enemy_action)

# Display health and options, return valid answer
def Static_Menu(enemy_name, enemy_health_current, enemy_health_max, player_health_current, player_health_max, display_hint=False):
    line_break()
    print(f"        {enemy_name}             {hp_bar(enemy_health_current, enemy_health_max)}")
    line_break()
    print(f"        YOU                    {hp_bar(player_health_current, player_health_max)}")
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

def Random_Static_Attack():
    r = random.randint(1, 3)
    # I could also return both as numbers, but I think it's more readable this way
    if r == 1:
        return "s"
    if r == 2:
        return "b"
    if r == 3:
        return "f"

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

def slow_print(text, delay=0.027, newline=True):
    for ch in text: # I keep forgetting you don't need parentheses in python
        print(ch, end='', flush=True) # Flush needs to be true or messes up
        time.sleep(delay)
    if newline:
        print()

# Wrapper with fast default read, better for keeping tempo in combat
def combat_print(text, delay=0.02, newline=True):
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
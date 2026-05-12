# Since I've decided to make the test available as an exe, I don't think I'm going to try to conceal the context anymore :)
import time, random

# Sourced via https://www.asciiart.eu/art/23319246a6009130, author Tim Spicer (Darkstar), modified
CORRIDOR_SPLIT = r"""
 _____________________________________________
|.'',                                     ,''.|
|.'.'',                                 ,''.'.|
|.'.'.'',                             ,''.'.'.|
|.'.'.'.'',                         ,''.'.'.'.|
|.'.'.'.'.|                         |.'.'.'.'.|
|.'.'.'.'.|=========================|.'.'.'.'.|
|.'.'.'.'.|:::|::::::::|::::::::|:::|.'.'.'.'.|
|.'.'.'.'.|---|--------|--------|---|.'.'.'.'.|
|.'.'.'.'.|:::|::::::::|::::::::|:::|.'.'.'.'.|
|,',',',',|---|--------|--------|---|,',',',',|
|.'.'.'.'.|:::|::::::::|::::::::|:::|.'.'.'.'.|
|.'.'.'.'.|---|--------|--------|---|.'.'.'.'.|
|.'.'.'.'.|=========================|.'.'.'.'.|
|.'.'.'.'.|%%%%%%%%%%%%%%%%%%%%%%%%%|.'.'.'.'.|
|.'.'.'.','       /%%%%%%%%%\       ','.'.'.'.|
|.'.'.','        /%%%%%%%%%%%\        ','.'.'.|
|.'.','         /%%%%%%%%%%%%%\         ','.'.|
|.','          /%%%%%%%%%%%%%%%\          ','.|
|;____________/%%%%%%%%%%%%%%%%%\____________;|
"""

# Sourced via https://www.asciiart.eu/art/619e9b9cbc49d3c1, author Shanaka Dias
DRAGON_REELING = r"""
             __                  __
            ( _)                ( _)
           / / \\              / /\_\_
          / /   \\            / / | \ \
         / /     \\          / /  |\ \ \
        /  /   ,  \ ,       / /   /|  \ \
       /  /    |\_ /|      / /   / \   \_\
      /  /  |\/ _ '_| \   / /   /   \    \\
     |  /   |/  0 \0\    / |    |    \    \\
     |    |\|      \_\_ /  /    |     \    \\
     |  | |/    \.\ o\o)  /      \     |    \\
     \    |     /\\`v-v  /        |    |     \\
      | \/    /_| \\_|  /         |    | \    \\
      | |    /__/_ `-` /   _____  |    |  \    \\
      \|    [__]  \_/  |_________  \   |   \    ()
       /    [___] (    \         \  |\ |   |   //
      |    [___]                  |\| \|   /  |/
     /|    [____]                  \  |/\ / / ||
    (  \   [____ /     ) _\      \  \    \| | ||
     \  \  [_____|    / /     __/    \   / / //
     |   \ [_____/   / /        \    |   \/ //
     |   /  '----|   /=\____   _/    |   / //
  __ /  /        |  /   ___/  _/\    \  | ||
 (/-(/-\)       /   \  (/\/\)/  |    /  | /
               (/\/\)           /   /   //
                      _________/   /    /
                     \____________/    (
"""

# Sourced via https://www.asciiart.eu/art/376a59d7692b8079, author Shanaka Dias
DRAGON_STATIC = r"""
 <>=======() 
(/\___   /|\\          ()==========<>_
      \_/ | \\        //|\   ______/ \)
        \_|  \\      // | \_/
          \|\/|\_   //  /\/
           (oo)\ \_//  /
          //_/\_\/ /  |
         @@/  |=\  \  |
              \_=\_ \ |
                \==\ \|\_
             __(\===\(  )\
            (((~) __(_/   |
                 (((~) \  /
                 ______/ /
                 '------'
"""

# Sourced via https://www.asciiart.eu/art/1833b5c2ffc7fafc, author Shanaka Dias, modified
DRAGON_CHARGING = r"""
          /                            )
          (                             |\
         /|                              \\
        //                                \\
       ///                                 \|
      /( \                                  )\
      \\  \_                               //)
       \\  :\__                           ///
        \\     )                         // \
         \\:  /                         // |/
          \\ / \                       //  \
           /)   \   ___..-'           (|  \_|
          //     /   _.'              \ \  \
         /|       \ \________          \ | /
        (| _ _  __/          '-.       ) /.'
         \\ .  '-.__            \_    / / \
          \\_'.     > --._ '.     \  / / /
           \ \      \     \  \     .' /.'
            \ \  '._ /     \ )    / .' |
             \ \_     \_   |    .'_/ __/
              \  \      \_ |   / /  _/ \_
               \  \       / _.' /  /     \
               \   |     /.'   / .'       '-,_
                \   \  .'   _.'_/             \
   /\    /\      ) ___(    /_.'           \    |
  | _\__// \    (.'      _/               |    |
  \/_  __  /--'`    ,                   __/    /
  ( b) /b)  \  '.   :            \___.-'_/ \__/
  /:/:  ,     ) :        (      /_.'__/-'|_ _ /
 /:/: __/\ >  __,_.----.__\    /        (/(/(/
(_(,_/V .'/--'    _/  __/ |   /
 VvvV  //`    _.-' _.'     \   \
   n_n//     (((/->/        |   /
   '--'         ~='          \  |
                              | |_,,,
                              \  \  /
                               '.__)
"""

# Sourced via https://www.asciiart.eu/art/627363361eda1a20, author unknown
UNICORN_STATIC = r"""
                              /
                   __       //
                   -\= \=\ //
                 --=_\=---//=--
               -_==/  \/ //\/--
                ==/   /O   O\==--
   _ _ _ _     /_/    \  ]  /--
  /\ ( (- \    /       ] ] ]==-
 (\ _\_\_\-\__/     \  (,_,)--
(\_/                 \     \-
\/      /       (   ( \  ] /)
/      (         \   \_ \./ )
(       \         \      )  \
(       /\_ _ _ _ /---/ /\_  \
 \     / \     / ____/ /   \  \
  (   /   )   / /  /__ )   (  )
  (  )   / __/ '---`       / /
  \  /   \ \             _/ /
  ] ]     )_\_         /__\/
  /_\     ]___\
 (___)
"""

# Sourced via https://www.asciiart.eu/art/b73d333aa387ff07, author Tua Xiong, modified
UNICORN_CHARGING = r"""
              ,,))))))));,
           __)))))))))))))),
\|/       -\(((((''''((((((((.
-*-==//////((''  .     `)))))),
/|\      ))| o    ;-.    '(((((                                  ,(,
         ( `|    /  )    ;))))'                               ,_))^;(~
            |   |   |   ,))((((_     _____------~~~-.        %,;(;(>';'~
            o__;   ;    )))(((` ~---~  `::           \      %%~~)(v;(`('~
                  ;    ''''````         `:       `:::|\,__,%%    );`'; ~
                 |   _                )     /      `:|`----'     `-'
           ______/\/~    |                 /        /
         /~;;.____/;;'  /          ___--,-(   `;;;/
        / //  _;______;'------~~~~~    /;;/\    /
       //  | |                        / ;   \;;,\
      (<_  | ;                      /',/-----'  _>
       \_| ||_                     //~;~~~~~~~~~
           `\_|                   (,~~
                                   \~\
                                    ~~
"""

# Sourced via https://www.asciiart.eu/art/4ac4be583e483ed5, author Colin J. Randall (CJRandall), modified
UNICORN_REELING = r"""
              \
               \
                \\
                 \\
                  >\`-_
              _.-(6'  \\
             (=___._/`'\\
                  )  \ `|)
                 /   /  '\)
               j    < _  `-\
           _.-' :      ``.  `
           \ r=._\        `.
          <`\\_  \         .`-.
           \ r-7  `-. ._  ' .  `\
            \`,      `-.`7  7)   )
             \/         \|  \'  / `-._
                        ||    .'
                         \\  (
                          >\  >
                      ,.-' >.'
                     <.'_.''
                       <'
"""

LINE_BREAK = "──────────────────────────────────────────────────────────"

PLAYER_START_HEALTH = 10

def Minigame(frog_name="Testing Frog"):
    slow_print("You enter the dungeon, the cold and dank air hitting your nose immediately.")
    slow_print("The walls are decrepit and detritus crumbles from them when touched.")
    slow_print("You hear distant sounds of crackling. Fire, falling stone, or something more sinister.")
    slow_print("The moisture in the air is so thick it coats your skin.")
    pause()
    print(CORRIDOR_SPLIT)
    slow_print("You begin forward into the dungeon, watching the light of outside fade behind you.")
    slow_print("The stone walls begin to become uniform as press on, occluded from the elements. Ahead, the path splits, both ways looking identical.")
    print("Only enter the letter corresponding to an action, as indicated by the parentheses. E.g. for (r)ight, enter 'r'.")

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
    pause(secs=1)
    slow_print(" barely dodging the unicorn's strike!")
    pause()
    slow_print("\nYou draw your sword and ready your stance. It's you or it.")
    pause(secs=1.5)
    # Begin first fight
    Fight_One(frog_name)

def Fight_One(frog_name):
    Combat(static=UNICORN_STATIC, charging=UNICORN_CHARGING, reeling=UNICORN_REELING, player_health_max=PLAYER_START_HEALTH, enemy_health_max=6, enemy_name="Unicorn")

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
        # This is probably better suited for like a dictionary or something, but the performance loss is so small that readability still wins
        if player_action == enemy_action:
            # "Clashes" where both characters pick the same option, no outcome
            if player_action == "s":
                combat_print("Both you and the beast lunge viciously at each other, your blade meeting its horn.")
                combat_print("Neither you nor the beast can overcome the other's strength and instead prepare the the next attack.")
                pause()
            elif player_action == "b":
                combat_print("You and the beast both brace yourselves for attack, only to be met by an odd stillness.")
                combat_print("When neither side moves, you loosen your grip on your shield and ready for the next opening.")
                pause()
            elif player_action == "f":
                # Slightly faster dialog since there's more of it
                combat_print("You flinch as your false attack is seemingly met with an attack from beast!", delay=0.017)
                pause(0.5)
                combat_print("At the last second, it pulls off its attack, for a moment seeming just as surprised as you.", delay=0.017)
                combat_print("Your mutual astonishment quickly fades and you ready yourself for the next window to attack.", delay=0.017)
                pause(0.5) # Reduced pause for double pauses
        # -- Player Advantage --
        elif player_action == "s" and enemy_action == "f":
            combat_print("The beast rears back in preperation for a larger strike, but your sword is already cutting through the air.")
            combat_print("The blade connects with flesh, staggering back the beast.")
            pause()
            # Advantage Menu
        elif player_action == "b" and enemy_action == "s":
            combat_print("The beast drives forward as you raise your shield.", delay=0.017)
            combat_print("You dig your feet into the ground as the strike connects, holding until you're finally still.", delay=0.017)
            combat_print("As soon as the beast's strike ends, you slam your shield forward, finding purchase against its face, granting you a precious window to strike.", delay=0.017)
            pause()
            # Advantage Menu
        elif player_action == "f" and enemy_action == "b":
            combat_print("You swipe your blade to the right with half strength, the beast immediately moving to counter.")
            combat_print("As it readies to block, you redirect the strike with full force, finding purchase in the beast's flesh, staggering it back.")
            pause()
            # Advantage Menu
        # -- Player Disadvantage --
        elif player_action == "s" and enemy_action == "b":
            combat_print("Your entire body shifts as you put your full weight into your attack.")
            combat_print("With so much momentum already invested, you can only watch helplessly as the beast blocks your blow, taking advantage of your poor stance to counter-attack.")
            pause()
            # Disadvantage Menu
        elif player_action == "b" and enemy_action == "f":
            combat_print("The beast steps back as it readies a strong swing, prompting you to raise your shield.")
            pause(0.5)
            combat_print("You stand there for a second, but when no attack slams against your shield, you peek your head over, only to see the true attack, now too late to stop.")
            pause(0.5)
            # Disadvantage Menu
        elif player_action == "f" and enemy_action == "s":
            combat_print("You swing your sword lazily, preparing to redirect the attack to avoid the beast's block, but the beast has no such intention.")
            combat_print("Your blade freezes as you feel its strike connect, only recovering fast enough to figure out how to escape worse consequences.")
            pause()
            # Disadvantage Menu
        # -- Error Case --
        else:
            slow_print("Something about your action caused an error.")
            pause()
            slow_print("Maybe something to discuss with the developer?")
            slow_print("Try again, but do something differently this time.")
            pause()

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

def slow_print(text, delay=0.027, newline=True):
    for ch in text: # I keep forgetting you don't need parentheses in python
        print(ch, end='', flush=True) # Flush needs to be true or messes up
        time.sleep(delay)
    if newline:
        print()

# Wrapper with fast default read, better for keeping tempo in combat
def combat_print(text, delay=0.02, newline=True):
    slow_print(text, delay=delay, newline=newline)

def pause(secs=0.7):
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
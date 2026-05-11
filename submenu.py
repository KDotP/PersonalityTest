# Since I've decided to make the test available as an exe, I don't think I'm going to try to conceal the context anymore :)
import time

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
DRAGON_INTRO = r"""
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
DRAGON_FLYING = r"""
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
DRAGON_FLYING_CLOSE = r"""
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

LINE_BREAK = "──────────────────────────────────────────────────────────"

def Minigame(frog_name):
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
    else:
        slow_print("right, lit now only by your torch.")
    pause()
    slow_print("As you press onward, a chalky mass flickers at the edge of your light.")
    slow_print("You extend your torch forward, bringing the flame closer, catching the hollow eyes of a skull.")
    slow_print("Before you can react, the undead creature turns to face you. Its hands fly forward, fingers shaped like claws.")
    pause()
    slow_print("\nYou draw your sword and ready your stance. It's you or it.")
    pause(secs=1.5)
    # Begin skeleton fight
    Fight_One()

def Fight_One():
    print()

def slow_print(text, delay=0.03, newline=True):
    for ch in text: # I keep forgetting you don't need parentheses in python
        print(ch, end='', flush=True)
        time.sleep(delay)
    if newline:
        print()

def pause(secs=0.7):
    time.sleep(secs)

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
    print("Main Testing Function")
    Minigame("Testing Frog")

main()
# This file does not contain any code, but contains all the sprites for the dungeon crawler minigame
# This is done to reduce file size and make editing easier
# Credits for each ASCII art image is above the variable (except for the dictionary at the end)

LINE_BREAK = "──────────────────────────────────────────────────────────"

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

# Sourced via https://www.asciiart.eu/art/23319246a6009130, author Tim Spicer (Darkstar), modified
CORRIDOR_BRANCHING = r"""
 _____________________________________________
|.'',                                     ,''.|
|.'.'',                                 ,''.'.|
|.'.'.'',                             ,''.'.'.|
|.'.'.'.'',                         ,''.'.'.'.|
|.'.'.'.'.|                         |.'.'.'.'.|
|.'.'.'.'.|===;                 ;===|.'.'.'.'.|
|.'.'.'.'.|:::|',             ,'|:::|.'.'.'.'.|
|.'.'.'.'.|---|'.|, _______ ,|.'|---|.'.'.'.'.|
|.'.'.'.'.|:::|'.|'|-|   |-|'|.'|:::|.'.'.'.'.|
|,',',',',|---|',|'|-|  .|-|'|,'|---|,',',',',|
|.'.'.'.'.|:::|'.|'|-|   |-|'|.'|:::|.'.'.'.'.|
|.'.'.'.'.|---|','   /%%%\   ','|---|.'.'.'.'.|
|.'.'.'.'.|===:'    /%%%%%\    ':===|.'.'.'.'.|
|.'.'.'.'.|%%%%%%%%%%%%%%%%%%%%%%%%%|.'.'.'.'.|
|.'.'.'.','       /%%%%%%%%%\       ','.'.'.'.|
|.'.'.','        /%%%%%%%%%%%\        ','.'.'.|
|.'.','         /%%%%%%%%%%%%%\         ','.'.|
|.','          /%%%%%%%%%%%%%%%\          ','.|
|;____________/%%%%%%%%%%%%%%%%%\____________;|
"""

# Sourced via https://www.asciiart.eu/art/23319246a6009130, author Tim Spicer (Darkstar), heavily modified
CORRIDOR_STRAIGHT = r"""
 _____________________________________________
|.'',                                     ,''.|
|.'.'',                                 ,''.'.|
|.'.'.'',                             ,''.'.'.|
|.'.'.'.'',                         ,''.'.'.'.|
|.'.'.'.'.'',                     ,''.'.'.'.'.|
|.'.'.'.'.'.'',                 ,''.'.'.'.'.'.|
|.'.'.'.'.'.'.'',             ,''.'.'.'.'.'.'.|
|.'.'.'.'.'.'.'.'',         ,''.'.'.'.'.'.'.'.|
|.'.'.'.'.'.'.'.'.'',     ,''.'.'.'.'.'.'.'.'.|
|,',',',',',',',',','  ^  ',',',',',',',',',',|
|.'.'.'.'.'.'.'.'.'   /%\   '.'.'.'.'.'.'.'.'.|
|.'.'.'.'.'.'.','    /%%%\    ','.'.'.'.'.'.'.|
|.'.'.'.'.'.','     /%%%%%\     ','.'.'.'.'.'.|
|.'.'.'.'.','      /%%%%%%%\      ', .'.'.'.'.|
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

# Sourced via https://www.asciiart.eu/art/8b0e61f1b343f4e2, author Unknown
DRAGON_AIRBORNE = r"""
       \`----.__                 ____               
        |       `--._         <=/  , *--,           
        /_             `-.    ,/  / `````            
          \__             (_.'  ,'                   
             \__ ......'       \___----^__           
          _./               ,'           `.         
|\     _.'   ___/ )\...._"   ___           \        
| \__.'  __.'            `""'   `""`.'""``--\       
\____.-'      
"""

# Sourced via https://www.asciiart.eu/art/0af5287cc6a700df, author BluePard
GRYPHON_STATIC = r"""
                 /i
                //,
               ///i 
             ,/ ).'i    
              |   )-i  
              |   )i 
              '   )i
             /    |- 
        _.-./-.  /z_ 
         `-. >._\ _ );i.
          / `-'/`k-'`u)-'`
         /    )-     
  ,.----'   ) '                       
  /      )1`  
 ///v`-v\v        
/v
"""

# Sourced via https://www.asciiart.eu/art/1439a2d47a4340e2, authors John van der Zwaag / VanderZwaag / Vanderz
GRYPHON_REELING = r"""
                        ______
             ______,---'__,---'
         _,-'---_---__,---'
  /_    (,  ---____',
 /  ',,   `, ,-'
;/)   ,',,_/,'
| /\   ,.'//\
`-` \ ,,'    `.
     `',   ,-- `.
     '/ / |      `,         _
     //'',.\_    .\\      ,{==>-
  __//   __;_`-  \ `;.__,;'
((,--,) (((,------;  `--'
```  '   ```
"""

# Sourced via https://www.asciiart.eu/art/0dfe2a759afdcfd7, author Joan G. Stark (Spunk)
GRYPHON_CHARGING = r"""
        _____,    _..-=-=-=-=-====--,
     _.'a   /  .-',___,..=--=--==-'`
    ( _     \ /  //___/-=---=----'
     ` `\    /  //---/--==----=-'
  ,-.    | / \_//-_.'==-==---='
 (.-.`\  | |'../-'=-=-=-=--'
  (' `\`\| //_|-\.`;-~````~,        _
       \ | \_,_,_\.'        \     .'_`\
        `\            ,    , \    || `\\
          \    /   _.--\    \ '._.'/  / |
          /  /`---'   \ \   |`'---'   \/
         / /'          \ ;-. \
      __/ /           __) \ ) `|
    ((='--;)         (,___/(,_/
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
                        ||    .'      `
                         \\  (
                          >\  >
                      ,.-' >.'
                     <.'_.''
                       <'
"""

# Combat outcomes dictionary
combat_events = {
    # --- Clashes ---
    ("s", "s"): {
        "lines": [
            ("Both you and the beast lunge viciously at each other, your blade meeting its own strike."),
            ("Neither you nor the beast can overcome the other's strength and instead prepare the next attack."),
        ],
        "result": "clash",
    },

    ("b", "b"): {
        "lines": [
            ("You and the beast both brace yourselves for attack, only to be met by an odd stillness."),
            ("When neither side moves, you loosen your grip on your shield and ready for the next opening."),
        ],
        "result": "clash",
    },

    ("f", "f"): {
        "lines": [
            ("You flinch as your false attack is seemingly met with an attack from the beast!"),
            ("At the last second, it pulls off its attack, for a moment seeming just as surprised as you."),
            ("Your mutual astonishment quickly fades and you ready yourself for the next window to attack."),
        ],
        "result": "clash",
    },

    # --- Player Advantage ---
    ("s", "f"): {
        "lines": [
            ("The beast rears back in preparation for a larger strike, but your sword is already cutting through the air."),
            ("The blade connects with flesh, staggering back the beast."),
        ],
        "result": "advantage",
    },

    ("b", "s"): {
        "lines": [
            ("The beast drives forward as you raise your shield."),
            ("You dig your feet into the ground as the strike connects, holding until you're finally still."),
            ("As soon as the beast's strike ends, you slam your shield forward, finding purchase against its face, granting you a precious window to strike."),
        ],
        "result": "advantage",
    },

    ("f", "b"): {
        "lines": [
            ("You swipe your blade to the right with half strength, the beast immediately moving to counter."),
            ("As it readies to block, you redirect the strike with full force, finding purchase in the beast's flesh, staggering it back."),
        ],
        "pause": 1,
        "result": "advantage",
    },

    # --- Player Disadvantage ---
    ("s", "b"): {
        "lines": [
            ("Your entire body shifts as you put your full weight into your attack."),
            ("With so much momentum already invested, you can only watch helplessly as the beast blocks your blow, taking advantage of your poor stance to counter-attack."),
        ],
        "result": "disadvantage",
    },

    ("b", "f"): {
        "lines": [
            ("The beast steps back as it readies a strong swing, prompting you to raise your shield."),
            ("You stand there for a second, but when no attack slams against your shield, you peek your head over, only to see the true attack, now too late to stop."),
        ],
        "result": "disadvantage",
    },

    ("f", "s"): {
        "lines": [
            ("You swing your sword lazily, preparing to redirect the attack to avoid the beast's block, but the beast has no such intention."),
            ("Your blade freezes as you feel its strike connect, only recovering fast enough to figure out how to escape worse consequences."),
        ],
        "result": "disadvantage",
    },

    # --- Advantage Actions ---
    ("c", "r"): {
        "lines": [
            ("The beast retreats, but you're already moving, your blade high."),
            ("Your blade plunges into flesh, blood already flowing freely from the fresh wound."),
            ("The beast can only retreat further, drawing the blade from its body and readying for the next attack."),
        ],
        "result": "success", # successful advantage strike
    },

    ("c", "d"): {
        "lines": [
            ("You dive your sword forward, but the beast has already dug in, fighting aside your blade."),
            ("Before it can strike in revenge for its fresh wound, you've backed off, readying for the next oppertunity."),
        ],
        "result": "failure",
    },

    ("h", "r"): {
        "lines": [
            ("Your blade rises above your head, ready to plunge down onto its victim."),
            ("Before you can take your prize, the creature backs off, clearing your blade's path."),
            ("Frustrated, you lower your sword and return to a more neutral stance."),
        ],
        "result": "failure",
    },

    ("h", "d"): {
        "lines": [
            ("The beast readies itself, already defensive of its new wound."),
            ("While it lowers to make a more steady defender, your blade is already towering above."),
            ("With a single swift motion, you bring the blade down on the creature, shearing fleshing from body."),
            ("It backs off, breathing heavily and readying for the next blow."),
        ],
        "result": "success",
    },

    # --- Disadvantage Actions ---
    ("r", "c"): {
        "lines": [
            ("You do your best to avoid another blow, but the last has already taken its toll on your agility."),
            ("Your skin ignite with pain as you add another wound to your body, barely managing to pull away enough to spare yourself any further punishment."),
        ],
        "result": "failure", # unsuccessful defensisve action
    },

    ("r", "h"): {
        "lines": [
            ("Adrenaline courses through your viens, driving your feet without conscious mind."),
            ("You barely evade attack after attack until you're far enough to raise your own weapon."),
        ],
        "result": "success",
    },

    ("d", "c"): {
        "lines": [
            ("You lower your body, bringing yourself closer to the ground and steadying in preperation for the next strike."),
            ("The beast is quickly on you again, but its charge stalls as your shield deflects several strikes until you spot an oppertunity to fight back."),
        ],
        "result": "success",
    },

    ("d", "h"): {
        "lines": [
            ("Your feet slip against the rough rock floors of the dungeon, costing you valuable attention and agility."),
            ("Before you can restore your stance, another blow lands, the cold dungeon air meeting your bloodstream."),
            ("You grimace in pain, but manage to recover your stance and ready for the next chance to get revenge."),
        ],
        "result": "failure",
    },
}

# ------ Dragon combat events, uses different dialog ------

dragon_combat_events = {
    # --- Clashes ---
    ("s", "s"): {
        "lines": [
            ("You thrust you sword forward, finding nothing but air as the dragon rises above you, its claws already trained on you."),
            ("Sparks fly from your sword as the steel scrapes against its talons, barely managing to fight them off as you get ready to strike again."),
        ],
        "result": "clash",
    },

    ("b", "b"): {
        "lines": [
            ("You ready your shield, ready to block another billow of flame."),
            ("The two of you circle each other, navigating the piles of coins without glancing away from each other, but neither of you dare to strike."),
        ],
        "result": "clash",
    },

    ("f", "f"): {
        "lines": [
            ("You fake a swipe at the dragon, but it deflects your sword with a claw before you can adjust your swing."),
            ("The creature glares down at you in what could almost be interpreted as mockery, but it does nothing to follow up."),
        ],
        "result": "clash",
    },

    # --- Player Advantage ---
    ("s", "f"): {
        "lines": [
            ("The dragon slams its head forward, teeth snapping at you, but you narrowly evade."),
            ("Your sword thrusts forward, finding a tender-looking section of its jaw and digging as far into as your blade can reach."),
            ("The monster screetches, recoiling back, hot smoke billowing from its nostrils."),
        ],
        "result": "advantage",
    },

    ("b", "s"): {
        "lines": [
            ("You pull your shield up just in time to block the stream of flames being spewed from the dragon's mouth."),
            ("When the flames subside, you rush foward, closing the distance and stabbing into the dragon."),
        ],
        "result": "advantage",
    },

    ("f", "b"): {
        "lines": [
            ("You fake a bash from your shield, the dragon swatting it away."),
            ("However, the true attack lies behind, your sword already stabbing into flesh."),
        ],
        "pause": 1,
        "result": "advantage",
    },

    # --- Player Disadvantage ---
    ("s", "b"): {
        "lines": [
            ("You lunge forward with all your strength, your sword aimed straight for the dragon's chest."),
            ("Before the strike can land, one of its massive claws bats your blade aside, leaving your balance broken and your guard open for its counter-attack."),
        ],
        "result": "disadvantage",
    },

    ("b", "f"): {
        "lines": [
            ("The dragon pulls back, smoke curling from its nostrils as you raise your shield to meet another burst of flame."),
            ("You wait for the fire to come, but instead its tail lashes around your guard, striking before you can react."),
        ],
        "result": "disadvantage",
    },

    ("f", "s"): {
        "lines": [
            ("You feint with your sword, expecting the dragon to shift into a defensive stance."),
            ("Instead, it surges forward without hesitation, its claws crashing into you before you can recover your footing."),
        ],
        "result": "disadvantage",
    },

    # --- Advantage Actions ---
    ("c", "r"): {
        "lines": [
            ("The dragon pulls back across its hoard, but you press forward without hesitation."),
            ("Your blade drives between its scales, drawing a fresh stream of blood onto the gold beneath your feet."),
            ("With an enraged roar, the dragon tears itself free and retreats, smoke spilling from its jaws as it prepares to strike again."),
        ],
        "result": "success", # successful advantage strike
    },

    ("c", "d"): {
        "lines": [
            ("You thrust your sword toward the dragon's wounded side, but it braces itself behind folded wings and hardened scales."),
            ("Your strike glances away harmlessly, and you quickly retreat before its claws can punish your mistake."),
        ],
        "result": "failure",
    },

    ("h", "r"): {
        "lines": [
            ("You raise your blade high, ready to bring it down on the dragon's exposed flesh."),
            ("But the creature recoils just in time, its great body sliding back across the treasure-strewn floor."),
            ("You lower your sword with frustration, forced to wait for another opening."),
        ],
        "result": "failure",
    },

    ("h", "d"): {
        "lines": [
            ("The dragon lowers itself, protecting its fresh wound as it prepares to endure your next strike."),
            ("But your sword is already descending, aimed with all the strength you can muster."),
            ("Steel bites through scale and flesh alike, tearing a cry of pain from the beast."),
            ("The dragon stumbles back, breathing heavily as it readies itself for the next exchange."),
        ],
        "result": "success",
    },

    # --- Disadvantage Actions ---
    ("r", "c"): {
        "lines": [
            ("You scramble backward, but your last wound slows your every movement."),
            ("The dragon surges after you, claws and flame leaving fresh pain behind before you barely escape its reach."),
        ],
        "result": "failure", # unsuccessful defensive action
    },

    ("r", "h"): {
        "lines": [
            ("Adrenaline drives your legs as you flee across the dragon's glittering hoard."),
            ("You narrowly evade snapping jaws and slashing claws until enough distance opens for you to raise your weapon once more."),
        ],
        "result": "success",
    },

    ("d", "c"): {
        "lines": [
            ("You steady your footing among the scattered coins, lowering your shield as the dragon charges."),
            ("Its assault crashes against your guard, and through the force of claws and flame, you find a brief opening to fight back."),
        ],
        "result": "success",
    },

    ("d", "h"): {
        "lines": [
            ("Your footing slips across the loose treasure beneath you, costing you precious balance."),
            ("Before you can recover, the dragon's strike tears into you, its fury cutting deeper than steel."),
            ("You grit your teeth through the pain and force yourself back into a fighting stance."),
        ],
        "result": "failure",
    },
}

MOMENTUM_DESC = {
    0: "You are being overrun, taking 1 damage per turn!",
    1: "You're at a disadvantage, your advantage attacks deal 1 less damage when successful.",
    2: "Your sword stands ready.",
    3: "You're beginning to find your footing, unsuccessful advantage attacks still deal 1 damage.",
    4: "Your advantage is growing! Matched attacks deal 1 damage, but do not put you in advantage.",
    5: "You're dominating the fight! Matched attacks now put you into advantage!",
}
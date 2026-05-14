import time, random
import REFERENCE

# The main file was just growing too large to be editable easily
"""
    Dragon Combat Design:
    Keep the existing clash phase, but add on new options and things that need to be tackled (and also repeat detection)
    Momentum provides advantages or debuffs depending on how much or how little momentum each side has
    Momentum is measured as a staggered tug-of-war where there are only 5 points of momentum, meaning that if all claimed, gaining another point comes at the cost of the opponent's momentum
    Not all momentum may be 'claimed' at any given time, meaning that taking it does not take from the other side
    Example: [YOU █|░░|██ DRAGON] or [YOU ███|██ DRAGON]
    Having 0 momentum keeps you on the backfoot, taking 1 damage every action. This includes advantage and disadvantage states, forcing a decision between defending/attacking or removing the constant debuff
    Having 1 momentum lowers successful advantage attack damage from 2 to 1
    Having 2 momentum is the current game state where you are no longer disadvantaged
    Having 3 momentum makes it so unsuccessful advantage attacks still do 1 extra damage
    Having 4 momentum allows you to still deal 1 damage on matching attacks, but does not put you into advantage
    Having 5 momentum means you have all the momentum! Matching attacks now puts you into advantage state and the winning side gains a special attack that can expend momentum for big damage

    At half dragon health, add 2 extra unclaimed momentum to a total of 7? Probably be a bad idea

    Momentum also presents a difficult challenge where gaining it takes away oppertunities to either defend or attack

    Non-Specific Momentum Actions:
    Overwhelm (Advantage, no cooldown): Spend 1 momentum to guarantee advantage attack does full damage
    Counter-Attack (Disadvantage, no cooldown): Spend 1 momentum to guarantee disadvantage defence fails
    * If both sides choose their respective force action, they resolve to deal 1 damage to the disadvantage player 
    
    Player-Specific Momentum Actions:
    Shield Bash (Clash, 1 clash cooldown): Reduce momentum by 1 both sides, resets to a new clash
    Hold Ground (Advantage, no cooldown): Gain 1 momentum, but deal no damage
    Overextend (Clash, 2 clash cooldown): Gain up 2 unclaimed momentum, always lose clash and take 1 extra damage
    Go For the Heart (Clash, at 5 momentum): Deal 4 unblockable damage and lose 2 momentum

    Dragon-Specific Momentum Actions:
    Wing Buffet (Advantage, 2 clash cooldown): Steal 1 momentum, but deal no damage
    Headbutt (Disadvantage, 2 clash cooldown, while down momentum): Lose 1 momentum, player loses 2 momentum, still take full hit
    Glare (Clash, 2 clash cooldown, while unclaimed momentum): Gain 1 unclaimed momentum, deals no damage, but player action also fails (even cooldown actions)
    Take Flight (Advantage, 2 clash cooldown, while up momentum, weighted favorably):  Requires 3+ momentum, reset momentum to 2, deal no damage, battle enters a temporary "Dragonflight" state for 2 turns
    * Dragonflight stages do not recover cooldown
    * Player can select from several new choices
    ** Take Breath: Gain 1 unclaimed momentum
    ** Take Cover: Take no damage
    ** Run: Dragon loses 1 momentum, to a minimum of 1 (does not affect dragonflight turns)
    ** Find High Ground: Reduce final dive damage by 2
    ** Taunt: Player gains 1 momentum, dive resolves immediately (allows the player to go from 2-3 momentum at the start (to 2-2) to 4-1 at the end if taking breath first, still take the chip damage)
    * The player takes 1 damage from fire breath each turn if they do not take cover
    * At the end of Dragonflight, the dragon dives, dealing 1 damage for each momentum lost when using Take Flight
    * Design for Dragonflight UI:
    line_break()
    [First/Second Turn](The dragon is flying overhead, spraying fire at you!)(The dragon looks like it's about to dive!)
    You're taking 1 damage per turn from fire! The final strike in (1/2) turn(s) will do X damage!

    [B] Take Breath — Gain 1 Unclaimed Momentum
    [C] Take Cover — Take no fire damage this turn
    [R] Run — Dragon Loses 1 Momentum (can only be used once!)
    [H] Find High Ground — Reduce Final Dive Damage by 2
    [T] Taunt — Gain 1 Momentum, Resolve Dive Immediately (does not dodge fire damage)
    """

# Programmed with the help of AI since I really didn't want to have to reprogram everything from scratch for a hidden side game in a silly personality test
def Dragon_Combat(static="S", charging="C", reeling="R", player_health_max=10, enemy_health_max=20, enemy_name="Invalid Dragon"): 
    MOMENTUM_TOTAL = 5

    # Cooldown maximums
    SHIELD_BASH_CD_MAX = 1
    OVEREXTEND_CD_MAX = 2
    WING_BUFFET_CD_MAX = 2
    HEADBUTT_CD_MAX = 2
    GLARE_CD_MAX = 2
    TAKE_FLIGHT_CD_MAX = 2
 
    enemy_health_current  = enemy_health_max
    player_health_current = player_health_max
    player_momentum       = 2
    dragon_momentum       = 2
    # unclaimed is always derived: MOMENTUM_TOTAL - player_momentum - dragon_momentum
 
    # Cooldowns count down by 1 each time a clash fully resolves (0 = ready).
    # Dragonflight turns do not tick cooldowns.
    shield_bash_cd  = 0
    overextend_cd   = 0
    wing_buffet_cd  = 0
    headbutt_cd     = 0
    glare_cd        = 0
    take_flight_cd  = 0
 
    # ------------------------------------------------------------------ momentum helpers
 
    def unclaimed():
        return MOMENTUM_TOTAL - player_momentum - dragon_momentum
 
    def momentum_bar():
        unc = unclaimed()
        if player_momentum + dragon_momentum != MOMENTUM_TOTAL:
            return f"[YOU {player_momentum} {'█' * player_momentum}|{'░' * unc}|{'█' * dragon_momentum} {dragon_momentum} DRAGON]"
        else:
            return f"[YOU {player_momentum} {'█' * player_momentum}|{'█' * dragon_momentum} {dragon_momentum} DRAGON]" # Do not add 2 bars
 
    def player_gain(amount):
        """Player gains: claims from unclaimed first, then steals from dragon."""
        nonlocal player_momentum, dragon_momentum
        for _ in range(amount):
            if unclaimed() > 0:
                player_momentum += 1
            elif dragon_momentum > 0:
                dragon_momentum -= 1
                player_momentum += 1
 
    def dragon_gain(amount):
        """Dragon gains: claims from unclaimed first, then steals from player."""
        nonlocal player_momentum, dragon_momentum
        for _ in range(amount):
            if unclaimed() > 0:
                dragon_momentum += 1
            elif player_momentum > 0:
                player_momentum -= 1
                dragon_momentum += 1
 
    def player_steal(amount):
        """Player steals from dragon directly; falls back to unclaimed if dragon is at 0."""
        nonlocal player_momentum, dragon_momentum
        for _ in range(amount):
            if dragon_momentum > 0:
                dragon_momentum -= 1
                player_momentum += 1
            elif unclaimed() > 0:
                player_momentum += 1
 
    def dragon_steal(amount):
        """Dragon steals from player directly; falls back to unclaimed if player is at 0."""
        nonlocal player_momentum, dragon_momentum
        for _ in range(amount):
            if player_momentum > 0:
                player_momentum -= 1
                dragon_momentum += 1
            elif unclaimed() > 0:
                dragon_momentum += 1
 
    def player_release(amount):
        """Player releases claimed momentum back to unclaimed."""
        nonlocal player_momentum
        player_momentum = max(0, player_momentum - amount)
 
    def dragon_release(amount):
        """Dragon releases claimed momentum back to unclaimed."""
        nonlocal dragon_momentum
        dragon_momentum = max(0, dragon_momentum - amount)
 
    # ------------------------------------------------------------------ display / misc
 
    def display_stats():
        line_break()
        print(f"        {enemy_name}             {hp_bar(enemy_health_current, enemy_health_max)}")
        line_break()
        print(f"        YOU                    {hp_bar(player_health_current, player_health_max)}")
        line_break()
        print(f"        MOMENTUM               {momentum_bar()}")
        line_break()
 
    def tick_cooldowns():
        nonlocal shield_bash_cd, overextend_cd, wing_buffet_cd, headbutt_cd, glare_cd, take_flight_cd
        shield_bash_cd  = max(0, shield_bash_cd  - 1)
        overextend_cd   = max(0, overextend_cd   - 1)
        wing_buffet_cd  = max(0, wing_buffet_cd  - 1)
        headbutt_cd     = max(0, headbutt_cd     - 1)
        glare_cd        = max(0, glare_cd        - 1)
        take_flight_cd  = max(0, take_flight_cd  - 1)
 
    # ------------------------------------------------------------------ dragon AI
 
    def dragon_choose_special(phase):
        if phase == "advantage":
            if take_flight_cd == 0 and dragon_momentum >= 3 and random.random() < 0.50:
                return "take_flight"
            if wing_buffet_cd == 0 and random.random() < 0.30:
                return "wing_buffet"
        elif phase == "disadvantage":
            if headbutt_cd == 0 and dragon_momentum <= 2 and random.random() < 0.30:
                return "headbutt"
        elif phase == "clash":
            if glare_cd == 0 and unclaimed() > 0 and random.random() < 0.30:
                return "glare"
        return None
 
    # ------------------------------------------------------------------ input menus
 
    def prompt(valid):
        while True:
            action = input("> ").strip().lower()
            if action in valid:
                return action
            combat_print("Invalid action! Enter only the letter shown in brackets.")
            pause(0.75)
 
    def clash_menu():
        display_stats()
        print("What will you do?")
        print("[S] Slash            [B] Block         [F] Feint")
        valid = {"s", "b", "f"}
        if shield_bash_cd == 0 and player_momentum > 0:
            print("[X] Shield Bash      (both sides lose 1 momentum, return to clash)")
            valid.add("x")
        if overextend_cd == 0 and unclaimed() > 0:
            print(f"[E] Overextend       (claim up to 2 unclaimed momentum [{unclaimed()} available], always lose clash + 1 dmg)")
            valid.add("e")
        if player_momentum == 5:
            print("[G] Go For the Heart (4 unblockable damage, lose 2 momentum)")
            valid.add("g")
        print()
        return prompt(valid)
 
    def advantage_menu():
        display_stats()
        print("The dragon is reeling! Press the advantage!")
        print("[C] Charge            [K] Kite          [H] Heavy Attack")
        print("[L] Hold Ground       (gain 1 momentum, deal no damage)")
        valid = {"c", "k", "h", "l"}
        if player_momentum > 0:
            print("[O] Overwhelm         (lose 1 momentum, guarantee full advantage damage)")
            valid.add("o")
        print()
        return prompt(valid)
 
    def disadvantage_menu():
        display_stats()
        print("You're on the backfoot! How will you defend?")
        print("[R] Retreat            [D] Dig In")
        valid = {"r", "d"}
        if player_momentum > 0:
            print("[A] Counter-Attack    (lose 1 momentum, guarantee your defence holds)")
            valid.add("a")
        print()
        return prompt(valid)
 
    # ------------------------------------------------------------------ Dragonflight
 
    def run_dragonflight(dive_damage):
        nonlocal player_health_current
        run_used    = False
        high_ground = False
 
        for turn in range(1, 3):
            line_break()
            if turn == 1:
                combat_print("The dragon is flying overhead, spraying fire at you!")
            else:
                combat_print("The dragon looks like it's about to dive!")
            current_dive = max(0, dive_damage - (2 if high_ground else 0))
            combat_print(f"You're taking 1 damage per turn from fire! The final dive in {3 - turn} turn(s) will do {current_dive} damage!")
            print()
            print("[B] Take Breath      — Gain 1 Momentum")
            print("[C] Take Cover       — Take no fire damage this turn")
            if not run_used:
                print("[R] Run              — Dragon loses 1 Momentum to a minimum of 1 (once only!)")
            print("[H] Find High Ground — Reduce final dive damage by 2")
            print("[T] Taunt            — Gain 1 Momentum, resolve dive immediately")
            print()
 
            valid = {"b", "c", "h", "t"}
            if not run_used:
                valid.add("r")
            action = prompt(valid)
 
            take_fire = True
            if action == "b":
                combat_print("You steady your breathing despite the heat, finding a sliver of composure.")
                player_gain(1)
            elif action == "c":
                combat_print("You throw yourself behind a heap of coins, the flames washing harmlessly overhead.")
                take_fire = False
            elif action == "r":
                combat_print("You sprint away, forcing the dragon to bank wide and lose its rhythm.")
                if dragon_momentum > 1:
                    dragon_release(1)
                run_used = True
            elif action == "h":
                combat_print("You scramble onto a raised mound of treasure, gaining precious elevation.")
                high_ground = True
            elif action == "t":
                combat_print("You raise your blade and scream a challenge at the sky. The dragon's eyes lock on you — it can't resist.")
                player_gain(1)
                combat_print("The dragon's fire breath washes over you, searing your skin! (-1 HP)")
                player_health_current -= 1
                if player_health_current <= 0:
                    return False
                break   # dive resolves immediately
 
            if take_fire:
                combat_print("The dragon's fire breath washes over you, searing your skin! (-1 HP)")
                player_health_current -= 1
                if player_health_current <= 0:
                    return False
            pause(1)
 
        # Dive resolves
        final_damage = max(0, dive_damage - (2 if high_ground else 0))
        if final_damage > 0:
            combat_print(f"The dragon plunges from the sky — the impact sends you skidding across the coins! (-{final_damage} HP)")
            player_health_current -= final_damage
            if player_health_current <= 0:
                return False
        else:
            combat_print("The dragon dives, but the high ground you claimed absorbs the blow!")
        pause(1)
        return True
 
    # ================================================================ main loop
 
    while True:
 
        # -- Passive debuff at 0 player momentum --
        if player_momentum == 0:
            line_break()
            combat_print("You're on the strong backfoot, the dragon has overwhelmed your defences! (-1 HP)")
            player_health_current -= 1
            if player_health_current <= 0:
                return False
 
        # ======== CLASH PHASE ========
        print(static)
        player_action = clash_menu()
 
        # Go For the Heart
        if player_action == "g":
            combat_print("You pour every scrap of momentum into one desperate, crushing blow — straight for the heart!")
            pause(0.5)
            combat_print("The dragon has no answer. The strike punches through scale and bone.")
            enemy_health_current -= 4
            player_release(2)
            tick_cooldowns()
            if enemy_health_current <= 0:
                return True
            continue
 
        # Shield Bash — both sides release 1 to unclaimed
        if player_action == "x":
            combat_print("You slam your shield into the dragon's jaw, disrupting its momentum — and your own.")
            pause(1.5)
            player_release(1)
            dragon_release(1)
            shield_bash_cd = SHIELD_BASH_CD_MAX
            tick_cooldowns()
            continue
 
        # Overextend — claim up to 2 unclaimed only (no stealing), always lose clash
        if player_action == "e":
            gain = min(2, unclaimed())
            combat_print("You overextend wildly, taking an advantagous position, but leave yourself wide open!")
            combat_print("You're helpless to block as the dragon attacks!")
            pause(1.5)
            player_momentum += gain
            player_health_current -= 1 # Take one more damage due to disadvantage state
            overextend_cd = OVEREXTEND_CD_MAX
            tick_cooldowns()
            # Dragon wins automatically, enter player disadvantage
            outcome = "overwhelmed"
 
        # Dragon Glare — requires unclaimed > 0; dragon claims 1 unclaimed, player action nullified
        dragon_special = dragon_choose_special("clash")
        if dragon_special == "glare" and glare_cd == 0:
            combat_print("The dragon fixes you with a searing stare, its eyes glowing like coals. Your action falters!")
            combat_print("While you're transfixed, it shifts its weight, pressing its advantage.")
            pause(1.5)
            dragon_momentum += 1   # direct claim from unclaimed (guard already ensured unclaimed > 0)
            glare_cd = GLARE_CD_MAX
            tick_cooldowns()
            continue
 
        # Normal clash resolution
        if player_action != "e": # overwhelm fix
            enemy_action = random_attack("static")
            outcome = run_event(player_action, enemy_action)
 
        if outcome == "clash":
            if player_momentum == 5:
                combat_print("Your overwhelming momentum carries through, fighting past the dragon's defence!")
                outcome = "advantage"
            elif player_momentum >= 4:
                combat_print("Your momentum advantage lets you eke out a scratch on the dragon despite the stalemate!")
                enemy_health_current -= 1
                if enemy_health_current <= 0:
                    tick_cooldowns()
                    return True
 
        tick_cooldowns()
 
        # ======== ADVANTAGE PHASE ========
        if outcome == "advantage":
            enemy_health_current -= 1
            if enemy_health_current <= 0:
                return True
 
            print(reeling)
            player_action = advantage_menu()
 
            if player_action == "l":   # Hold Ground — gain 1
                combat_print("You hold your position, letting the dragon reset while you bank the momentum.")
                player_gain(1)
                pause(1.5)
                continue
 
            if player_action == "o":   # Overwhelm — release 1, guarantee full damage
                combat_print("You channel everything into the strike, momentum surging through your blade!")
                player_release(1)
                enemy_health_current -= 2
                pause(1.5)
                if enemy_health_current <= 0:
                    return True
                continue
 
            dragon_special = dragon_choose_special("advantage")
 
            if dragon_special == "take_flight" and take_flight_cd == 0:
                released = max(0, dragon_momentum - 2)
                player_momentum = 2
                dragon_momentum = 2
                combat_print("With a deafening beat of its wings the dragon vaults upward, snatching back the initiative!")
                take_flight_cd = TAKE_FLIGHT_CD_MAX
                pause(1.5)
                if not run_dragonflight(released):
                    return False
                continue
 
            if dragon_special == "wing_buffet" and wing_buffet_cd == 0:
                combat_print("Before you can capitalise, the dragon's wing catches you full in the chest, faultering your position!")
                dragon_steal(1)
                wing_buffet_cd = WING_BUFFET_CD_MAX
                pause(1.5)
                continue
 
            if player_action == "k":   # Kite — always 1 damage, uncounterable
                combat_print("You hold your momentum, scoring several more cuts and bruises before the chase is over and you're back to even footing.")
                pause()
                enemy_health_current -= 1
                if enemy_health_current <= 0:
                    return True
            else:
                adv_outcome = run_event(player_action, random_attack("advantage"))
                if adv_outcome == "success":
                    enemy_health_current -= 1 if player_momentum <= 1 else 2
                    if enemy_health_current <= 0:
                        return True
                elif adv_outcome == "failure" and player_momentum >= 3:
                    combat_print("Even missing your mark, your momentum carries the blow far enough to draw blood.")
                    enemy_health_current -= 1
                    if enemy_health_current <= 0:
                        return True
 
        # ======== DISADVANTAGE PHASE ========
        elif outcome == "disadvantage" or outcome == "overwhelmed":
            player_health_current -= 1
            if player_health_current <= 0:
                return False
 
            print(charging)
            player_action = disadvantage_menu()
 
            if player_action == "a":   # Counter-Attack — release 1, guarantee defence
                combat_print("You burn a measure of momentum to anchor your ground, fighting off the dragon's attack!")
                player_release(1)
                pause(1.5)
                continue
 
            dragon_special = dragon_choose_special("disadvantage")
            if dragon_special == "headbutt" and headbutt_cd == 0:
                combat_print("The dragon swings its great head in a punishing headbutt, robbing both of you of momentum!")
                dragon_release(1)
                player_release(2)
                headbutt_cd = HEADBUTT_CD_MAX
                pause(1.5)
                player_health_current -= 1   # still take the full hit
                if player_health_current <= 0:
                    return False
                continue
 
            dis_outcome = run_event(player_action, random_attack("disadvantage"))
            if dis_outcome == "failure":
                player_health_current -= 1
                if player_health_current <= 0:
                    return False
 
        # End-of-round checks
        if enemy_health_current <= 0:
            return True
        if player_health_current <= 0:
            return False
 
 
# ============================================================
# Helpers — local to this file
# ============================================================
 
def run_event(player_action, enemy_action):
    """Look up a dragon combat event, print its lines, and return the result."""
    event = REFERENCE.dragon_combat_events.get((player_action, enemy_action))
    if not event:
        event = REFERENCE.dragon_combat_events.get((player_action, enemy_action))
    if not event:
        combat_print("Something caused an unexpected combat error. Try a different action.")
        pause()
        return None
    for line in event["lines"]:
        combat_print(line)
    pause(1.5)
    return event.get("result")
 
def random_attack(mode="static"):
    """Return a random enemy action string for the given combat phase."""
    options = {
        "static":       ["s", "b", "f"],
        "advantage":    ["r", "d"],
        "disadvantage": ["c", "h"],
    }
    return random.choice(options.get(mode, ["s", "b", "f"]))
 
def combat_print(text, delay=0.02):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()
 
def pause(secs=1):
    time.sleep(secs)
 
def line_break():
    print(REFERENCE.LINE_BREAK)
 
def hp_bar(current, maximum):
    filled = "█" * current + "░" * (maximum - current)
    return f"[{filled}] {current}/{maximum}"

def main():
    Dragon_Combat(static=REFERENCE.DRAGON_STATIC, charging=REFERENCE.DRAGON_CHARGING, reeling=REFERENCE.DRAGON_REELING, player_health_max=20, enemy_health_max=22, enemy_name="Dragon, Guardian of the Dungeon")

main()
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

def Dragon_Combat(static="S", charging="C", reeling="R", player_health_max=10, enemy_health_max=20, enemy_name="Invalid Dragon"):
    pass
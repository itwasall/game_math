from random import randint

class Character:
    def __init__(self, health: int, AV: int, DV: int, attack: str, **kwargs):
        self.max_health = health
        self.current_health = self.max_health
        self.AV = AV
        self.DV = DV
        self.attack = attack
        for k, d in kwargs.item():
            self.__setattr_(k, d)

def dice(dice_string):
    throws, sides = dice_string.split("d")
    return sum([randint(1, int(sides)) for _ in range(int(throws))])

def attack(atk: str):
    """
        Should be in format "2d6+3"
        Where the "+3" is the sum of any extra weapon dmg (should there be any) and the strength mod
    """
    if "+" in atk:
        dice_string, flat_damage = atk.split("+")
    else:
        flat_damage = 0
    return dice(dice_string) + int(flat_damage)

def confirm_hit(DV, to_hit, atk_agi_mod):
    crit = False
    dice_roll = dice("1d20")
    if dice_roll == 20:
        crit = True
    accuracy = dice_roll + atk_agi_mod + to_hit
    if DV > accuracy and not crit:
        return False
    return True 


def confirm_penetration():
    return "Dear god no have you seen how the game calculates this shit?"


def total_xp_per_level(lvl: int):
    return (15 * (lvl ** 3)) + 100

def xp_for_level(lvl: int):
    if lvl == 1:
        return 100
    return total_xp_per_level(lvl) - total_xp_per_level(lvl - 1)

def battle_sim():
    pass

a = attack("2d6+3")
print(a)

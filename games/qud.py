def total_xp_per_level(lvl: int):
    return (15 * (lvl ** 3)) + 100

def xp_for_level(lvl: int):
    if lvl == 1:
        return 100
    return total_xp_per_level(lvl) - total_xp_per_level(lvl - 1)



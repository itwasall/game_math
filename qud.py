
def calc_xp_by_level(lvl: int):
    return (15 * (lvl ** 3)) + 100

def calc_total_xp_by_level(lvl: int):
    return sum(calc_xp_by_level(i) for i in range(1, lvl))



for i in range(10, 20):
    print(f"XP for level {i}: {calc_xp_by_level(i)}, Total: {calc_total_xp_by_level(i)}")

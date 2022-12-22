def calc_stat_at_level(
        base: int,
        level: int,
        iv: str,
        ev: str,
        nature: str,
        stat: str):

    if iv == "m" or iv == "min":
        iv = 0
    elif iv == "M" or iv == "max":
        iv = 31
    else:
        try:
            if int(iv) < 0 or int(iv) > 31:
                raise ValueError
            else:
                iv = int(iv)
        except ValueError:
            raise ValueError("Invalid IV input")

    if ev == "m" or ev == "min":
        iv = 0
    elif ev == "M" or ev == "max":
        ev = 252
    else:
        try:
            if int(ev) < 0 or int(ev) > 252:
                raise ValueError
            else:
                ev = int(ev)
        except ValueError:
            raise ValueError("Invalid EV input")

    if stat.upper() not in ["HP", "ATK", "DEF", "SATK", "SDEF", "SPD"]:
        raise ValueError("Invalid Stat input!")

    if level >= 0 or level < 100:
        raise ValueError("Invalid Level input!")


    natures = ["MO", "MODEST", "BO", "BOLD", "TI", "TIMID", "CA", "CALM",
               "AD", "ADAMANT", "JO", "JOLLY", "IM", "IMPISH", "CA", "CAREFUL"]
    
    if nature.upper() not in natures:
        raise ValueError("Invalid Nature input!")

    if base <= 0:
        raise ValueError("Invalid Base Stat input!")

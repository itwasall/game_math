import sys
from games import qud
from cli_ui import reset, info, bold, yellow, red, ask_string

def try_int(input: str):
    try:
        int(input)
        return
    except ValueError:
        raise ValueError("Invalid Input")

def clear_line():
    return sys.stdout.write("\033[F") # Cursor up one line

def qud_option():
    print("==================")
    info(red, " [1]:", reset, "Total Level XP\n", red, "[2]:", reset, "Level XP")
    qud_inp = ask_string("")
    clear_line()
    try_int(qud_inp)
    match qud_inp:
        case "1":
            lvl = ask_string(bold, "Enter Level: ")
            clear_line()
            # lvl = ask_string("")
            out = (qud.total_xp_per_level(int(lvl)))
            info(bold, yellow, f"Total Exp to reach level {lvl}:", reset, out)
        case "2":
            lvl = ask_string(bold, "Enter Level: ")
            clear_line()
            out = (qud.xp_for_level(int(lvl)))
            info(bold, yellow, f"Exp to reach level {lvl}:", reset, out)


if __name__ == "__main__":
    inp = ask_string(bold, yellow, "Select Game:\n", reset, red, "[1]:", reset, "Caves of Qud")
    clear_line()
    try_int(inp)
    match inp:
        case "1": 
            qud_option()

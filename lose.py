import curses


def losing():
    stdscr = curses.initscr()
    stdscr.addstr(0, 0, "     )             (")
    stdscr.addstr(1, 0, "  ( /(             )\ )")
    stdscr.addstr(2, 0, "  )\())       (   (()/(             (")
    stdscr.addstr(3, 0, " ((_)\) (    ))\   /(_))  (   (    )\))")
    stdscr.addstr(4, 0, "__ ((__))\  /((_) (_))    )\  )\  /((_)")
    stdscr.addstr(5, 0, "\ \ / /(_))(_))_) | |    (_)( (_)(_)_(")
    stdscr.addstr(6, 0, " \ V // _ \| || | | |__ / _ \(_-</ -_)")
    stdscr.addstr(7, 0, "  |_| \___/ \_,_| |____|\___//__/\___|")
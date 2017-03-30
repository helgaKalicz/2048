import curses


def winning():
    stdscr = curses.initscr()
    stdscr.addstr(0, 0, "     )")
    stdscr.addstr(1, 0, "   ( /(             (  (")
    stdscr.addstr(2, 0, "  )\())       (    )\))(   ' (")
    stdscr.addstr(3, 0, " ((_)\  (    ))\  ((_)()\ )  )\   (")
    stdscr.addstr(4, 0, "__)((__))\  /((_) _(())\ )_)((_)  )\ )")
    stdscr.addstr(5, 0, "\ \ / /(_))(_))_( \ \(( )/ / (_) _(_/(")
    stdscr.addstr(6, 0, " \ V // _ \| || |  \ \/\/ /  | || ' \))")
    stdscr.addstr(7, 0, "  |_| \___/ \_,_|   \_/\_/   |_||_||_|")
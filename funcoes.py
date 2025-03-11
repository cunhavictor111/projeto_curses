import curses

def init():
    window = curses.initscr()
    assets = {
        'pos': [0, 0],
        'vel': [2, 2]
        }
    return window, assets

def get_event(window, assets):
    event = window.getch()
    window.clear()
    if event == ord('d'):
        assets['pos'][0] += assets['vel'][0]
    if event == ord('a'):
        assets['pos'][0] -= assets['vel'][0]
    if event == ord('w'):
        assets['pos'][1] -= assets['vel'][1]
    if event == ord('s'):
        assets['pos'][1] += assets['vel'][1]

    window.addstr(assets['pos'][1], assets['pos'][0], 'this is a: ' + chr(event))
    return event
    
def draw():
    pass


def game_loop(window, assets):
    while get_event(window, assets) != ord('q'):
        window.refresh()     
    curses.endwin()
from .grid import Grid
from .player import Player
from . import pickups



#player = Player(2, 1)
player = Player(17, 5)
score = 0
inventory = []

g = Grid()
g.set_player(player)
g.make_walls()
g.make_additional_walls(part_x=2, part_y=2)
pickups.randomize(g)


# TODO: flytta denna till en annan fil
def print_status(game_grid):
    """Visa spelvärlden och antal poäng."""
    print("--------------------------------------")
    print(f"You have {score} points.")
    print(game_grid)

def to_do_with_a_move(move_x, move_y):
    global score
    score -= 1 #each step takes 1 point
    maybe_item = g.get(player.pos_x + move_x, player.pos_y + move_y)
    player.move(move_x, move_y)
    if isinstance(maybe_item, pickups.Item):
        to_do_after_found_something(maybe_item)

def to_do_after_found_something(maybe_item):
    # we found something
    global score
    #global inventory
    score += maybe_item.value
    inventory.append(maybe_item)
    print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
    # g.set(player.pos_x, player.pos_y, g.empty)
    g.clear(player.pos_x, player.pos_y)

def print_info_about_found_fruits():
    for fruit in inventory:
        print(f"You have: {fruit.name} with +{fruit.value} points")


command = "a"
# Loopa tills användaren trycker Q eller X.
while not command.casefold() in ["q", "x"]:
    print_status(g)

    command = input("Use WASD to move, Q/X to quit. ")
    command = command.casefold()[:1]
    if command == "d" and player.can_move(1, 0, g):  # move right
        to_do_with_a_move(1,0)
    if command == "a" and player.can_move(-1, 0, g):  # move left
        to_do_with_a_move(-1,0)
    if command == "w" and player.can_move(0, -1, g):  # move up
        to_do_with_a_move(0,-1)
    if command == "s" and player.can_move(0, 1, g):  # move down
        to_do_with_a_move(0,1)
    if command == "i":
        print_info_about_found_fruits()

""""
    if command == "d" and player.can_move(1, 0, g):  # move right
        # TODO: skapa funktioner, så vi inte behöver upprepa så mycket kod för riktningarna "W,A,S"
        maybe_item = g.get(player.pos_x + 1, player.pos_y)
        player.move(1, 0)

        if isinstance(maybe_item, pickups.Item):
            # we found something
            score += maybe_item.value
            print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
            #g.set(player.pos_x, player.pos_y, g.empty)
            g.clear(player.pos_x, player.pos_y)"""


# Hit kommer vi när while-loopen slutar
print("Thank you for playing!")

import random

def opening_text():
    '''
    This function prints the game rules.
    '''
    print(
        """\n
        the player searches for a treasure in a 5x5 map. \n
        The player starts at the top left and has a limited number of moves (10 moves) \n
        to find the treasure. There are obstacles on the map that the player cannot\n
        enter. The goal is to find the treasure before the moves run out.\n"""
    ) 


#GUI setup
def create_map():
    '''
     Creates the 5x5 game board and initializes it with empty cells (".").
'''
    initial_game_state = [] 
    for i in range(5): # creates the initial map
        inner_list = [".", ".", ".", ".", "."] # Rows.
        initial_game_state.append(inner_list) # Columns.
    return initial_game_state 


def place_element(game_map, element):
    '''
    Places an element (e.g. treasure "X" or obstacles "O") randomly on the
map. Placement only occurs on free spaces.
Obstacles are designed to remain hidden until the player encounters one. After that,
they are shown on the map so the player doesn't encounter them again.
    '''
    while True:
        # Generates random locations for the "O"s and the "X".
        shuffle_list = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4]
        random.shuffle(shuffle_list)
        x = shuffle_list[0]
        y = shuffle_list[1]
        if game_map[y][x] == ".":
            game_map[y][x] = element
            return (x, y) # Returns coordinates.


def print_map(game_map):
    '''
    Prints the current map to the console. Each line is displayed on a new
line and fields are separated by spaces.
    '''
    for y in range(5):
        for x in range(5):
            element = game_map[y][x]
            if len(element) == 1: 
                # If element longer than 1, print ".", so the "O" is hidden.
                print(element, end= "    ")
            else: print(".", end= "    ") # Print actual sign.
            
        print("\n")


def move_player(position, direction, game_map, obstacles):
    '''
    Calculates the player's new position based on the direction entered.
The function prevents movement outside the map or into obstacles. In case of invalid
moves, the player remains at his current position.
    '''
    position_difference = None
    # Define new position using summation of old position and position_difference.
    if direction == "r":
        position_difference = (1, 0)
    elif direction == "l":
        position_difference = (-1, 0)
    elif direction == "o":
        position_difference = (0, -1)
    elif direction == "u":
        position_difference = (0, 1)
        
    # New coordinates.
    x_new = position[0] + position_difference[0]
    y_new = position[1] + position_difference[1]
    
    new_position = (x_new, y_new)
    # Out of bounds of the 5x5 grid condition.
    if 0 <= x_new < 5 and 0 <= y_new < 5:
        element = game_map[y_new] [x_new]
        # Player hits the obstacle. Outputs this and does not move.
        if element[0] == "O":
            print("You hit an obstacle HAHA!")
            game_map[y_new][x_new] = "O"
            return position
        else: # Moves.
            game_map[y_new][x_new] = "P"
            game_map[position[1]][position[0]] = "."
            return new_position
    else:
        print("You are trying to go out of bounds.")
        return position


def treasure_hunter_game():
    '''
    Controls the entire game:
    Initialize the playing field and place the treasure and obstacles.
    Processes the player's inputs and moves him accordingly.
    Displays the updated map after each turn.
    End the game when the treasure is found or the moves are used up.
    '''
    # Setup.
    opening_text()
    map = create_map()
    player_position = (0, 0)
    map[0][0] = "P"
    treasure = place_element(map, "X")
    obstacles = []
    # for i in range(x), x = amount of obstacles.
    for i in range(6):
        o_ele = place_element(map, "O ")
        obstacles.append(o_ele)
    # defines the amount of moves.
    moves = 10
    while True:
        print_map(map)
        move_direction = None
        while True: 
            # Explains keybinds.
            player_move = input("""
                            Input r to move right.\n
                            Input l to move left.\n
                            Input o to move up.\n
                            Input u to move down.\n
                            Input q to QUIT\n
                            """)
            # Checks if input is valid.
            if player_move in "rlou":
                move_direction = player_move
                break
            # Enter "q" to quit
            elif player_move == "q":
                return
            else: 
                print("Invalid input! >:[")
        # Decreases amount of moves left.
        moves -= 1
        print("moves left:", moves, "\n")
        player_position = move_player(player_position, move_direction, map, obstacles)
        # Victory condition
        if player_position == treasure:
            print("You won. Nice.")
            break
        # Defeat condition
        if moves == 0:
            print("""No more moves. In Germany we say: Würd' mir stinken,\n 
                  and I think that's beautiful.""")
            break


if __name__ == '__main__':
    map = create_map()
    place_element(map, "X")
    var = []
    for i in range(5):
        var.append(place_element(map, "O"))
    map[0][0] = "P"
    move_player((0, 0), "r", map, var)
    print_map(map)
class GameState:
    def __init__(self, score, level, lives):
        self.score = score
        self.level = level
        self.lives = lives

    def add_to_score(self, amount):
        # The += operator is a simple way to add to the players score
        self.score += amount


    def next_level(self):
        #Similarly to add_to_score, the += operator is used to "move" to the next level by adding 1
        self.level += 1



    def add_or_subtract_lives(self, amount):
        self.lives += amount
        if self.lives < 0:
            self.lives = 0

#   def check_gameover(self):
# This function should, in theory, put up a game over message when lives reach 0, although im having trouble with it displaying.
#        if self.lives == 0:
#            print("Rest in peace, you're dead! Game over!")


def save_game(game_state, file_name):
    #The current game file is opened in write mode using 'w' and the data, those being score, level, and lives, are all recorded.
    with open(file_name, 'w') as file:
        file.write(f"{game_state.score}, {game_state.level},{game_state.lives}")




def load_game(file_name):
    #While the above funtion used 'w' to write data, this one uses 'r' or read in order to pull up data thats been stored.
    #line 42 reads the data available in the saved file, if no files exists then a new game is started.
    try:
        with open(file_name, 'r') as f:
            line = f.readline().strip()
            if not line:
                print("Nothing found. Starting with a fresh save")
                return GameState(0, 1, 3)
            score, level, lives = line.split(',')
            return GameState(int(score), int(level), int(lives))
    except FileNotFoundError:
        print("Save file not found. Starting new game.")
        return GameState(0, 1, 3)
    except:
        print("Error reading save file. Starting new game.")
        return GameState(0, 1, 3)
    return loaded_game









#game = load_game("test")
#game.add_to_score(100)

#save_game(game, "test")

#game.add_or_subtract_lives(-3)

#save_game(game,"test")

game = GameState(0,1,1)
game.add_or_subtract_lives(-1)
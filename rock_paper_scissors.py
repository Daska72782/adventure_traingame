import random


class Player:
    
    score = 0
    computer_score = 0
    
    
    def __init__(self):
        self.my_move = None
        self.their_move = None

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()
        self.characters = "Human" 
        
    def move(self):
        while True:
            move = input ("On three; 1, 2, 3! "
                          "(rock, paper, scissors)").lower()
            if move in moves:
                return move
            else:
                print("Sorry, I didn't get that!")
                
                
class RepeatPlayer(Player):
    def move(self):
        return 'rock' 
    
    
class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)
    
    
class ReflectPlayer(Player):
    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        else:
            return self.their_move


class CyclePlayer(Player):
    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        else:
            position = moves.index(self.my_move) + 1
            if position == len(moves):
                position = 0
            return moves[position] 
        
                      
def beats(p1move, p2move):
    return ((p1move == 'rock' and p2move == 'scissors') or
            (p1move == 'scissors' and p2move == 'paper') or
            (p1move == 'paper' and p2move == 'rock'))                
                  
        
class Game:
    def __init__(self, Player1, Player2):
        self.p1 = Player1
        self.p2 = Player2
        self.score = 0
        self.computer_score = 0
        

    def play_round(self):
        p1move = self.p1.move()
        p2move = self.p2.move()
        print(f"Player1: {p1move}  Player2: {p2move}")
        if beats(p1move, p2move):
            self.score += 1
            print("You Win!")
        elif p1move == p2move:
            print("Tie!")
        else:
            self.computer_score += 1
            print("You Lose!")
        self.p1.learn(p1move, p2move)
        self.p2.learn(p2move, p1move)
        print(f"Player1: {self.score} | "
              f"Player2: {self.computer_score}")   
        
        
    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round +1}:")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    moves = ['rock', 'paper', 'scissors']
    characters = { 
         "human": HumanPlayer(),
         "random": RandomPlayer(),
         "reflect": ReflectPlayer(),
         "cycle": CyclePlayer(),
         "repeat": RepeatPlayer()
    }
    
    
    while True:
        print("Let's pound it!")
        choices = input("Choose your character!"
                        "(Human, Random, Reflect, Cycle, Repeat)").lower()
        if choices in characters:
             game = Game(characters["human"], characters[choices])
             game.play_game()
        else:
            print("Sorry, that's not an option.")
     
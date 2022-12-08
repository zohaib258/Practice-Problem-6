import random

class Player:

    def __init__(self, a, b):
        numb = random.randint(a , b)
        
        self.trail = 0
        while True:
            inp = int(input("Enter Your Guess: "))
            self.trail += 1
            if inp < numb:
                print("Sorry Wrong Guess (Enter a larger number this time)")
            elif inp > numb:
                print("Sorry Wrong Guess (Enter a smaller number this time)")
            else:
                print(f"Congratulations Player guessed the number in {self.trail} trails")
                break
       



if __name__ == '__main__':
    print("Hello And welcome to multiplayer game")
    print("Player 1 Trun!!!!!!:")
    a = int(input("Please Enter the value of a: "))
    b = int(input("Please Enter the value of b: "))
    print(f"The number is generated between {a} and {b}")
    p1 = Player(a,b)
    print("Now Player 2 Trun!!!!!")
    p2 = Player(a,b)
    if p1.trail < p2.trail:
        print("The Winner is Player 1!!!!")
    else:
        print("The Winner is Player 2!!!!!")

    
    c = int(input("Press 0 for exit: "))
    if c==0:
        exit()
    else:
        pass

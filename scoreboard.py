from turtle import Turtle



class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        with open("data.txt") as data:
            self.high_score=int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.hideturtle()
        self.updated_score()

    def updated_score(self):
        self.clear()
        self.write(f"SCORE= {self.score} High Score:{self.high_score}",False,"center",font=("arial",10,"normal"))

    def reset_score(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.high_score}")
        self.score=0
        self.updated_score()




    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", False,"center",font=("arial", 10,"normal"))



    def increase_score(self):
        self.score+=1
        self.updated_score()













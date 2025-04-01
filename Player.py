from Character import Character

class Player(Character):
    def __init__(self, name, score=0, lives=3):
        super().__init__(name)
        self.lives = lives
        self.score = score

    def __str__(self):
        return f"Player(name={self.name}, lives={self.lives}, score={self.score})"
    
    def move(self, direction):
        if direction == "up":
            self.y -= 1
        elif direction == "down":
            self.y += 1
        elif direction == "left":
            self.x -= 1
        elif direction == "right":
            self.x += 1
        else:
            raise ValueError("Invalid direction")
    
    def shoot(self):
        #shot= Shot(self.name, is_enemy_shot=False)
        print(f"{self.name} has shot a bullet!")
        #return shot
        #comentado hasta crear la clase Shot :)


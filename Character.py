from Entity import Entity

class Character(Entity):
    def __init__(self, lives):
        super().__init__()
        self.lives = lives

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
    
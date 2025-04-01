class Entity:
    def __init__(self, x ,u, image):
        self.x = x
        self.y = y
        self.image = image
    
    def __str__(self):
        return f"Entity(x={self.x}, y={self.y}, image={self.image})"
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        #asumiendo que image es un objeto de pygame.Surface

    
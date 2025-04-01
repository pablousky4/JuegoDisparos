from Entity import Entity

class Shot(Entity):
    def __init__(self, x, y, image, speed):
        super().__init__(x, y, image)
        self.speed = speed
        self.is_alive = True
        self.is_a_star = False
        self.is_bomb_exploded = False

    def __str__(self):
        return super().__str__() + f", speed={self.speed}, is_alive={self.is_alive}, is_a_star={self.is_a_star}, is_bomb_exploded={self.is_bomb_exploded})"
    
    def move(self):
        if self.is_alive:
            # Implementar lógica de movimiento del disparo
            # Por ejemplo, mover el disparo hacia abajo
            self.y += self.speed
            if self.y < 0 or self.y > 600:
                self.is_alive = False
        else:
            pass

    def hit_target(self, target):
        if self.is_alive:
            # Implementar lógica para detectar si el disparo ha alcanzado el objetivo
            # Por ejemplo, verificar la colisión entre el disparo y el objetivo
            if self.x == target.x and self.y == target.y:
                self.is_alive = False
                
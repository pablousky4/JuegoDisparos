from Character import Character
from Shot import Shot

class Opponent(Character):
    def __init__(self, is_star=False):
        self.is_star = is_star

    def __str__(self):
        return f"Opponent(is_star={self.is_star})"
    
    def move(self):
        # Implementar lógica de movimiento del oponente
        if self.position.x <= 0 or self.position.x >= self.screen_width - self.width:
            self.velocity.x = -self.velocity.x  # cambia de dirección cuando se choca
        self.position.x += self.velocity.x
    
    def shoot(self):
        if self.is_alive:
            # Creo un disparo (shot) en la posición del oponente
            # y con la misma velocidad que el oponente
            # El disparo se crea con la posición y velocidad del oponente
            # y se ajusta para que se mueva hacia abajo
            shot = Shot(
                position=self.position.copy(),  
                velocity=self.velocity.copy(),  
                owner=self,  
                type="opponent_bullet"  # especifico el tipo de disparo
            )
            shot.velocity.y = abs(shot.velocity.y)  # Aseguro que el disparo se mueve hacia abajo
            return shot
        return None 
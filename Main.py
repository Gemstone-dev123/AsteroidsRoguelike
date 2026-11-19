import math
import arcade
import random
import ShipFunctions
import AsteroidFunctions

Screen = "Upgrades"

class Bullet:
    def __init__(self, X, Y, Angle):
        self.X = X + math.cos(Angle) * 20
        self.Y = Y + math.sin(Angle) * 20
        self.Speed = 10

        self.Angle = Angle

        self.Lasted = 0
        self.LifeSpan = 60

class Ship:
    def __init__(self):
        self.X = 512
        self.Y = 382
        self.MoveSpeed = 0

        self.Angle = 0
        self.TurnSpeed = 0

        self.DirectionRadians = 0

class GameScreen(arcade.View):
    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.BLACK)
        self.MaxPoints = 0
        self.Points = 0
        self.KeysPressed = []
        self.Ship = Ship()
        self.Bullets = []
        self.Asteroids = []

    def on_key_press(self, Key, Modifiers):
        if Key not in self.KeysPressed:
            self.KeysPressed.append(Key)
        if arcade.key.Z in self.KeysPressed:
            self.Bullets.append(Bullet(self.Ship.X, self.Ship.Y, self.Ship.DirectionRadians))

    def on_key_release(self, Key, Modifiers):
        if Key in self.KeysPressed:
            self.KeysPressed.remove(Key)

    def on_update(self, DeltaTime):
        ShipFunctions.Move(self.Ship, self.KeysPressed)
        ShipFunctions.MoveBullets(self.Bullets)

        if len(self.Asteroids) < 10:
            if random.randint(0, 100) < 2:
                self.Asteroids.append(AsteroidFunctions.CreateAsteroid())

        ShipFunctions.GetHit(self, self.Ship, self.Asteroids)

        AsteroidFunctions.Move(self, self.Asteroids, self.Bullets)

    def on_draw(self):
        self.clear()

        ShipFunctions.Draw(self.Ship, self.Bullets)
        AsteroidFunctions.Draw(self.Asteroids)

        arcade.draw_text(f"Points: {self.Points}", 10, 10, arcade.color.WHITE, 20)
        arcade.draw_text(f"Max Points: {self.MaxPoints}", 10, 40, arcade.color.WHITE, 20)

def Main():
    Window = arcade.Window(1024, 764, "Asteroids")
    Window.show_view(GameScreen())
    arcade.run()

if __name__ == "__main__":
    Main()
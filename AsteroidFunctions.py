import math
import arcade
import random

class Asteroid:
    def __init__(self):
        Side = random.randint(1, 4)

        if Side == 1:
            self.X = random.randint(0, 1024)
            self.Y = 0
            self.Angle = math.radians(random.randint(100, 260))
        elif Side == 2:
            self.X = 1024
            self.Y = random.randint(0, 764)
            self.Angle = math.radians(random.randint(-170, -10))
        elif Side == 3:
            self.X = random.randint(0, 1024)
            self.Y = 764
            self.Angle = math.radians(random.randint(-80, 80))
        elif Side == 4:
            self.X = 0
            self.Y = random.randint(0, 764)
            self.Angle = math.radians(random.randint(10, 170))

        self.Size = random.randint(1, 3)

        self.Speed = 4 - self.Size

def CreateAsteroid(Size = 0):
    NewAsteroid = Asteroid()
    if Size > 0:
        NewAsteroid.Size = Size
        NewAsteroid.Speed = 4 - Size
    return NewAsteroid

def Move(Self, Asteroids, Bullets):
    for Asteroid in Asteroids:
        Asteroid.X += math.cos(Asteroid.Angle) * Asteroid.Speed
        Asteroid.Y += math.sin(Asteroid.Angle) * Asteroid.Speed

        if Asteroid.X > 1024:
            Asteroid.X = 0
        elif Asteroid.X < 0:
            Asteroid.X = 1024

        if Asteroid.Y > 764:
            Asteroid.Y = 0
        elif Asteroid.Y < 0:
            Asteroid.Y = 764

        for Bullet in Bullets:
            if math.hypot(Asteroid.X - Bullet.X, Asteroid.Y - Bullet.Y) <= Asteroid.Size * 20:
                Self.Points += 10
                if Self.Points > Self.MaxPoints:
                    Self.MaxPoints = Self.Points

                Bullets.remove(Bullet)
                Asteroids.remove(Asteroid)

                if Asteroid.Size > 1:
                    NewAsteroid1 = CreateAsteroid(Asteroid.Size - 1)
                    NewAsteroid2 = CreateAsteroid(Asteroid.Size - 1)
                    NewAsteroid1.X = Asteroid.X
                    NewAsteroid1.Y = Asteroid.Y
                    NewAsteroid2.X = Asteroid.X
                    NewAsteroid2.Y = Asteroid.Y
                    NewAsteroid1.Angle = Asteroid.Angle + math.radians(random.randint(-135, -45))
                    NewAsteroid2.Angle = Asteroid.Angle + math.radians(random.randint(45, 135))
                    Asteroids.append(NewAsteroid1)
                    Asteroids.append(NewAsteroid2)

def Draw(Asteroids):
    for Asteroid in Asteroids:
        arcade.draw_circle_outline(Asteroid.X, Asteroid.Y, Asteroid.Size * 20, arcade.color.WHITE, 2)
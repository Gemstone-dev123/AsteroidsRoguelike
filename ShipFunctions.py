import math
import arcade

def Move(Ship, KeysPressed):
    if arcade.key.LEFT in KeysPressed:
        Ship.TurnSpeed += 2
    if arcade.key.RIGHT in KeysPressed:
        Ship.TurnSpeed -= 2
    Ship.TurnSpeed *= 0.8

    if arcade.key.UP in KeysPressed:
        Ship.MoveSpeed += 2
    if arcade.key.DOWN in KeysPressed:
        Ship.MoveSpeed -= 2
    Ship.MoveSpeed *= 0.8

    Ship.Angle += Ship.TurnSpeed
    Ship.DirectionRadians = math.radians(Ship.Angle)

    Ship.X += math.cos(Ship.DirectionRadians) * Ship.MoveSpeed
    Ship.Y += math.sin(Ship.DirectionRadians) * Ship.MoveSpeed

    if Ship.X > 1024:
        Ship.X = 0
    elif Ship.X < 0:
        Ship.X = 1024

    if Ship.Y > 764:
        Ship.Y = 0
    elif Ship.Y < 0:
        Ship.Y = 764

def MoveBullets(Bullets):
    for Bullet in Bullets:
        Bullet.Lasted += 1
        if Bullet.Lasted > Bullet.LifeSpan:
            Bullets.remove(Bullet)
            continue

        Bullet.X += math.cos(Bullet.Angle) * Bullet.Speed
        Bullet.Y += math.sin(Bullet.Angle) * Bullet.Speed

        if Bullet.X > 1024:
            Bullet.X = 0
        elif Bullet.X < 0:
            Bullet.X = 1024

        if Bullet.Y > 764:
            Bullet.Y = 0
        elif Bullet.Y < 0:
            Bullet.Y = 764

def GetHit(Self, Ship, Asteroids):
    for Asteroid in Asteroids:
        if math.hypot(Asteroid.X - Ship.X, Asteroid.Y - Ship.Y) <= Asteroid.Size * 30:
            Ship.X = 512
            Ship.Y = 382
            Ship.MoveSpeed = 0

            Ship.Angle = 0
            Ship.TurnSpeed = 0

            Ship.DirectionRadians = 0

            Self.Points = 0

            while len(Asteroids) > 0:
                Asteroids.pop()
            break

def Draw(Ship, Bullets):
    Front = [
        Ship.X + math.cos(Ship.DirectionRadians) * 20,
        Ship.Y + math.sin(Ship.DirectionRadians) * 20
    ]
    Right = [
        Ship.X + math.cos(Ship.DirectionRadians + math.pi / 1.5) * 20,
        Ship.Y + math.sin(Ship.DirectionRadians + math.pi / 1.5) * 20
    ]
    Back = [
        Ship.X,
        Ship.Y
    ]
    Left = [
        Ship.X + math.cos(Ship.DirectionRadians - math.pi / 1.5) * 20,
        Ship.Y + math.sin(Ship.DirectionRadians - math.pi / 1.5) * 20
    ]

    arcade.draw_line(
        Front[0],
        Front[1],
        Right[0],
        Right[1],
        arcade.color.WHITE, 2
    )
    arcade.draw_line(
        Right[0],
        Right[1],
        Back[0],
        Back[1],
        arcade.color.WHITE, 2
    )
    arcade.draw_line(
        Back[0],
        Back[1],
        Left[0],
        Left[1],
        arcade.color.WHITE, 2
    )
    arcade.draw_line(
        Left[0],
        Left[1],
        Front[0],
        Front[1],
        arcade.color.WHITE, 2
    )

    for Bullet in Bullets:
        arcade.draw_line(Bullet.X, Bullet.Y, Bullet.X - math.cos(Bullet.Angle) * 10, Bullet.Y - math.sin(Bullet.Angle) * 10, arcade.color.WHITE, 2)
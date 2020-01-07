from enum import Enum

class Direction(Enum):
    NORTH = 1
    EAST  = 2
    SOUTH = 3
    WEST  = 4

class Robot:
    _name      = ""
    _px        = 0
    _py        = 0
    _direction = Direction.NORTH

    def __init__(this, name, xInit = 0, yInit = 0, dirInit = Direction.NORTH):
        assert isinstance(dirInit, Direction)
        this._name      = name
        this._px        = xInit
        this._py        = yInit
        this._direction = dirInit

    def goFwd(this):
        if this._direction == Direction.NORTH:
            this._py += 1
        elif this._direction == Direction.SOUTH:
            this._py -= 1
        elif this._direction == Direction.WEST:
            this._px -= 1
        elif this._direction == Direction.EAST:
            this._px += 1
        else:
            raise ValueError("Bad direction !")

    def goBack(this):
        this.turnAround()
        this.goFwd()
        this.turnAround()

    def turnLeft(this):
        if this._direction == Direction.NORTH:
            this._direction = Direction.WEST
        elif this._direction == Direction.SOUTH:
            this._direction = Direction.EAST
        elif this._direction == Direction.WEST:
            this._direction = Direction.SOUTH
        elif this._direction == Direction.EAST:
            this._direction = Direction.NORTH
        else:
            raise ValueError("Bad direction !")

    def turnRight(this):
        if this._direction == Direction.NORTH:
            this._direction = Direction.EAST
        elif this._direction == Direction.SOUTH:
            this._direction = Direction.WEST
        elif this._direction == Direction.WEST:
            this._direction = Direction.NORTH
        elif this._direction == Direction.EAST:
            this._direction = Direction.SOUTH
        else:
            raise ValueError("Bad direction !")

    def turnAround(this):
        this.turnRight()
        this.turnRight()

    def printPosition(this):
        print("Position du robot " + this._name + " : X = " + str(this._px) + ", Y = " + str(this._py) + " Direction value = " + str(this._direction))

# DEBUT du programme

r1 = Robot("R1", 2, 3, Direction.EAST)
r2 = Robot("R2")

r1.printPosition()
r2.printPosition()

r1.turnRight()
r2.turnLeft()
r1.goBack()
r2.goFwd()
r1.printPosition()
r2.printPosition()


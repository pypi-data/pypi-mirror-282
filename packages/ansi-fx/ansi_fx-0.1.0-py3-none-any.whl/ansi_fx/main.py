from enum import Enum
import sys


class Style(Enum):
    BOLD = 1
    DIM = 2
    ITALIC = 3
    UNDERLINE = 4
    BLINK = 5


class Intensity(Enum):
    NORMAL = 30
    BRIGHT = 90


class Color(Enum):
    BLACK = 0
    RED = 1
    GREEN = 2
    YELLOW = 3
    BLUE = 4
    MAGENTA = 5
    CYAN = 6
    WHITE = 7


class Direction(Enum):
    UP = "A"
    DOWN = "B"
    FORWARD = "C"
    BACKWARD = "D"


class Fx:

    @staticmethod
    def escape(*argv: int):
        codes = [str(i) for i in argv]
        codes = ";".join(codes)
        sys.stdout.write(f"\033[{codes}m")

    @staticmethod
    def reset(self):
        self.escape(0)

    @staticmethod
    def foreground(color: Color, intensity: Intensity = Intensity.NORMAL):
        code = color.value + intensity.value
        Fx.escape(code)

    @staticmethod
    def background(color: Color, intensity: Intensity = Intensity.NORMAL):
        code = color.value + intensity.value + 10
        Fx.escape(code)

    @staticmethod
    def set(*argv: Style):
        codes = [s.value for s in argv]
        if len(codes):
            Fx.escape(*codes)

    @staticmethod
    def echo(message: str, *argv: Style):
        Fx.set(*argv)
        sys.stdout.write(message)
        Fx.reset()


class Erase:

    @staticmethod
    def line(goToBeginnig: bool = True):
        sys.stdout.write("\033[2K")
        if goToBeginnig:
            Move.towards(Direction.BACKWARD)
    
    @staticmethod
    def lines(count: int, goToBeginnig: bool = True):
        for n in range(count):
            Erase.line(goToBeginnig)
            if n + 1 < count:
                Move.towards(Direction.Up, 1)

    @staticmethod
    def screen():
        sys.stdout.write("\033[2J")

    @staticmethod
    def toEnd(goToBeginnig: bool = True):
        sys.stdout.write("\033[K")
        if goToBeginnig:
            Move.towards(Direction.BACKWARD)


class Move:

    @staticmethod
    def towards(direction: Direction, count: int = 1000):
        sys.stdout.write(f"\033[{count}{direction.value}")

    @staticmethod
    def moveAt(line: int, column: int):
        sys.stdout.write(f"\033[{line};{column}H")

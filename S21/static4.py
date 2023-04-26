class Car:

    sound = "ta ta ta"

    def __init__(self) -> None:
        self.__engine_started = False

    def start_engine(self):
        self.__engine_started = True

    def __stop_engine(self):
        self.__engine_started = False

    @staticmethod
    def horn():
        print(Car.sound)

# Client code
vw = Car()
vw.horn()
# Car.horn()
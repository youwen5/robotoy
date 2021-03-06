from gpiozero import DistanceSensor
from . import pins
from ..singleton import singleton


@singleton
class UltraSonic(DistanceSensor):
    def __init__(self, *args, **kwargs):
        super().__init__(echo=pins.ULTRASONIC_ECHO,
                         trigger=pins.ULTRASONIC_TRIGGER, *args, *kwargs)

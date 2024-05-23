import numpy as np

from Models.Round import Round
from time import sleep

while True:
    round = Round()
    round.start()
    sleep(10)
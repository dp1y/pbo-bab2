from game.image import open, close, change
from game.sound import load as sound_load, play, pause
from game.level import over, load as level_load, start

print(open.functionOpenImage())
print(close.functionCloseImage())
print(change.functionChangeImage())

print(sound_load.functionLoadSound())
print(play.functionPlaySound())
print(pause.functionPauseSound())

print(over.functionOverLevel())
print(level_load.functionLoadLevel())
print(start.functionStartLevel())
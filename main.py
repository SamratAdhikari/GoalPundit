import matplotlib.pyplot as plt
from mplsoccer import Pitch, VerticalPitch

pitch = Pitch()

fig, ax = pitch.draw(figsize=(10, 5))
plt.show()
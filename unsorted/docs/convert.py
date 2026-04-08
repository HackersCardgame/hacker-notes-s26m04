from lottie import Animation
from PIL import Image

# Lade die .tgs-Datei
anim = Animation.load("AnimatedSticker.tgs")

# Speichere als GIF (einfache Lösung, erfordert ggf. Anpassungen)
anim.write_gif("output.gif", fps=30)




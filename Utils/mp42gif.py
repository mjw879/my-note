# require moviepy
from moviepy.editor import *
import os
for file in os.listdir("./Temp/Input"):
    if file.endswith(".mp4"):
        clip=(VideoFileClip(file)).resize((0.8))
        clip.write_gif(f"./Temp/Output/{file[:-4]}.gif",program="imageio",opt="nq",fps=5)
    
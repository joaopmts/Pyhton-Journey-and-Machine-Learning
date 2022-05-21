import pandas as pd
import numpy as np
import os

local = f"{os.path.dirname(os.path.dirname(__file__))}\\arquivos"

frame = pd.read_csv(f"{local}\\Android_Permission.csv", usecols=["App", "Category", "Default : Access all system downloads (S)", "Your messages : edit SMS or MMS (D)", "Default : delete other applications' data (S)", "Package"]).drop_duplicates("Package").set_index('Package')

print("-----------------------")

print(frame[frame["Default : Access all system downloads (S)"] == 1])

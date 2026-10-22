from matplotlib import pyplot as plt
import numpy as np
import csv
import pandas as pd

with open('gpu_run.csv', mode='r', encoding='utf-8') as file:
    df = pd.read_csv(file)

    ax = df.plot(x="batch", y="time", subplots = True, label="gpu_run", color="green")


with open('cpu_run.csv', mode='r', encoding='utf-8') as file:
    df = pd.read_csv(file)

    df.plot(ax=ax,x="batch", y="time", subplots = True, label="cpu_run", color="red", ylabel="Time (s)", xlabel="Batch (#)")


plt.ylim(bottom=0)
plt.savefig('gpucpuplot.png')
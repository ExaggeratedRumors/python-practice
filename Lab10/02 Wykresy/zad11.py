# Mamy dane zachorowań na COVID w Polsce
# https://www.gov.pl/attachment/7152d6ee-4519-4f02-98e4-38376c3705eb
# Narysować wykres z legendą z pełną nazwą województwa
# i procentową ilością przypadków w stosunku do całego kraju
# i procentową ilością zgonów w stosunku do zgonów w całym kraju

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = np.array(pd.read_csv('https://www.gov.pl/attachment/7152d6ee-4519-4f02-98e4-38376c3705eb'
                            , encoding='windows-1250', skipinitialspace=True, sep=';'))

labels = [i for i, _ in enumerate(data[1:, 0])]
cases = data[1:, 1]/data[0][1]
deaths = data[1:, 3]/data[0][3]


fig = plt.figure(figsize=(18,11), dpi=80)
gs = fig.add_gridspec(2, hspace=0.5)
axs = gs.subplots(sharex=False, sharey=False)
axs[0].bar(labels, cases, color='teal')
axs[1].bar(labels, deaths, color='indigo')

for ax in axs.flat:
    ax.set_xticks(labels, data[1:, 0], fontsize=10, rotation=45)
axs.flat[0].set(ylabel = "Liczba przypadków w stosunku do kraju")
axs.flat[1].set(ylabel = "Liczba zgonów w stosunku do kraju")
plt.show()


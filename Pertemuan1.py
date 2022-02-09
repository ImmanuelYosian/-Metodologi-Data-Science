# import numpy as np

# tinggi = (177, 175, 189)
# berat = (77, 56, 43)


# np_tinggi = np.array(tinggi)
# np_berat = np.array(berat)

# print (np_tinggi)
# print (np_berat)

# beratideal = np_tinggi/np_berat ** 10
# print(beratideal)

# import pandas as pd
# Data = pd.read_csv("Tab.csv")
# print(Data.Negara)

import matplotlib as plt

tahun = [1999, 1998, 1997, 2000]
penduduk = [189, 178, 156, 134]

plt.plot(tahun, penduduk)
plt.show()
import numpy as np

yday = np.datetime64('today','D') - np.timedelta64(1,'D')
print("Ieri:",yday)

today = np.datetime64('today','D')
print("Azi:",today)

maine = np.datetime64('today','D') + np.timedelta64(1,'D')
print("Maine:",maine)

sapt = np.datetime64('today','D') + np.timedelta64(7,'D')
print("Peste o saptamana:",sapt)
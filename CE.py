import pandas as pd
import numpy as np

# data preparation
df = pd.read_csv('trainingDataCandElim.csv')
df = df.drop_duplicates()
train = df.iloc[0:, 0:]
train = np.array(train)

S = ("0", "0", "0", "0", "0", "0")
G = (("?", "?", "?", "?", "?", "?"), ("?", "?", "?", "?", "?", "?"), ("?", "?", "?", "?", "?", "?"),
     ("?", "?", "?", "?", "?", "?"), ("?", "?", "?", "?", "?", "?"), ("?", "?", "?", "?", "?", "?"))
g_history = [G]
s_history = [S]
g_counter = 0
s_counter = 1

A = df.iloc[0:, 0:1]
B = df.iloc[0:, 1:2]
C = df.iloc[0:, 2:3]
D = df.iloc[0:, 3:4]
E = df.iloc[0:, 4:5]
F = df.iloc[0:, 5:6]
G = df.iloc[0:, 6:7]

A = np.array(A)
B = np.array(B)
C = np.array(C)
D = np.array(D)
E = np.array(E)
F = np.array(F)
G = np.array(G)

# S initialization
for y in train:
    if y[6] == "Enjoy Sport":
        S = y
        break
S = np.delete(S, 6)
s_history.append(S)

Sky = True
Air_temp = True
Humidity = True
Wind = True
Water = True
Forecast = True

aa = 0
aaa = 0
aaaa = 0
bb = 0
bbb = 0
cc = 0
ccc = 0
dd = 0
ddd = 0
ee = 0
eee = 0
ff = 0
fff = 0

sky = ["Sunny", "Rainy", "Cloudy"]
air_temp = ["Cold", "Warm"]
humidity = ["High", "Normal"]
wind = ["Weak", "Strong"]
water = ["Cool", "Warm"]
forecast = ["change", "same"]

# /// A

for i in range(len(A)):
    if A[i] == "Sunny" and G[i] == "Enjoy Sport":
        aa = 1
for i in range(len(A)):
    if A[i] == "Sunny" and G[i] == "Do Not Enjoy":
        aa = 2
if aa == 2:
    sky.remove("Sunny")

for i in range(len(A)):
    if A[i] == "Rainy" and G[i] == "Enjoy Sport":
        aaa = 1
for i in range(len(A)):
    if A[i] == "Rainy" and G[i] == "Do Not Enjoy":
        aaa = 2

if aaa == 2:
    sky.remove("Rainy")

for i in range(len(A)):
    if A[i] == "Cloudy" and G[i] == "Enjoy Sport":
        aaaa = 1
for i in range(len(A)):
    if A[i] == "Cloudy" and G[i] == "Do Not Enjoy":
        aaaa = 2

if aaaa == 2:
    sky.remove("Cloudy")

if len(sky) != 1:
    Sky = False

# /// B

for i in range(len(B)):
    if B[i] == "Cold" and G[i] == "Enjoy Sport":
        bb = 1
for i in range(len(B)):
    if B[i] == "Cold" and G[i] == "Do Not Enjoy":
        bb = 2

if bb == 2:
    air_temp.remove("Cold")

for i in range(len(B)):
    if B[i] == "Warm" and G[i] == "Enjoy Sport":
        bbb = 1
for i in range(len(B)):
    if B[i] == "Warm" and G[i] == "Do Not Enjoy":
        bbb = 2

if bbb == 2:
    air_temp.remove("Warm")

if len(air_temp) != 1:
    Air_temp = False

# /// C

for i in range(len(C)):
    if C[i] == "High" and G[i] == "Enjoy Sport":
        cc = 1
for i in range(len(C)):
    if C[i] == "High" and G[i] == "Do Not Enjoy":
        cc = 2

if cc == 2:
    humidity.remove("High")

for i in range(len(C)):
    if C[i] == "Normal" and G[i] == "Enjoy Sport":
        ccc = 1
for i in range(len(C)):
    if C[i] == "Normal" and G[i] == "Do Not Enjoy":
        ccc = 2

if ccc == 2:
    humidity.remove("Normal")

if len(humidity) != 1:
    Humidity = False

# /// D

for i in range(len(D)):
    if D[i] == "Weak" and G[i] == "Enjoy Sport":
        dd = 1
for i in range(len(D)):
    if D[i] == "Weak" and G[i] == "Do Not Enjoy":
        dd = 2

if dd == 2:
    wind.remove("Weak")

for i in range(len(D)):
    if D[i] == "Strong" and G[i] == "Enjoy Sport":
        ddd = 1
for i in range(len(D)):
    if D[i] == "Strong" and G[i] == "Do Not Enjoy":
        ddd = 2

if ddd == 2:
    wind.remove("Strong")

if len(wind) != 1:
    Wind = False

# /// E

for i in range(len(E)):
    if E[i] == "Cool" and G[i] == "Enjoy Sport":
        ee = 1
for i in range(len(E)):
    if E[i] == "Cool" and G[i] == "Do Not Enjoy":
        ee = 2

if ee == 2:
    water.remove("Cool")

for i in range(len(E)):
    if E[i] == "Warm" and G[i] == "Enjoy Sport":
        eee = 1
for i in range(len(E)):
    if E[i] == "Warm" and G[i] == "Do Not Enjoy":
        eee = 2

if eee == 2:
    water.remove("Warm")

if len(water) != 1:
    Water = False

# /// F

for i in range(len(F)):
    if F[i] == "change" and G[i] == "Enjoy Sport":
        ff = 1
for i in range(len(F)):
    if F[i] == "change" and G[i] == "Do Not Enjoy":
        ff = 2

if ff == 2:
    forecast.remove("change")

for i in range(len(F)):
    if F[i] == "same" and G[i] == "Enjoy Sport":
        fff = 1
for i in range(len(F)):
    if F[i] == "same" and G[i] == "Do Not Enjoy":
        fff = 2

if fff == 2:
    forecast.remove("same")

if len(forecast) != 1:
    Forecast = False

if Sky:
    g1 = sky
else:
    g1 = "?"

if Air_temp:
    g2 = air_temp
else:
    g2 = "?"

if Humidity:
    g3 = humidity
else:
    g3 = "?"

if Wind:
    g4 = wind
else:
    g4 = "?"

if Water:
    g5 = water
else:
    g5 = "?"

if Forecast:
    g6 = forecast
else:
    g6 = "?"

print("(%s, %s, %s, %s, %s, %s)" % (g1, g2, g3, g4, g5, g6))
for y in train:

    if y[6] == "Enjoy Sport":
        # S
        new_s = s_history[s_counter]
        new_s = list(new_s)
        for i in range(6):
            if new_s[i] != y[i]:
                new_s[i] = "?"
        s_counter += 1
        new_s = tuple(new_s)
        s_history.append(new_s)
print(s_history[-1])
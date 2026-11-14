import numpy as np

femur = int(input("masukan 2 angka terakhir NIU mu :  "))
tibia = int(input("masukan 2 angka terakhir NIF mu :  "))

sudut1 = float(input("masukan sudut 1 :  "))
sudut2 = float(input("masukan sudut 2 :  "))

theta1 = np.radians(sudut1)
theta2 = np.radians(sudut2)

X1 = femur * np.cos(theta1)
Y1 = femur * np.sin(theta1)
X2 = tibia * np.cos(theta1 + theta2)
Y2 = tibia * np.sin(theta1 + theta2)

Xtotal = X1 + X2
Ytotal = Y1 + Y2

print("Titik akhir X : ", Xtotal)
print("Titik akhir Y : ", Ytotal)
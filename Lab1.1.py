ameb = 1

print("Годин", " ", "Амеб")

for i in range(2, 49, 2):
    ameb *= 3
    if i > 1 and i < 10:
        if i in (12,24,36,48):
         print(i, " " * 5, ameb)
    else:
        if i in (12,24,36,48):
         print(i, " " * 4, ameb)
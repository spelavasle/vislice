# Napiši program, ki izpiše prvih 200 praštevil

def je-prastevilo(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for x in range(2, 201):
    if je_prastevilo(x):
        print(x)
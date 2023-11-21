n = int(input("Tapez la valeur de n "))
print("La table de multiplication de : ", n," est :")
if n>0:
    for i in range(1,11):
        print(f"{i} x {n} = {i*n}")
else: 
    print("rentrer un entier supérieur à 0") 
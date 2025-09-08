def somma(a, b):
    return a + b

def sottrazione(a, b):
    return a - b

def moltiplica(a, b):
    return a * b

def dividi(a, b):
    return a / b

print("=== Calcolatrice ===")
print("Operazioni: +  -  *  /")

operazione = input("Scegli operazione (+,-,*,/): ")

a = float(input("Inserisci il primo numero: "))
b = float(input("Inserisci il secondo numero: "))

if operazione == "+":
    print("Risultato:", somma(a, b))
elif operazione == "-":
    print("Risultato:", sottrazione(a, b))
elif operazione == "*":
    print("Risultato:", moltiplica(a, b))
elif operazione == "/":
    print("Risultato:", dividi(a, b))

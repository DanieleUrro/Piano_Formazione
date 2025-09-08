def addizione(a, b):
    return a + b

def sottrazione(a, b):
    return a - b

def moltiplicazione(a, b):
    return a * b

def divisione(a, b):
    return a / b

print("=== Calcolatrice ===")
print("Operazioni: +  -  *  /")

operazione = input("Scegli operazione (+,-,*,/): ")

a = float(input("Inserisci il primo numero: "))
b = float(input("Inserisci il secondo numero: "))

if operazione == "+":
    print("Risultato:", addizione(a, b))
elif operazione == "-":
    print("Risultato:", sottrazione(a, b))
elif operazione == "*":
    print("Risultato:", moltiplicazione(a, b))
elif operazione == "/":
    print("Risultato:", divisione(a, b))

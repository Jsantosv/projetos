numero_str = input("vou dobrar o numero que voce me der: ")
try :
    numero_float = float(numero_str)
    print("O dobro de", numero_float, "e", 2 * numero_float)
    print ('float:', numero_float)

except:
    print("Isso nao e um numero valido.")
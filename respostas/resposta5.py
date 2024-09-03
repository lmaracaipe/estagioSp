def inverter_string(s):
    resultado = ''
    for char in s:
        resultado = char + resultado
    return resultado

string = input("Informe uma string: ")
string_invertida = inverter_string(string)
print(f"String invertida: {string_invertida}")

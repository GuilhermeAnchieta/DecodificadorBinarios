binarios = []
resultados = []
binum = 0

print('\n\033[1;94mDigite uma sequência binaria com 7 ou 6 digitos para serem convertidos em letras.\n'
      '\033[34m"\033[0;32m100000\033[m\033[34m" para "espaço".\n'
      '"\033[32mparar\033[34m" para encerrrar o programa.'
      '\n"\033[32m1111111\033[34m" para excluir ultimo binario digitado.\033[m\n')
while True:
    bina = str(input('→ ')).strip().lower()
    entrada = ""

    if bina == "parar":
        break

    if bina == "1111111" and len(binarios) > 0:
        binarios.pop()
    else:

        if bina.isnumeric():
            binum = int(bina)

        if bina.isnumeric() == False or len(bina) < 6 or len(bina) > 7:
            print('\033[0;31mERRO! Digite uma seguencia de 7 ou 6 números binários.\033[m')

        elif binum < 100000 or binum > 1111111:
            print('\033[31mErro! essa sequência não representa um caractere.\033[m')

        elif bina.isnumeric():
            entrada = bina
            try:
                retorno = int(entrada, 2)
                binarios.append(bina)
            except ValueError:
                print('\033[0;31mERRO! Há um algarismo não binário.\033[m')

for n, bi in enumerate(binarios):
    totresult = 0
    if len(bi) == 7:
        for c, num in enumerate(binarios[n]):
            if c == 6 and num == "1":
                totresult += 1
            elif c == 5 and num == "1":
                totresult += 2
            elif c == 4 and num == "1":
                totresult += 4
            elif c == 3 and num == "1":
                totresult += 8
            elif c == 2 and num == "1":
                totresult += 16
            elif c == 1 and num == "1":
                totresult += 32
            elif c == 0 and num == "1":
                totresult += 64
        resultados.append(totresult)
    else:
        for c, num in enumerate(binarios[n]):
            if c == 5 and num == "1":
                totresult += 1
            elif c == 4 and num == "1":
                totresult += 2
            elif c == 3 and num == "1":
                totresult += 4
            elif c == 2 and num == "1":
                totresult += 8
            elif c == 1 and num == "1":
                totresult += 16
            elif c == 0 and num == "1":
                totresult += 32
        resultados.append(totresult)

conversor = {32: ' ', 33: '!', 34: '"', 35: '#', 36: '$', 37: '%', 38: '&', 39: "'", 40: '(', 41: ')', 42: '*', 43: '+',
             44: ',', 45: '-', 46: '.', 47: '/', 58: ':', 59: ';', 60: '<', 61: '=', 62: '>', 63: '?', 64: '@', 91: '[',
             92: '\ ', 93: ']', 94: '^', 95: '_', 96: '`', 123: '{', 124: '|', 125: '}', 126: '~',
             # NÚMEROS
             48: '0', 49: '1', 50: '2', 51: '3', 52: '4', 53: '5', 54: '6', 55: '7', 56: '8', 57: '9',
             # LETRAS
             65: 'A', 66: 'B', 67: 'C', 68: 'D', 69: 'E', 70: 'F', 71: 'G',
             72: 'H', 73: 'I', 74: 'J', 75: 'K', 76: 'L', 77: 'M', 78: 'N',
             79: 'O', 80: 'P', 81: 'Q', 82: 'R', 83: 'S', 84: 'T', 85: 'U',
             86: 'V', 87: 'W', 88: 'X', 89: 'Y', 90: 'Z',

             97: 'a', 98: 'b', 99: 'c', 100: 'd', 101: 'e', 102: 'f', 103: 'g', 104: 'h',
             105: 'i', 106: 'j', 107: 'k', 108: 'l', 109: 'm', 110: 'n', 111: 'o', 112: 'p',
             113: 'q', 114: 'r', 115: 's', 116: 't', 117: 'u', 118: 'v', 119: 'w', 120: 'x',
             121: 'y', 122: 'z'}

print("\n\033[0;34mA palavra digitada foi: ", end='')
for dec in resultados:
    print(conversor[dec], end='')

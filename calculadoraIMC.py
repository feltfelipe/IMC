''' Índice de Massa Corporal (IMC) e seu status, de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida'''

altura = float(input('Informe sua altura em m. Por exemplo: 1.75m. Informe: '))
peso = float(input('Informe seu peso: '))
imc = peso / (altura ** 2)
if imc > 18.5 and imc <= 25: #poderíamos escrever poupando o 'imc'. assim: 18.5 <= imc < 25: (Lê-se 'se o imc for maior ou igual 18.5 e menor que 25, então:
    print('Seu IMC é {:.1f} e você está no PESO IDEAL'.format(imc))
elif imc > 25 and imc <= 30:
    print('Seu IMC é {:.1f} e você está com SOBREPESO'.format(imc))
elif imc > 30 and imc <= 40:
    print('Seu IMC é {:.1f} e você está OBESO(a)'.format(imc))
elif imc > 40:
    print('Seu IMC é {:.1f} e você se está com Obesidade Mórbida'.format(imc))
else:
    print('Seu IMC é {:.1f} e você está ABAIXO DO PESO'.format(imc))

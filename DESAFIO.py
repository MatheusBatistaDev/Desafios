CONSTANTE_BONUS = 1000

# 1) SOLICITAR AO USUÁRIO QUE DIGITE SEU NOME
nome_usuario = input("Digite o seu nome: ")

# 2) SOLICITAR AO USUÁRIO QUE DIGITE O SEU SALÁRIO
salario_usuario = float(input("Digite o seu salário: "))

# 3) SOLICITAR AO USUÁRIO QUE DIGITE O VALOR DO SEU BÔNUS RECEBIDO
bonus_usuario = float(input("Digite o seu bônus: "))

# 4) CALCULE O VALOR DO BÔNUS FINAL

VALOR_DO_BONUS = CONSTANTE_BONUS + salario_usuario * bonus_usuario

# 6) IMPRIMA A MENSAGEM PERSONALIZADA COM O NOME DO USUÁRIO E O VALOR DO BONUS 

print(f"O usuário {nome_usuario} possui um bônus de R$ {VALOR_DO_BONUS}")

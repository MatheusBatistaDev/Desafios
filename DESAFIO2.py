CONSTANTE_BONUS = 1000

# 1) SOLICITAR AO USUÁRIO QUE DIGITE SEU NOME
nome_usuario = input("Digite o seu nome: ")

# nome_usuario = 30 isso é um erro?

if nome_usuario.isdigit():
    print("Você digitou um número, por favor digite um nome válido.")
    exit()

elif len(nome_usuario) == 0:
    print("Você não digitou nada, por favor digite um nome válido.")
    exit() 

elif nome_usuario.isspace():
    print("Você digitou apenas espaços, por favor digite um nome válido.")
    exit()
    
        


# 2) SOLICITAR AO USUÁRIO QUE DIGITE O SEU SALÁRIO
salario_usuario = float(input("Digite o seu salário: "))

if salario_usuario <= 0:
    print("Você digitou um salário inválido, por favor digite um valor maior que zero.")
    exit() 



# 3) SOLICITAR AO USUÁRIO QUE DIGITE O VALOR DO SEU BÔNUS RECEBIDO
bonus_usuario = float(input("Digite o seu bônus: "))

if bonus_usuario < 0:
    print("Você digitou um bônus inválido, por favor digite um valor maior ou igual a zero.")
    exit()
    

# 4) CALCULE O VALOR DO BÔNUS FINAL

VALOR_DO_BONUS = CONSTANTE_BONUS + salario_usuario * bonus_usuario

# 6) IMPRIMA A MENSAGEM PERSONALIZADA COM O NOME DO USUÁRIO E O VALOR DO BONUS 

print(f"O usuário {nome_usuario} possui um bônus de R$ {VALOR_DO_BONUS}")
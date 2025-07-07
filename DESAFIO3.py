from cmath import e


CONSTANTE_BONUS = 1000

# 1) SOLICITAR AO USUÁRIO QUE DIGITE SEU NOME

nome_valido = False
salario_valido = False
bonus_valido = False   





while nome_valido is not True:
       

    try:
        nome_usuario = input("Digite o seu nome: ")

    # nome_usuario = 30 isso é um erro?

        if len(nome_usuario) == 0:
            raise ValueError("Você não digitou nada, por favor digite um nome válido.")
        
        elif any(char.isdigit() for char in nome_usuario):        
            raise ValueError("Você digitou um número, por favor digite um nome válido.")

        elif nome_usuario.isspace():
            print("Você digitou apenas espaços, por favor digite um nome válido.")
            
        else:
            nome_valido = True
            print("Nome válido:", nome_usuario)

    except ValueError as e:
        print(e)
        continue




    
        


# 2) SOLICITAR AO USUÁRIO QUE DIGITE O SEU SALÁRIO

while salario_valido is not True:
    try:
        salario_usuario = float(input("Digite o seu salário: "))
        if salario_usuario < 0:
            print("Você digitou um salário inválido, por favor digite um valor maior que zero.")
        salario_valido = True
    except ValueError:
        print("Você digitou um valor inválido, por favor digite um número válido.")
    continue
    

# 3) SOLICITAR AO USUÁRIO QUE DIGITE O VALOR DO SEU BÔNUS RECEBIDO

while bonus_valido is not True:
    try:
        bonus_usuario = float(input("Digite o seu bônus: "))
        if bonus_usuario < 0:
            raise ValueError("Você digitou um bônus inválido, por favor digite um valor maior ou igual a zero.")
        bonus_valido = True
    except ValueError as e:
        print(e)
        bonus_usuario = float(input("Digite o seu bônus: "))
        continue
if bonus_usuario < 0:
    print("Você digitou um bônus inválido, por favor digite um valor maior ou igual a zero.")
    



# 4) CALCULE O VALOR DO BÔNUS FINAL

VALOR_DO_BONUS = CONSTANTE_BONUS + salario_usuario * bonus_usuario

# 6) IMPRIMA A MENSAGEM PERSONALIZADA COM O NOME DO USUÁRIO E O VALOR DO BONUS 

print(f"O usuário {nome_usuario} possui um bônus de R$ {VALOR_DO_BONUS}")
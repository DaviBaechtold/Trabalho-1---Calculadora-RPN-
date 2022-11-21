#Davi Baechtold Campos
#Trabalho 1 - Calculadora RPN 

"""
Você deverá desenvolver um programa, na sua linguagem de programação favorita, que leia uma string de entrada e execute a operação matemática contida nesta string. Esta string irá representar operações matemáticas segundo uma variação da RPN, que inclui obrigatoriamente parênteses para limitar as operações, conforme exemplos a seguir: 

a) (2 3 +) = 5 
b) (3 4 *) = 12 
c) (4 2 2 /) = 1 
d) ((4 2 +) 3 *) = 18  

O seu programa deverá ser capaz de realizar as seguintes operações:  
• Adição representada por +; 
• Subtração representada por -; 
• Multiplicação representada por *; 
• Divisão representada por /; 

As operações devem ser realizadas com número reais, mesmo que todos os exemplos aqui utilizados sejam com números inteiros. As operações podem ser aninhadas, sem qualquer limite, 
como pode ser visto nos exemplos a seguir:  
• ((3 4 +) (4 2 /) *) = 14 
• ((3 4 +) (4 (1 1 +) /) *) = 14 
"""



import re,time


entrada = input("Digite a operação matematica: ")
entradaSplit = re.findall('[\d]*[.][\d]+|[\d]+|\+|\-|\*|\/|\^',entrada)      

start_time = time.time() 
print(entradaSplit)
counter=0

while (len(entradaSplit) > 1): 
    if entradaSplit[counter] == '*':  
        entradaSplit[counter-1] = float(entradaSplit[counter-2]) * float(entradaSplit[counter-1]) 
        entradaSplit.pop(counter)                                                                  
        entradaSplit.pop(counter-2)                                                                
        print(entradaSplit)
        counter=counter-2
    if entradaSplit[counter] == '/':
        entradaSplit[counter-1] = float(entradaSplit[counter-2]) / float(entradaSplit[counter-1])
        entradaSplit.pop(counter)
        entradaSplit.pop(counter-2)
        print(entradaSplit)
        counter=counter-2
    if entradaSplit[counter] == '-':
        entradaSplit[counter-1] = float(entradaSplit[counter-2]) - float(entradaSplit[counter-1])
        entradaSplit.pop(counter)
        entradaSplit.pop(counter-2)
        print(entradaSplit)
        counter=counter-2
    if entradaSplit[counter] == '+':
        entradaSplit[counter-1] = float(entradaSplit[counter-2]) + float(entradaSplit[counter-1])
        entradaSplit.pop(counter)
        entradaSplit.pop(counter-2)
        print(entradaSplit)
        counter=counter-2

    counter=counter+1

print('\n','Resultado: ','\n',entradaSplit[0])
print('\n','--- %s seconds ---' % (time.time() - start_time))

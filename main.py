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
#Recorridos dobles dentro de matrices 
#los numeros impares los divide entre 2 y los pares los multiplica por 2 
matriz = [[5, 7, 6, 9], [3, 4, 2, 8], [7, 9, 6, 1]]
i = 0
while i < len(matriz):
    j = 0
    while j < len(matriz[i]):
        if matriz[i][j]%2 == 0:
            matriz[i][j]*=2
        else:
            matriz[i][j]/=2    
        j+=1    
    i+=1
print(matriz)    
"""
1. Analise o trecho de código abaixo e selecione entre as alternativas o que será exibido após a execução.
Algoritmo questão;
var
    a, b, d : inteiro;
    v[4] : inteiro;
inicio
       a <- 3;
        b <- 2;
        v[4] <- {6,7,8,9}; // inicialização do vetor, de forma correta.
        a = (v[2] – v[0]) + a;
        d <- a * v[b]; //o caractere * significa multiplicação
        escreva(“ a saída é: “, d, “ “, v[1], a+2);
fim.
"""

# transformei o cód acima escrito em Portugol pra Python:

# declarando var sem precisar declarar tipo
a = 3
b = 2
v = [6, 7, 8, 9] # lista/array (0 -> 6, 1 -> 7 etc.)

a = (v[2] - v[0]) + a
d = a * v[b]

print(f"A saída é: {d} {v[1]} {a+2}")

# Output: 40 7 7, pq:
    # a * v[b] --> onde v[b] corresponde ao v[2], logo, o valor é 8
    # na saída, d = 40, v[1] = 7, a+2 é a = 5 (novo valor) + 2 = 7
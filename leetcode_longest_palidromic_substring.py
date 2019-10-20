"""
Sumário
Este artigo é para leitores intermediários. Ele apresenta as seguintes idéias: Palíndromo, Programação Dinâmica e 
Manipulação de Cordas. Certifique-se de entender o que significa um palíndromo. Um palíndromo é uma sequência que lê o 
mesmo em ambas as direções. Por exemplo,SS = "aba" é um palíndromo,SS = "abc" não é.

Solução
Abordagem 1: Substring comum mais longo
Erro comum

Algumas pessoas ficarão tentadas a encontrar uma solução rápida, que infelizmente é falha (no entanto, pode ser 
facilmente corrigida):

Marcha ré SS e se tornarS 'S 
′
  . Encontre a substring comum mais longa entreSS eS 'S 
′
  , Que também deve ser o substrato palindrômico mais longo.

Isso pareceu funcionar, vamos ver alguns exemplos abaixo.

Por exemplo, SS = "caba"S 'S 
′
  = "Abac".

A substring comum mais longa entre SS eS 'S 
′
  É "aba", que é a resposta.

Vamos tentar outro exemplo: SS = "abacdfgdcaba",S 'S 
′
  = "Abacdgfdcaba".

A substring comum mais longa entre SS eS 'S 
′
  É "abacd". Claramente, este não é um palíndromo válido.

Algoritmo

Pudemos ver que o método de substring comum mais longo falha quando existe uma cópia reversa de um substring não 
palindrômico em alguma outra parte do SS . Para corrigir isso, cada vez que encontramos um candidato mais longo da 
substring comum, verificamos se os índices da substring são iguais aos índices originais da substring reversa. 
Se for, tentamos atualizar o palíndromo mais longo encontrado até agora; caso contrário, pularemos isso e encontraremos 
o próximo candidato.

Isso nos dá uma O (n ^ 2)O ( n 
2
  )Solução de programação dinâmica que usaO (n ^ 2)O ( n 
2
  )espaço (poderia ser melhorado para usarEm)O ( n ) espaço). Leia mais sobre Substring comum mais longaaqui.


Abordagem 2: Força Bruta
A solução óbvia de força bruta é escolher todas as posições possíveis de início e de término para uma substring e 
verificar se é um palíndromo.

Análise de complexidade

Complexidade do tempo: O (n ^ 3)O ( n 
3
  ). Assuma issonn é o comprimento da sequência de entrada, há um total de
  binom {n} {2} = \
  frac {n (n-1)} {2}( 
2
n
 )= 
2
n ( n - 1 )
 tais substrings (excluindo a solução trivial em que um personagem em si é um palíndromo). Como a verificação de cada 
 substring levaEm)O ( n ) tempo, a complexidade do tempo de execução éO (n ^ 3)O ( n 
3
  ).

Complexidade do espaço: O (1)S ( 1 ) .


Abordagem 3: Programação Dinâmica
Para melhorar a solução de força bruta, primeiro observamos como podemos evitar recálculos desnecessários ao validar 
palíndromos. Considere o caso "ababa". Se já sabíamos que "bab" é um palíndromo, é óbvio que "ababa" deve ser um 
palíndromo, pois as duas letras da esquerda e da direita são as mesmas.

Nós definimos P (i, j)P ( i ,j ) como se segue:

P (i, j) = begin {cases} text {true,} & quad text {se a substring} S_i dots S_j text {for um palíndromo} 
text {false,} & quad text {caso contrário.} end {cases}P ( i ,j )={ 
verdadeiro,
falsa,
  
se a substring  S 
Eu
 ...S 
j
  é um palíndromo
contrário.
 

Portanto,

P (i, j) = (P (i + 1, j-1) 
text {e} S_i == S_j)P ( i ,j )=( P ( i+1 ,j-1 )  e  S 
Eu
 ==S 
j
 )

Os casos base são:

P (i, i) = verdadeiroP ( i ,i )=t r u e

P (i, i + 1) = (S_i == S_ {i + 1})P ( i ,Eu+1 )=( S 
Eu
 ==S 
i + 1
 )

Isso produz uma solução direta de DP, que primeiro inicializamos os palíndromos de uma e duas letras e trabalhamos até
encontrar todos os três palíndromos de letras, e assim por diante ...

Análise de complexidade

Complexidade do tempo: O (n ^ 2)O ( n 
2
  ). Isso nos dá uma complexidade de tempo de execução deO (n ^ 2)O ( n 
2
  ).

Complexidade do espaço: O (n ^ 2)O ( n 
2
  ). UsaO (n ^ 2)O ( n 
2
  )espaço para guardar a mesa.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        m = ''  # Memory to remember a palindrome
        for i in range(len(s)):  # i = start, O = n
            for j in range(len(s), i, -1):  # j = end, O = n^2
                if len(m) >= j - i:  # To reduce time
                    break
                elif s[i:j] == s[i:j][::-1]:
                    m = s[i:j]
                    break
        return m

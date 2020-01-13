"""
Sumário
Este artigo é para leitores intermediários. Ele apresenta as seguintes idéias: Palíndromo, Programação Dinâmica e 
Manipulação de Cordas. Certifique-se de entender o que significa um palíndromo. Um palíndromo é uma sequência que lê o 
mesmo em ambas as direções. Por exemplo,SS = "aba" é um palíndromo,SS = "abc" não é.

Solução

Abordagem de Força Bruta
A solução óbvia de força bruta é escolher todas as posições possíveis de início e de término para uma substring e 
verificar se é um palíndromo.

Análise de complexidade

Complexidade do espaço: O (1) S (1).

Isso produz uma solução direta de DP, que primeiro inicializamos os palíndromos de uma e duas letras e trabalhamos até
encontrar todos os três palíndromos de letras, e assim por diante ...

Análise de complexidade
Complexidade do tempo: O (n ^ 2)O ( n 2). Isso nos dá uma complexidade de tempo de execução deO (n ^ 2)O ( n 2).
Complexidade do espaço: O (n ^ 2)O ( n 2). UsaO (n ^ 2)O ( n 2)espaço para guardar a mesa.
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

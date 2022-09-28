# Aula 03 - exercício 01 - listas
import os
os.system('cls')

def checkPalindrome(exp):
        exp_rev = exp
        exp_rev.reverse()
        return exp == exp_rev

def main():
        frase = list(input("Digite uma frase: "))
        print(f"É palíndromo? {checkPalindrome(frase)}")

main()
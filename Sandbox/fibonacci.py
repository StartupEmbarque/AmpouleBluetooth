__author__ = 'Yaiba'

def fibonacci(n):
    if n==1 or n==2:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
while True :
    n = int(input('Entrez le nombre inférieur à 50 que vous voulez \n (pas au dessus, '))
    print(fibonacci(n))

# Questão 02 - Estagio - São Paulo
def pertence_fibonacci(n):
    """
    Verifica se um número pertence à sequência de Fibonacci.
    """
    # Inicializando os dois primeiros números da sequência
    a, b = 0, 1
    
    # Continuar enquanto o valor de b for menor que n
    while b < n:
        a, b = b, a + b
    
    # Verifica se o número informado está na sequência
    return b == n

def main():
    # Solicita ao usuário que informe um número
    try:
        numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
        
        # Verifica se o número pertence à sequência
        if pertence_fibonacci(numero):
            print(f"O número {numero} pertence à sequência de Fibonacci.")
        else:
            print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")
    
    except ValueError:
        print("Por favor, informe um número inteiro válido.")

if __name__ == "__main__":
    main()
```
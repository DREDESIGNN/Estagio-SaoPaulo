# Estagio-SaoPaulo
Técnica:

Questão 1:

O programa soma todos os números de 1 até 13.
Resultado:
Ao final do processamento, o valor da variável SOMA será 91.

Passo a passo do código:

1 - Inicialização:
'INDICE' é definido como 13.
'SOMA' é inicializada com 0.
'K' é inicializada com 0.

2 - Loop (Enquanto K < INDICE):
A variável 'K' é incrementada em 1 a cada iteração ('K = K + 1').
O valor de 'K' é adicionado à variável 'SOMA' a cada iteração ('SOMA = SOMA + K').

3 - Condições de execução:
O loop continua até que 'K' seja igual a 13.

Cálculo:

Vamos fazer as somas manualmente para cada iteração:

Quando 'K = 1':'SOMA = 0 + 1 = 1'

Quando 'K = 2':'SOMA = 1 + 2 = 3'

Quando 'K = 3':'SOMA = 3 + 3 = 6'

Quando 'K = 4':'SOMA = 6 + 4 = 10'

Quando 'K = 5':'SOMA = 10 + 5 = 15'

Quando 'K = 6':'SOMA = 15 + 6 = 21'

Quando 'K = 7':'SOMA = 21 + 7 = 28'

Quando 'K = 8':'SOMA = 28 + 8 = 36'

Quando 'K = 9':'SOMA = 36 + 9 = 45'

Quando 'K = 10':'SOMA = 45 + 10 = 55'

Quando 'K = 11':'SOMA = 55 + 11 = 66'

Quando 'K = 12':'SOMA = 66 + 12 = 78'

Quando 'K = 13':'SOMA = 78 + 13 = 91'

______________________________________________________________________________________________________________________________________________________________________
Questão 2:

Explicação do Código:

1 - Função 'pertence_fibonacci(n)':
Inicializa os primeiros dois números da sequência de Fibonacci ('0' e '1').
Usa um loop 'while' para gerar números da sequência até que o valor de 'b' seja maior ou igual ao número informado ('n').
Verifica se o número informado ('n') é igual ao último valor de 'b' gerado na sequência. Se sim, retorna 'True', indicando que o número pertence à sequência; caso contrário, retorna 'False'.

2 - Função 'main()':
Solicita ao usuário que informe um número e o converte para um inteiro.
Usa a função 'pertence_fibonacci()' para verificar se o número informado pertence à sequência.
Exibe uma mensagem apropriada com base no resultado da verificação.
Inclui tratamento de exceção para garantir que o usuário informe um número inteiro válido.

3 - Bloco 'if __name__ == "__main__":':
Garante que a função 'main()' seja executada apenas quando o script é executado diretamente e não quando importado como módulo.

______________________________________________________________________________________________________________________________________________________________________
Questão 3:

Explicação do Código:

1 - Função 'carregar_dados_json(caminho_arquivo)':
Carrega os dados de faturamento a partir de um arquivo JSON e retorna a lista de faturamento diário.

2 - Função 'calcular_faturamento(dados)':
Filtra os valores de faturamento para ignorar os dias sem faturamento (valores iguais a 0).
Calcula o menor e o maior valor de faturamento.
Calcula a média de faturamento diário, excluindo os dias sem faturamento.
Conta o número de dias em que o faturamento foi superior à média mensal.

3 - Função 'main()':
Carrega os dados do arquivo JSON.
Calcula os valores solicitados.
Exibe os resultados.

_______________________________________________________________________________________________________________________________________________________________________
Questão 4:

Explicação do Código:

1 - Dicionário 'faturamento':
Armazena os valores de faturamento para cada estado.

2 - Cálculo do faturamento total:
A função 'sum()' é usada para somar todos os valores do dicionário e obter o faturamento total.

3 - Cálculo do percentual para cada estado:
Itera sobre cada item no dicionário faturamento e calcula o percentual correspondente para cada estado.

4 - Exibição dos resultados:
Imprime o percentual de cada estado e o faturamento total.

________________________________________________________________________________________________________________________________________________________________________
Questão 5:


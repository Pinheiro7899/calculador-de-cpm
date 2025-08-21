# calculador-de-cpm
Sistema em Python para calcular CPM (Custo por Mil impressões): (custo/impressões)*1000. Menu interativo permite calcular CPM, exibir histórico em lista e sair. Usa operadores, condicionais, laços, break, continue, pass e métodos de listas. Valida entradas e armazena cálculos. Extensível e robusto.

Objetivo:
O projeto consiste em um sistema interativo em Python para calcular o Custo por Mil (CPM), uma métrica de marketing digital que determina o custo de uma campanha publicitária por mil impressões. A fórmula utilizada é:
$$CPM = \left(\frac{\text{Custo Total da Campanha}}{\text{Número de Impressões}}\right) \times 1000$$
O sistema permite ao usuário calcular o CPM, armazenar os cálculos em um histórico e exibir os resultados anteriores, utilizando conceitos fundamentais de programação em Python descritos no documento 4.2.txt (operadores aritméticos, de comparação, lógicos, estruturas condicionais, laços, break, continue, pass e métodos de listas).

Funcionalidades

Cálculo de CPM:

Solicita o custo total da campanha (em reais) e o número de impressões.
Calcula o CPM usando operadores aritméticos (/ e *), arredondando o resultado para duas casas decimais.
Valida entradas com operadores de comparação (>=, ==) e lógicos (or) para evitar valores negativos, zero impressões ou entradas não numéricas.
Armazena cada cálculo (custo, impressões e CPM) em uma lista usando o método append.


Histórico de Cálculos:

Mantém uma lista mutável (historico_cpm) para armazenar os cálculos como dicionários (ex.: {"custo": 500, "impressoes": 100000, "cpm": 50.0}).
Permite exibir o histórico usando um laço for para iterar sobre a lista, mostrando cada cálculo numerado.


Menu Interativo:

Usa um laço while para apresentar um menu com três opções:

Calcular novo CPM.
Exibir histórico de cálculos.
Sair do programa.


Gerencia escolhas com estruturas condicionais (if, elif, else).
Usa break para sair do programa e continue para pular iterações inválidas (ex.: entradas incorretas).


Validações:

Captura erros de entrada (ex.: texto em vez de números) com try-except.
Verifica valores negativos ou zero com mensagens claras (ex.: "Erro: Custo e impressões devem ser não negativos.").
Evita divisão por zero retornando None na função de cálculo.


Extensibilidade:

Inclui a instrução pass como marcador para futuras funcionalidades (ex.: ordenar histórico com sort, salvar em arquivo).




Estrutura Técnica

Linguagem: Python.
Conceitos Utilizados (baseados no documento 4.2.txt):

Operadores Aritméticos: Divisão (/) e multiplicação (*) para calcular o CPM.
Operadores de Comparação: ==, <, >= para validar entradas.
Operadores Lógicos: or para combinar condições de validação.
Condicionais: if, elif, else para gerenciar o menu e validações.
Laços:

while para o menu interativo.
for para exibir o histórico.


Break: Encerra o programa na opção de sair.
Continue: Pula iterações inválidas.
Pass: Marcador para expansões futuras.
Listas e Métodos:

Lista historico_cpm para armazenar cálculos.
append para adicionar cálculos.
len para verificar se a lista está vazia.




Entradas: Custo (float), impressões (float), opção do menu (string).
Saídas: CPM calculado, histórico formatado, mensagens de erro.


Exemplo de Uso

Menu:
textRecolherEncapsularCopiar=== Calculadora de CPM ===
1. Calcular novo CPM
2. Exibir histórico de cálculos
3. Sair
Escolha uma opção (1, 2 ou 3):

Cálculo de CPM:

Entrada: Custo = 500, Impressões = 100000
Saída: O CPM é: R$50.0
Ação: Adiciona {"custo": 500, "impressoes": 100000, "cpm": 50.0} ao histórico.


Histórico:

Saída:
textRecolherEncapsularCopiar=== Histórico de Cálculos ===
Cálculo 1: Custo = R$500.0, Impressões = 100000, CPM = R$50.0
Cálculo 2: Custo = R$200.0, Impressões = 5000, CPM = R$40.0



Erro:

Entrada: Custo = -500
Saída: Erro: Custo e impressões devem ser não negativos.


Saída do Programa:

Entrada: Opção 3
Saída: Saindo do programa...




Benefícios

Simplicidade: Interface clara e intuitiva com menu interativo.
Robustez: Validações garantem que o sistema não quebre com entradas inválidas.
Flexibilidade: O histórico permite acompanhar cálculos anteriores, e o uso de pass facilita expansões.

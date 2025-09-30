# 🚀 Meus Primeiros Passos com Python

Bem-vindo ao meu repositório de aprendizado! Aqui eu guardo pequenos scripts que crio para praticar e entender conceitos fundamentais da linguagem Python. Cada arquivo foca em um desafio ou técnica diferente.

## 📂 Scripts no Repositório

### 1. Arquivo 1: Dobrador de Números com Tratamento de Erros

Este script pede ao usuário um número e calcula o seu dobro. O principal conceito demonstrado aqui é o **tratamento de exceções** com `try...except`, que torna o programa mais robusto e amigável.



#### 🧠 O que ele ensina:
-   **Captura de Entrada:** A função `input()` sempre retorna o que o usuário digita como um **texto (string)**.
-   **Conversão de Tipo (Casting):** A necessidade de converter a string de entrada para um número (`float()`) antes de fazer cálculos matemáticos.
-   **Tratamento de Erros (`try...except`):**
    -   O bloco `try` tenta executar um código que pode falhar (a conversão para `float`).
    -   Se a conversão falhar (por exemplo, se o usuário digitar "olá"), em vez de o programa quebrar, o bloco `except` é executado, exibindo uma mensagem de erro controlada.

---

### 2. Arquivo 2: Simulador de Radar de Velocidade

Este script simula um radar de trânsito. Ele verifica se um carro, com base em sua velocidade e localização, passou por um radar acima do limite de velocidade. O foco aqui é a **lógica booleana** e a criação de condições complexas.



#### 🧠 O que ele ensina:
-   **Nomenclatura de Variáveis:** O uso de nomes descritivos (como `vel_carro_passou_radar_1`) e constantes em maiúsculas (como `RADAR_1`) para deixar o código mais legível.
-   **Lógica Booleana:** As variáveis podem armazenar valores `True` ou `False`, que são o resultado de comparações (`>`).
-   **Operadores Lógicos (`and`):** Como combinar múltiplas condições. Para `carro_multado_radar_1` ser `True`, **todas** as três condições precisam ser verdadeiras.
-   **Estruturas Condicionais (`if`):** Como executar um bloco de código apenas se uma determinada condição for `True`.

---

### 3. Arquivo 3: Calculadora de Soma Simples

Este script pede ao usuário dois números e exibe a soma deles. O destaque deste código é a conversão de tipo no momento do uso e a introdução de **f-strings** para formatar a saída de forma limpa.



#### 🧠 O que ele ensina:
-   **Conversão de Tipo "On-the-fly":** A conversão de `string` para `float` é feita diretamente dentro da expressão matemática, tornando o código mais conciso.
-   **Importância da Conversão:** Demonstra que, sem o `float()`, o operador `+` iria **concatenar** os textos (ex: `"5" + "3"` se tornaria `"53"`) em vez de somar os números.
-   **Strings Formatadas (f-strings):**
    -   A letra `f` antes das aspas (`f'...'`) ativa a formatação.
    -   Permite embutir variáveis e expressões diretamente dentro do texto usando chaves `{}`.
    -   É a maneira moderna e mais legível de formatar strings em Python.

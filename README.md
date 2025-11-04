# Desafio de Automação Digital (Intro Python)

Sistema de **inspeção e armazenamento de peças** para disciplina de Algoritmos e Lógica de Programação (nível introdutório).  
Sem bibliotecas externas, apenas **condicionais e laços**.

## Funcionalidades
- Cadastro de peça (id, peso, cor, comprimento)
- Validação de qualidade:
  - **Peso** entre `95g` e `105g`
  - **Cor** `azul` ou `verde`
  - **Comprimento** entre `10cm` e `20cm`
- Armazenamento em **caixas de 10 peças**
- Fechamento automático da caixa ao atingir a capacidade
- Remoção de peça por ID (reorganiza as caixas automaticamente)
- Listagem de peças aprovadas / reprovadas
- Listagem de **caixas fechadas**
- **Relatório final** (aprovadas, reprovadas por motivo e total de caixas)

## Como rodar
1. Tenha o **Python 3.8+** instalado.
2. No terminal, vá até a pasta do projeto:
   ```bash
   cd automacao_pecas_intro_python
   ```
3. Execute:
   ```bash
   python3 main.py
   ```

## Exemplos de entrada
- ID: `P001`
- Peso: `100`
- Cor: `azul`
- Comprimento: `15`

## Dicas de uso (nível introdutório)
- IDs devem ser **únicos**.
- Se remover uma peça, as caixas são **remontadas** a partir das aprovadas.
- As mensagens do menu explicam cada passo.

## Estrutura do projeto
```
automacao_pecas_intro_python/
├─ main.py
└─ README.md
```

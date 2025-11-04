# Parte Teórica — Análise e Discussão 

## Contexto do desafio
A automação em linhas de montagem reduz **atrasos, erros de conferência** e **custos operacionais**. Com regras simples de qualidade e uma lógica de armazenamento previsível, é possível **padronizar a inspeção** e gerar relatórios mais confiáveis para decisões rápidas.

## Lógica e raciocínio
- **Entradas**: `id`, `peso`, `cor`, `comprimento`.
- **Processamento**:
  - Condicionais (`if/elif/else`) verificam os limites de **peso** (95–105g), **cor** (azul/verde) e **comprimento** (10–20cm).
  - Quando a peça é aprovada, é adicionada à **caixa atual**. Se a caixa atinge 10 peças, ela é **fechada** e uma nova caixa é iniciada.
  - Em caso de **remoção** de qualquer peça, as caixas são **recriadas** linearmente (simples, previsível).
- **Saídas**: listagens e relatório consolidado (aprovadas, reprovadas por motivo, número de caixas).

## Estruturas e controles básicos utilizados
- **Listas** para coleções de peças e caixas.
- **Dicionários** para representar cada peça com campos nomeados.
- **Laços** `while` e `for` para percorrer menus e coleções.
- **Condicionais** para aplicar as regras de qualidade.

## Boas práticas adotadas (nível iniciante)
- **Validação de entrada** numérica com tratamento de erro simples.
- **IDs únicos** por peça.
- Funções pequenas e coesas: avaliação, embalagem, reempacotamento e relatório.
- **Mensagens claras** ao usuário (fluxo de menu).
- Sem recursos avançados (classes/arquivos/bancos), focando em lógica básica.

## Benefícios e desafios
- **Benefícios**: padronização, rapidez na conferência, rastreabilidade simples por ID, relatório imediato.
- **Desafios**: tratar entradas inválidas, manter consistência ao remover peças (resolvido com **reempacotamento**).

## Expansões possíveis
- Persistência em **arquivo CSV/JSON** ou banco local para manter histórico.
- Integração com **sensores** (peso e comprimento) e **visão computacional** (cor).
- Interface **gráfica** simples para operadores.
- Uso de **APIs**/fila para integração industrial; aplicação de **IA** para detecção de anomalias.

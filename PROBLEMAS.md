# Problemas Identificados — Leitura Inicial do Código

Este arquivo é preenchido pelos estudantes na Aula 1 após a leitura do código legado.
Descreva em linguagem livre tudo que parecer estranho, errado ou difícil de entender.
Não é necessário usar termos técnicos neste momento.

WAGNER_BARRAL_DA_CONCEICAO_BSI

---

## Minha leitura inicial

*(Espaço reservado para o estudante preencher)*

Exemplo de entradas:
- "A classe faz muita coisa ao mesmo tempo"
- "Tem código de e-mail misturado com o cálculo de multa"
- "O mesmo cálculo aparece duas vezes no código"
- "As listas de equipamentos estão fora da classe, soltas no arquivo"

01-Uso de variáveis globais (alto acoplamento)

02-A classe faz lógica de negócio e notificação (print simulando email).

03-Cálculo de multa duplicado (violação do DRY)

04-O sistema não é aberto para extensão — para adicionar um novo tipo de equipamento, precisa alterar o código.

05-A função main() está no mesmo arquivo e diretamente acoplada à lógica do sistema.



---

## Revisão com vocabulário técnico

*(Este espaço será preenchido após a Aula 4, quando os termos técnicos corretos forem aprendidos)*

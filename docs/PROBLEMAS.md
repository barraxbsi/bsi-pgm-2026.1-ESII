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

>01 — Uso de variáveis globais

O sistema apresenta alto acoplamento por estado global, pois diferentes partes do código dependem diretamente de variáveis compartilhadas. Isso dificulta manutenção, testes e previsibilidade do comportamento.

>02 — A classe faz lógica de negócio e notificação

Há baixa coesão e mistura de responsabilidades, porque a mesma classe executa regras de negócio e envio de notificações (print simulando e-mail). Isso viola o princípio SRP (Single Responsibility Principle).

>03 — Cálculo de multa duplicado

O código viola o princípio DRY (Don’t Repeat Yourself), pois a mesma lógica de cálculo aparece repetida em mais de um ponto do sistema, aumentando risco de inconsistências e dificuldade de manutenção.

>04 — O sistema não é aberto para extensão

O sistema viola o princípio OCP (Open/Closed Principle), já que adicionar um novo tipo de equipamento exige modificar código existente em vez de apenas estender comportamentos.

>05 — A função main() está no mesmo arquivo e diretamente acoplada à lógica do sistema

Existe forte acoplamento entre interface/executável e regras de negócio, além de ausência de separação de responsabilidades. Isso reduz modularidade e dificulta reutilização e testes do sistema.

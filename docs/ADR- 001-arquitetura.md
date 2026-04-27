## Arquitetura

**Versão:** 2.0
**Data:** Abril de 2026


## 1.0 Contexto:
O sistema precisa evoluir para uma nova versão mantendo qualidade estrutural e facilidade de manutenção. Para isso, deve atender aos seguintes requisitos não funcionais:

RNF03: o sistema deve permitir a adição de novos tipos sem a necessidade de modificar múltiplos módulos, evitando alto acoplamento e facilitando a evolução.

RNF04: as regras de negócio devem poder ser testadas de forma isolada, sem depender de estado externo (como arquivos, banco de dados ou entrada do usuário).

O problema central é definir uma organização de código que permita atender a esses dois requisitos ao mesmo tempo, sem introduzir complexidade excessiva para uma aplicação de linha de comando e uma equipe iniciante.

## 2.0 Opções consideradas:

   **Arquivo único**

     Estrutura simples, com todo o código em um único arquivo.

   **Problemas:**

-Alto acoplamento: qualquer mudança impacta várias partes do código.

-Dificulta a adição de novos tipos sem modificar diferentes trechos (não atende RNF03).

-Regras de negócio ficam misturadas com entrada/saída, dificultando testes isolados (não atende RNF04).

-Motivo do descarte: não escala e compromete extensibilidade e testabilidade.


## MVC

Divide o sistema em Model, View e Controller.

  **Pontos positivos:**

    Boa separação de responsabilidades.
    Permite testar o Model de forma isolada.
  **Problemas:**

      -Estrutura mais complexa do que o necessário para uma aplicação CLI.
      -Introduz conceitos (como View) pouco úteis no contexto.
  **Motivo do descarte:** 

      -atende os requisitos, mas com custo de complexidade maior que o necessário para o projeto e a equipe.

## Arquitetura em camadas

Organiza o sistema em camadas com responsabilidades bem definidas.
   **Pontos positivos:**

      Permite isolar regras de negócio (atende RNF04).
      Facilita a adição de novos tipos com impacto localizado (atende RNF03).
      Estrutura simples e adequada para CLI.
  **Motivo da escolha:** 

melhor equilíbrio entre simplicidade, organização e capacidade de evolução do sistema.

## 3.0 Decisão:

      Será adotada a arquitetura em camadas, organizando o sistema em módulos com responsabilidades bem definidas.
        As camadas serão estruturadas da seguinte forma:

   **src/interface/**
        
        Responsável pela interação com o usuário via CLI.
        Contém leitura de entrada (comandos) e exibição de saída no terminal.
   **src/application/**

        Contém os casos de uso do sistema.
        Coordena o fluxo de execução, recebendo dados da interface e acionando o domínio.
   **src/domain/**

        Núcleo do sistema, contendo entidades e regras de negócio.
        Não depende de nenhuma outra camada, permitindo testes isolados.
   **src/infrastructure/**

        Responsável por detalhes técnicos, como persistência de dados, arquivos ou integrações externas.

## Fluxo de dependência:
   **interface → application → domain → infrastructure**

      Essa organização garante separação clara de responsabilidades sem introduzir complexidade excessiva para o contexto do projeto.

## 4.0 Consequências:

**Impactos positivos:**

  -Redução do acoplamento entre partes do sistema
  
  -Facilidade para adicionar novos tipos com impacto localizado (atende RNF03)
  
  -Regras de negócio isoladas e testáveis sem dependências externas (atende RNF04)
  
  -Código mais organizado e fácil de manter
  
  -Estrutura adequada para aplicações CLI

**Impactos negativos:**

  -Aumento na quantidade de arquivos e diretórios
  
  -Necessidade de disciplina para respeitar a separação entre camadas
  
  -Leve curva de aprendizado para a equipe iniciante.
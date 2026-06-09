## Aula 04 — SRP:

A decisão de fronteira mais difícil foi separar o Notificador do
ServicoEmprestimo. Inicialmente, parecia natural deixar os prints de
“email” dentro do serviço, porque as notificações acontecem logo após
as regras de negócio. Porém, analisando com a lente de SRP, percebi que
existiam dois motivos diferentes para mudança: alterações nas regras de
empréstimo e alterações na forma de notificação.

O que tornou essa decisão difícil foi que ambos os comportamentos fazem
parte do mesmo fluxo de uso do sistema. Separar excessivamente também
poderia aumentar o número de classes e o acoplamento entre módulos.
Mesmo assim, decidi separar porque o critério principal do SRP não é a
quantidade de código, mas sim a existência de um único motivo de mudança.

Minha decisão foi baseada no Capítulo 5 de Valente, especialmente na
ideia de coesão e responsabilidade única. O autor argumenta que módulos
bem projetados devem agrupar responsabilidades relacionadas e evitar
misturar comportamentos que evoluem por razões diferentes. Assim,
o ServicoEmprestimo ficou responsável apenas pelas regras de negócio,
enquanto o Notificador ficou isolado para comunicação externa.


## Aula 05 — OCP

A hierarquia criada aplica OCP via polimorfismo, funcionando bem para variações por **tipo** de equipamento. Porém, tem limites com requisitos radicalmente novos.

Se surgir um equipamento com multa **por hora** (não por dia) ou política dependente do **dia da semana**, a decomposição atual seria **insuficiente**. Adicionar novo tipo (`EquipamentoPorHora`) respeita OCP, mas mudar a **lógica de cobrança** para todos exigiria modificar múltiplas classes, violando o princípio.

Valente (Cap. 5) afirma: *"O OCP recomenda pensar nos pontos de extensão já na implementação, mas não é possível prever todas as evoluções futuras. Quando a variação não é por tipo, mas por estratégia ou contexto, herança torna-se inadequada e outros mecanismos como o padrão Strategy são necessários"* [Valente, Cap. 5].

Nesses casos, uma abordagem baseada em **estratégia** (padrão de projeto) ou **funções de cálculo injetadas** seria mais flexível, permitindo novas políticas sem criar subclasses ou modificar código existente.

**Referência:**  
Valente, M. T. *Engenharia de Software Moderna*, Capítulo 5 — Princípios de Projeto. Disponível em https://engsoftmoderna.info/cap5.html


## Aula 09 — TDD

Ao comparar TDD e BDD, considero que o BDD comunica melhor com clientes não técnicos. Os cenários escritos no formato Dado-Quando-Então utilizam uma linguagem próxima das regras de negócio, permitindo que pessoas sem conhecimento de programação entendam o comportamento esperado do sistema. Já o TDD é mais adequado para desenvolvedores, pois os testes automatizados descrevem o comportamento de forma técnica e verificável pelo código.

Eu prefiro utilizar TDD durante a implementação porque ele fornece feedback rápido, ajuda a evitar erros e incentiva a criação de código mais simples e testável. Por outro lado, o BDD é mais útil quando há necessidade de alinhar expectativas entre clientes, analistas e equipe de desenvolvimento. Dessa forma, as duas abordagens são complementares: o BDD ajuda a definir o que deve ser construído e o TDD auxilia na construção correta da solução.

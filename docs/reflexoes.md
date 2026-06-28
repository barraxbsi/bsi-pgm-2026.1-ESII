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


## Aula 06 — Verificação de LSP
Verifiquei as subclasses Notebook, Projetor e Cabo a partir do contrato da classe base. Como o contrato exige que calcular_multa(...) retorne um float maior ou igual a zero, sem exceção inesperada, as três subclasses satisfazem o LSP se, para 0 e para valores negativos como -5, retornarem 0.0 e não lançarem erro. Nesse caso, o ServicoEmprestimo pode tratá-las de forma uniforme, sem precisar conhecer detalhes internos de cada equipamento. Se alguma subclasse retornasse valor negativo ou lançasse exceção para entrada que a classe base aceita, ela quebraria o serviço, porque o cálculo de multa deixaria de ser confiável.

## Aula 06 — DIP
O DIP mudou a relação entre os módulos porque ServicoEmprestimo deixou de criar suas próprias dependências e passou a recebê-las de fora. Isso não é só uma mudança técnica no construtor; é uma mudança conceitual de controle. Antes, o serviço “mandava” na criação de repositório e notificador; agora ele apenas consome abstrações já prontas, e quem decide as implementações concretas é o módulo de composição, como main.py. Essa inversão reduz o acoplamento e melhora a testabilidade, porque permite substituir as dependências reais por falsos objetos em memória. Como destaca Valente em Engenharia de Software Moderna, a inversão de dependência orienta o código para depender de abstrações, e não de detalhes concretos, tornando o sistema mais flexível e menos rígido. Na prática, isso quita a dívida técnica da v1.0 relacionada à testabilidade isolada das regras de negócio.

## Aula 12 — Refactoring e Code Smells

Os testes funcionaram como rede de segurança durante a Aula 12, porque cada alteração no código pôde ser validada com `pytest` antes de seguir para o próximo passo. Isso foi importante principalmente na troca do evento de `dict` para `Evento`, pois a mudança mexeu na estrutura interna sem alterar o comportamento observável do sistema. Quando o teste permaneceu verde, ficou claro que a refatoração preservou o funcionamento; quando algum ajuste exigisse quebra de contrato, o teste indicaria o problema imediatamente. Sem essa proteção, eu teria que confiar só na leitura manual do código, o que aumenta bastante o risco de introduzir falhas enquanto reorganizo nomes, funções e estruturas.

O falso positivo das subclasses vazias após o Strategy aparece porque, à primeira vista, elas lembram uma Data Class: têm poucos ou nenhum método e parecem guardar só identidade. Mas nesse caso elas não são um erro de design. Elas existem para representar tipos diferentes de equipamento e sustentar a solução baseada em Strategy e OCP. Aplicar `Inline Class` ou dissolver essas subclasses desfaria a intenção arquitetural já conquistada na Aula 11. Por isso, mesmo parecendo um smell, a decisão correta é não refatorar esse ponto.
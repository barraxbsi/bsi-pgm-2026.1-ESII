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
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

A hierarquia criada aplica o Princípio Aberto/Fechado (OCP) através de polimorfismo, funcionando bem para variações por tipo de equipamento. No entanto, sua eficácia tem limites quando enfrentamos requisitos radicalmente novos.

Se surgisse um equipamento cuja multa fosse cobrada **por hora** em vez de por dia, ou cuja política dependesse do **dia da semana**, a decomposição atual seria **insuficiente** e exigiria reestruturação. Adicionar um novo tipo de equipamento (ex: `EquipamentoPorHora`) exigiria criar uma nova subclasse, o que respeita o OCP. Porém, mudar a **lógica de cobrança** para todos os tipos existentes (ex: de "por dia" para "por hora") demandaria modificar múltiplas classes, violando o princípio.

Valente (Cap. 5) explícitamente discute os limites do OCP: *"O OCP recomenda pensar nos pontos de extensão já no momento da implementação, mas não é possível prever todas as evoluções futuras. Quando a variação não é por tipo, mas por estratégia ou contexto, herança torna-se inadequada e outros mecanismos como o padrão Strategy são necessários"* [Valente, Cap. 5].

Nesses casos, uma abordagem baseada em **estratégia** (padrão de projeto) ou **funções de cálculo injetadas** seria mais flexível, permitindo novas políticas de multa sem criar subclasses ou modificar código existente.

---

**Referência:**  
Valente, M. T. *Engenharia de Software Moderna: Princípios e Práticas para Desenvolvimento de Software com Produtividade*, Capítulo 5 — Princípios de Projeto, seção sobre OCP. Disponível em https://engsoftmoderna.info/cap5.html
"""

print("Conteúdo dos arquivos para o exercício OCP:")
print("=" * 60)
print("\n1. models/equipamento.py:")
print("-" * 40)
print(import_text)
print("\n2. repositories/repositorio_emprestimo.py:")
print("-" * 40)
print(repositorio_text)
print("\n3. services/servico_emprestimo.py:")
print("-" * 40)
print(servico_text)
print("\n4. docs/reflexoes.md:")
print("-" * 40)
print(reflexao_text)
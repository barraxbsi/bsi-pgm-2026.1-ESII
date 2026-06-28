# Diagnóstico Aula 12

| Arquivo:linha | Smell técnico | Refactoring proposto | Justificativa |
|---|---|---|---|
| services/notificador_email.py | Primitive Obsession | Replace Primitive with Object | O evento era representado por `dict`, com chaves mágicas como `tipo`, `email`, `data` e `multa`, em vez de um tipo explícito. |
| repositories/repositorio_emprestimo.py | Primitive Obsession | Replace Data Value with Object | Equipamentos ainda são representados como `dict`, o que espalha acesso por chaves e fragiliza o domínio. |
| repositories/repositorio_emprestimo.py | Data Clumps | Extract Class | `nome`, `tipo` e `disponivel` aparecem sempre juntos, indicando um agrupamento implícito de dados. |
| services/notificador_email.py | Conditional Complexity | Extract Function | O método `update` concentra vários ramos de decisão por tipo de evento; se crescer, ficará mais difícil de manter. |
| models/notebook.py, models/projetor.py, models/cabo.py | Smell aparente — não refatorado | Não refatorar | As subclasses estão vazias após Strategy, mas representam tipos intencionais; removê-las desfaria a solução baseada em OCP/Strategy. |
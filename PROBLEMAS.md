# Problemas Identificados — Leitura Inicial do Código

WAGNER BARRAL DA CONCEICAO - BSI

---

## Minha leitura inicial

*(Espaço reservado para o estudante preencher)*

- 01- não conseguir cadastrar um livro aparece um erro de inexistencia, eu cadatrei mas não consigo registrar um emprestimo.

1-Registrar  2-Devolver  3-Atrasados  0-Sair
Opção: 1
ID equipamento: 23
Nome: wagner
Email: wagnerc
Dias: 1
Traceback (most recent call last):
  File "/home/repl846/emprestimos.py", line 122, in <module>
    main()
  File "/home/repl846/emprestimos.py", line 107, in main
    s.registrar(
  File "/home/repl846/emprestimos.py", line 17, in registrar
    if e["id"] == equipamento_id:
       ~^^^^^^
KeyError: 'id'


** Process exited - Return Code: 1 **


-02 -A classe Sistema usa diretamente equipamentos e emprestimos_registrados
Isso deixa o código difícil de controlar porque qualquer parte pode alterar esses dados sem passar pela classe.
for e in equipamentos
for e in emprestimos_registrados:

-03-Cálculo de multa repetido
devolver
listar_atrasados
if tipo == "notebook"
elif tipo == "projetor"
elif tipo == "cabo"
isso não escala. Se adicionar um novo tipo, tem que mexer no código novamente.

-04-Busca manual ineficiente em listas

O código usa for para encontrar equipamento empréstimo
Isso funciona, mas fica lento e pouco prático conforme os dados crescem.
Uma estrutura como dicionário (dict) seria mais adequada.

05-Mistura de lógica com impressão (prints)

print(f"[EMAIL] {usuario_email} — empréstimo até {data_devolucao}")

print(f"[EMAIL] {emprestimo['usuario_email']} — multa R${multa:.2f}")


---

## Revisão com vocabulário técnico

*(Este espaço será preenchido após a Aula 4, quando os termos técnicos corretos forem aprendidos)*

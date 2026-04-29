# Resenha Aula 3 — Modelos UML e Design de Componentes 
 
**Aluno:** 
<Wagner_barral_da_conceicao> 

**Data:** <29/04/2026> 
 
## Questão 1 — Modelos UML como ferramentas de modelagem 
 
### (a) Estrutura × comportamento 
<nomes de classes, atributos, métodos, relacionamentos (associações, herança, agregaçoes) e multiplicidades, representados em retângulos divididos. 
destaca, como objetos participantes, linhas de vida uma duração temporal, mensagens trocadas  ordem cronológica de interações e frames de controle .
como ele nos disse no livro ,um exemplo são nos caixa eletronicos na hora de sacar um dinheiro ou consultar algo , depositos etc ,nao esta com essas mesmas palavaras mas dar de enteder este ex.>

<para Valente Diagramas de classes são estruturais; de sequência, dinâmicos> 
 
### (b) Consequência prática 
<diagrama de classes ele contribui para decisões estruturais, como definir herança, associações, multiplicidades e operações de classes que são citadas no livro no cap. 4.3.2 heranças>

<diagrama de sequência apoia decisões dinâmicas, como ordem de mensagens, fluxos de controle e colaborações entre objetos como exemplo no livro cap 4 , em diagramas de sequencia que mostra a imagem de objeto a1 e b1.> 
 
### (c) Aplicação ao UC01 
<atendente , :Sistema/Interface , :EmprestimoService , :UsuarioRepository, :EquipamentoRepository, :Emprestimo.
 |(ator)|(fronteira)|(controle)|(entidades)|.> 

 1. Atendente → |Interface:  |iniciarEmprestimo | idUsuario
 2. Interface → |Service:    | validarUsuario   |
 3. Service   → |UsuarioRepo | buscar           | id
 4. Service   → |EquipRepo:  | buscarDisponivel | idEquip 
 5. Service   → |Emprestimo: | criar(data)      |
 6. Repo      → |persistir   |                  |
 7. Interface → |Atendente:  |confirma          |
  
## Questão 2 — Arquitetura, design e os princípios de decomposição 
 
### (a) Definições 
<Coesão é quando um modulo concentra suas funçoes em um unico proposito claro, como se todas as operaçoes relacionadas a "emprestimos" ficarem "juntas", facilitando entendimento e manutenção> 

<Acoplamento mede o grau de dependencia entre os modulos baixo acoplamento ocorre quando um modulo usa outro so por interfaces publicas simples>

<Ocultamento de informação é esconder detalhes internos de um modulo como se fosse umass estruturas de dados privadas, expondo apenas metodos publicos necessarios e  protegendo as informaçoes contra uso indevido>


 
### (b) Relações entre os princípios 
<ao esconder detalhes internos (ex : os dados privados)> 

<Ele se relaciona com coesao ao permitir agrupar dados e operaçoes relacionadas dentro de um modulo protegido, fortalecendo foco funcional sem expor excessos>

<Sim, creio que ha tensao aumentar coesao por concentrar responsabilidades pode elevar acoplamento se modulos compartilharem dados diretamente. >


 
### (c) Aplicação ao projeto v2.0 
<models | Usuario, Equipamento, Emprestimo	
Alta coesão em entidades de dominio com atributos encapsulados sem a lgica externa > 
 
<services | EmprestimoService, ValidacaoService	Coesao em orquestraçao de regras de negocio acoplamento baixo via dependencias em interfaces de repo >

<repositories |	UsuarioRepository, EquipamentoRepository, EmprestimoRepository	Coesão exclusiva em persistência  ocultamento de detalhes de storage, reduzindo acoplamento com services> 

<main.py |	App, CLIHandler	Coesão em inicialização e entrypoint acoplamento baixo como fachada injetando services>


## Questão 3 — Crítica fundamentada à documentação do sistema legado 
 
### (a) Pontos frágeis 
<toda logica concentrada em emprestimos.py unico, misturando registro, devoluçao, listagem e persistencia: Baixa coesao, pois um modulo assume multiplas responsabilidades nao relacionadas, dificultando manutençao>

<Variaveis globais equipamentos e emprestimos_registrados acessadas diretamente pela "classe" Sistema: Acoplamento por variavel global, criando dependencia forte e fragil entre logica e estado compartilhado, violando isolamento de modulos.>

{<Pontos frageis com Vocabulario Aceitavel (Cap. 7)

<dados em dicionários sem classes de domínio (DP02, DT07): Viola ocultamento de informaçao>

<Variaveis globais acessadas diretamente pela classe Sistema Seção 3, Acoplamento por variavel global.>}


### (b) Ponto forte 
<Registro explicito da dívida tecnica em tabela DT01–DT07 na seçao 5 Antecipa boa decisão ao mapear problemas como DT02 (variaveis globais) e DT07 (sem classes), promovendo transparencia e planejamento de refatoraçao> 

<a luz de Valente Cap. 7 isso alinha com principios de decomposiçao ao reconhecermos as violaçoes (baixa coesao, alto acoplamento), permitindo priorizar modularidade na v2.0 — divida "consciente" que irá facilitar na nossa manutençao.>
 
### (c) Síntese 
<sim, temos o intuito implementar postura planejada e incremental para v2.0, para priorizarmos refatoraçoes guiadas por principios como exemplos as camadas, evitando acumulo caotico ou extremo.> 
 
## Questão 4 — Tipos como contratos: dicionários × classes 
 
### (a) Prevenção de erros 
<Erro de digitaçao na chave (ex.: equipamento["disponivel"] → equipamento["dispnivel"]): 
Torna-se AttributeError em .disponivel, detectado em runtime (ou IDE com type hints), não KeyError silencioso>

<Valor ausente: __init__ obrigatorio força preenchimento, evitando KeyError ao acessar chave inexistente>

<tipo errado (ex.: string em campo bool): Type hints + @property ou Pydantic validam em tempo de criação/codigo, previne TypeError tardio>
 
### (b) Capacidade de evolução 
<uma classe permite adicionar calcular_multa() (Aula 5) sem afetar consumidores porque eles acessam via atributos publicos/.metodo() estavel — novo metodo opcional, respeitando contrato (interface implicita, Cap. 4/5 Valente>

<Dicionario nao permite: adicionar "calcular_multa" mas exige funçao externa que assume estrutura interna, mudanças no dict quebram clientes dependentes de chaves exatas.>

# exemplo
# Classe: evolui
class Emprestimo:
    def calcular_multa(self): ...

# Uso inalterado: e.calcular_multa() novo
e = Emprestimo(...)

# Dict: quebra
def calcular_multa_dict(emp): return emp['dias'] * 10  # Assume chave; muda → erro

as classes elas habilitam polimorfismo/encapsulamento para evoluçao segura do codigo.>
 
### (c) Comunicação do design 
<Valente argumenta que clareza de modelo é parte essencial do projeto porque nomes de tipos transmitem intençao, dominio e responsabilidades, guiando desenvolvedores e stakeholders — nao mero estilo, mas abstraçao que reduz ambiguidades.

comunica "entidade de dominio com atributos como id/serial/disponivel e métodos relacionados", sugerindo encapsulamento e uso OO, dict é generico, não revela semantica em si.

podemos ver essa evoluçao no Cap. 4 "Modelos": Seção 4.3 (Diagrama de Classes) e 4.5 (Sequência) — classes como abstrações que comunicam estrutura/intenção; nomes de tipos revelam domínio [https://engsoftmoderna.info/cap4.html].
Cap. 5 "Princípios de Projeto": Seções sobre Information Hiding (ocultamento) e contratos — clareza de modelo (nomes como Equipamento) é design essencial para legibilidade/equipe
>
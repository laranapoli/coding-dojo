# SOLID

- 5 princípios na programação orientada a objetos
- Torna o processo de desenvolvimento de software mais fácil de manter e voluir
- Primo do clean code
- Acrônimo criado por Michael Feathers
- Separam a responsabilidade, diminuindo o acoplamento
- Facilita refatoração e reaproveitamento do código

- S: Single responsability principle (SPR) = MAIS IMPORTANTE
    - Princípio da responsabilidade única
    - Uma classe deve ter e somente um motivo para mudar
    - Uma classe deve ser especializada em um único assunto e possuir apenas uma responsabilidade
    - Classe deve ter apenas uma tarefa/ação para executar
    - Não seguir gera:
        - Falta de coesão
        - Alto acoplamento (maior nível de dependências)
        - Dificuldade de implementar testes automatizados (difícil mockar essas classes)
        - Baixo reaproveitamento
    - Não se limite a classes. Possível aplicar a métodos e funções.

- O: Open-closed principle -> Design Pattern Strategy
    - Princípio aberto fechado
    - Objetos ou entidades devem estar:
        - ABERTOS para extensão
        - FECHADOS para modificação
    - Quando novos recursos precisam ser adicionados, devemos extender e não alterar o código fonte.
    - Ex. de má prática: Adicionar uma condicional para um novo comportamento.
    - Modelo mental: Extensão de um navegador (repeita contratos previamente estabelecidos)

- L: Liskov substitution principle
    - Princípio da substituição de Liskov
    - Uma classe derivada deve ser substituível por sua classe base
    - Ao usar uma classe para criar uma subclasse (herança), o objeto da subclasse deve conseguir substituir o objeto da classe principal.
    - Força a pensar no que a classe pai deveria forçar de comum
    - Objetivo: Um método fundamental não gerar exceção em uma implementação de mais baixo nível

- I: Interface segregation principle
    - Princípio da segregação da interface
    - Uma classe não deve ser forçada a implementar interfaces e métodos que não irão utilizar.
    - É melhor criar interfaces mais específicas do que uma mais genérica.
    - É um reflexo de respeitar os 3 primeiros princípios (especializados para interfaces)

- D: Dependency inversion principle (DIP)
    - Princípio da inversão de dependências
    - Devemos depender de abstrações e não de implementações
    - Módulos de alto nível não devem depender de módulos de baixo nível. Ambos devem depender da abstração.
    - Usa a injeção de dependência via método construtor
    - O efeito resultante de utilizar rigorosamente os princípios O e L pode ser generalizado em um princípio só: o DIP
# Arquitetura de Software

- Conjunto de princípios, normas e técnicas usadas para a construção de software
- É importante pensar nela desde o dia zero da construção
- Arquitetura vs. Desing de software:
    - Arquitetura foca em como os componentes de um sistema interagem entre si
    - Design se concentra na implementação dos componentes, focando em detalhes como implementação de um padrão de projeto, uso de algoritmos, estruturas de dados, etc.

## Model-view-controller (MVC)
- Padrão mais simples e amplamente utilizado
- Model: Contém dados da aplicação, onde as regras de negócio são aplicadas
- View: Parte que exibe os dados para o cliente e permite interação
- Controller: Intermedia model e view (ex.: valida dados, conecta regras de negócio com consultas no BD)

## Arquitetura em camadas
- Aplicação dividida em camadas lógicas, onde cama camada tem uma responsabilidade específica.
- Não existe um número máximo de camadas
- Separação de responsabilidades nas camadas deve clara e bem documentada
- Exemplo:
    - Controller: Gerencia requisições e respostas do fluxo
    - Service: Regras de negócio
    - Repository: Operações com bancos de dados
    - Entity: Representação da entidade (tabelas do BD dentro da aplicação)
- Desvantagem: A adição de camadas em um fluxo de requisição acarreta perda de desempenho
- Aplicação de alto desempenho requer outro padrão

## Arquitetura de microsserviços
- Cada funcionalidade da aplicação é um serviço independente, comunicando-se via APIs.
- Quando usar:
    - Para escalar diferentes partes do sistema independentemente.
    - Para isolar a inferência de ML em um serviço próprio.
- Desafios:
    - Maior complexidade operacional.
    - Necessidade de orquestração (kubernetes)

## Arquitetura monolítica
- Toda a aplicação roda em um único processo ou serviço
- Quando usar: 
    - Para sistemas menores, com menos requisitos de escalabilidade
    - Para desenvolvimento e manutenção mais simples
- Limitações:
    - Dificuldade de escalar componentes individuais
    - Maior dependência entre módulos


# Como arquitetar um software
1. Bloco de notas
2. Escrever e detalhar como o sistema deve funcionar (brain dump), evitando termos técnicos
3. Transformar o texto: limpar, organizar e explicar para o cliente
4. Abrir novo bloco de notas: Explicar tecnicamente como o sistema funcionará
    - Criar um bloco para cada funcionalidade
    - Discutir parte técnica com outro desenvolvedor
5. Arquitetar o banco de dados (diagramas)
6. Pensar em ferramentas e tecnologias

# Software Architecture x ML
- Requisitos operacionais para servir, monitorar, retreinar e fazer o re-deploy dos modelos.
- Categorias de desafios:
    - Desenvolvimento
    - Deployment
    - Organizacional
- Testar e avaliar a qualidade de componentes de ML é particularmente difícil
- Enquanto alguns desafios se aplicam igualmente em software com/sem componentes de ML, desafios específicos de ML também emergem.
# Plano de Estudos

## 1. Fundamentos de Python para Desenvolvimento
- Estrutura de dados avançadas: 
    - Listas
    - Dicionários
    - Conjuntos
    - Tuplas
    - Filas
    - Pilhas
    - Heaps 
    - Árvores
- Programação funcional: map, filter, reduce, list comprehensions
- Módulos e pacotes
- Tratamento de error e logging
- Gerenciamento de dependências: Poetry, virtualenv

### Prática:
Criar um CLI simples usando Typer para automatizar tarefas

### Recursos
- Livro: Fluent Python (Luciano Ramalho)
- Site: https://realpython.com/

## 2. Programação Orientada a Objetos (OOP) & Boas Práticas
- Classes, herança, encapsulamento, polimorfismo
- Design Patterns básicos: Factory, Singleton, Adapter
- Solid Principles: SRP, OCP, LSP, ISP, DIP

### Prática:
Criar um sistema de agendamento de tarefas simples: API para gerenciar tarefas usando FastAPI

### Recursos:
- Livro: Design Patterns in Python (Packt)

## 3. Arquitetura de Software & Microsserviços
- REST APIs e boas práticas
- Microsserviços vs. Monólitos
- Comunicação entre serviços: HTTP, gRPC, Message Brokers - RabbitMQ, Kafka
- Event-driven architecture

### Prática:
Criar 2 microsserviços pequenos que se comunicam via fila de mensagens (Exemplo: um serviço que processa pedidos e outro que gera faturas)

### Recursos:
- Livro: Building Microservices (Sam Newman)

## 4. CLoud & Deploy
- Conceitos básicos de Docker e Kubernetes
- Infra como código: Terraform, AWS CDK
- CI/CD: GitHub Actions, GitLab CI
- Logging & monitoring: Prometheus e Grafana

### Prática
Dockerizar um microsserviço e fazer deploy na AWS usando Terraform

## 5. Arquiteturas Avançadas & MLOps
- Arquitetura hexagonal e Clean Architecture
- Pipelines de ML: Airflow & Kubeflow
- Armazenamento e versionamento de modelos: MLflow

### Prática:
Criar um pipeline de ML completo com versionamento e automação

### Recursos:
- Curso: https://github.com/DataTalksClub/mlops-zoomcamp
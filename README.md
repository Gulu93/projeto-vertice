
# Projeto Vértice

MVP de gestão de agendamentos desenvolvido como projeto acadêmico de Engenharia de Software, com foco na organização da rotina de pequenos negócios.

## Sobre o projeto

O Projeto Vértice busca simplificar o controle de agendamentos, reduzindo conflitos de horários e facilitando a consulta aos atendimentos registrados.

A proposta foi inspirada em dificuldades observadas na organização de horários de um pequeno salão de beleza.

## Funcionalidades implementadas

- Cadastro de agendamentos com cliente, serviço, data e horário.
- Armazenamento persistente dos dados em banco SQLite.
- Consulta dos agendamentos cadastrados.
- Ordenação dos registros por data e horário.
- Validação de campos obrigatórios.
- Rejeição de datas passadas.
- Bloqueio de agendamentos na mesma data e horário.
- Testes automatizados com pytest.

## Tecnologias utilizadas

- Python
- Flask
- SQLite
- HTML5
- CSS3
- pytest
- Git e GitHub

## Estrutura do projeto

```text
projeto-vertice/
├── app.py
├── test_app.py
├── testes-manuais.md
├── README.md
├── .gitignore
├── static/
│   └── style.css
└── templates/
    ├── index.html
    ├── novo_agendamento.html
    └── agenda.html
```

## Como executar o projeto

### Pré-requisitos

- Python instalado
- Git (opcional, para clonar o repositório)

### 1. Clonar o repositório

```bash
git clone https://github.com/Gulu93/projeto-vertice.git
cd projeto-vertice
```

### 2. Criar um ambiente virtual

No Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Instalar as dependências

```powershell
python -m pip install Flask pytest
```

### 4. Iniciar a aplicação

```powershell
python app.py
```

Abra o navegador no endereço:

http://127.0.0.1:5000

## Executar os testes automatizados

Com o ambiente virtual ativado, execute:

```powershell
python -m pytest -v
```

Os testes atuais verificam a página inicial, o cadastro, a prevenção de duplicidades e a validação de dados inválidos.

## Status do projeto

O projeto está em desenvolvimento. A implementação do MVP, os testes automatizados iniciais e a publicação do repositório já foram realizados.

As próximas etapas incluem integração contínua, revisão por Pull Request e validação com usuários para identificar melhorias.

## Autor

Desenvolvido por [Gulu93](https://github.com/Gulu93) como parte de um projeto acadêmico de desenvolvimento de software.

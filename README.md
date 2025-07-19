# Workout API - FastAPI

Uma API RESTful para gerenciamento de academias, atletas, categorias e centros de treinamento.
Projeto desenvolvido durante o curso **Santander 2025 - Back-End com Python** oferecido pela **DIO**.

---

## 🚀 Tecnologias

Este projeto foi desenvolvido com as seguintes tecnologias:

-   [Python 3.11+](https://www.python.org/)
-   [FastAPI](https://fastapi.tiangolo.com/)
-   [Pydantic](https://docs.pydantic.dev/latest/)
-   [SQLAlchemy 2.0](https://www.sqlalchemy.org/)
-   [PostgreSQL](https://www.postgresql.org/)
-   [Alembic](https://alembic.sqlalchemy.org/en/latest/)
-   [Uvicorn](https://www.uvicorn.org/)

---

## 📂 Estrutura do Projeto

```

/workout_api
│
├── alembic/                  # Contém as migrações do banco de dados (Alembic)
├── workout_api/              # Módulo principal da aplicação (código-fonte)
│   │
│   ├── atleta/               # Módulo de domínio para Atletas
│   │   ├── controler.py
│   │   ├── models.py
│   │   └── schemas.py
│   │
│   ├── categorias/           # Módulo de domínio para Categorias
│   │   └── ...
│   │
│   ├── centro_treinamento/   # Módulo de domínio para Centros de Treinamento
│   │   └── ...
│   │
│   ├── configs/              # Configurações da aplicação
│   │   ├── database.py       # Configuração da conexão com o banco
│   │   └── settings.py       # Gerenciamento de variáveis de ambiente
│   │
│   ├── contrib/              # Módulos compartilhados
│   │   ├── dependencies.py
│   │   ├── models.py
│   │   └── schemas.py
│   │
│   ├── main.py               # Ponto de entrada da API (FastAPI app)
│   └── routers.py            # Agregador de todas as rotas da API
│
├── alembic.ini               # Arquivo de configuração do Alembic
├── docker-compose.yml        # Arquivo para orquestração com Docker
├── Makefile                  # (Opcional) Comandos para automação de tarefas
├── requirements.txt          # Lista de dependências do projeto
└── README.md                 # Este arquivo

````

---

## 📥 Instalação

```bash
# Clone este repositório
git clone https://github.com/ferreiraryan/DIO_workout_API

# Acesse o diretório
cd DIO_workout_API

# Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Aplique as migrações no banco de dados
make run-migrations

# Execute o projeto
make run
````

-----

## 🛠️ Como usar

Após iniciar a aplicação, você pode interagir com a API através da documentação interativa gerada automaticamente pelo FastAPI.

  - **Swagger UI:** [http://127.0.0.1:8000/docs](https://www.google.com/search?q=http://127.0.0.1:8000/docs)
  - **ReDoc:** [http://127.0.0.1:8000/redoc](https://www.google.com/search?q=http://127.0.0.1:8000/redoc)

A documentação permite visualizar todos os endpoints, seus parâmetros e testá-los diretamente pelo navegador.

-----

## 🤝 Contribuindo

Sinta-se à vontade para contribuir\! Basta seguir os passos abaixo:

1.  Faça um fork do projeto.
2.  Crie uma **branch** com a sua feature: `git checkout -b minha-feature`
3.  Faça commit das suas alterações: `git commit -m 'Adiciona nova feature'`
4.  Envie para o GitHub: `git push origin minha-feature`
5.  Abra um **Pull Request**

-----

## 📬 Contato

  - **Ryan Ferreira** - [ryanferreira4883@gmail.com](mailto:ryanferreira4883@gmail.com)
  - **GitHub** - [https://github.com/ferreiraryan](https://github.com/ferreiraryan)
  - **LinkedIn** - [https://www.linkedin.com/in/ferryan/](https://www.linkedin.com/in/ferryan/)


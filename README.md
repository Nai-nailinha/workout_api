# 💪 Workout API – FastAPI + SQLAlchemy + Pydantic

Bem-vinda(o) à **Workout API**: uma aplicação REST desenvolvida com foco em **organização de atletas**, utilizando tecnologias modernas como **FastAPI**, **SQLAlchemy**, **Pydantic** e **FastAPI Pagination**. Esse projeto foi construído passo a passo, com o objetivo de consolidar conhecimentos e criar uma base sólida para APIs profissionais.

---

## 🎯 Objetivo do Projeto

Desenvolver uma API robusta para gerenciamento de atletas, com foco em:

- Cadastro, listagem e filtragem de dados
- Validação de entradas (ex: CPF duplicado)
- Paginação para melhor escalabilidade
- Padrões profissionais de código (separação em rotas, schemas, models)
- Documentação interativa com Swagger UI

---

## 🛠️ Tecnologias Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://docs.pydantic.dev/)
- [FastAPI Pagination](https://fastapi-pagination.tiangolo.com/)
- SQLite (banco de dados simples para desenvolvimento local)
- Uvicorn (servidor ASGI para rodar a API)

---

## 🚀 Como rodar o projeto localmente

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/workout_api.git
cd workout_api

# Crie e ative o ambiente virtual
python -m venv venv
.\venv\Scripts\activate  # Windows

# Instale as dependências
pip install -r requirements.txt

# Execute o servidor
uvicorn app.main:app --reload
```

## Acesse a documentação em:

* http://127.0.0.1:8000/docs – Swagger UI 
* http://127.0.0.1:8000/redoc – Redoc

## 📦 Funcionalidades implementadas
✅ GET / – Mensagem de boas-vindas
✅ POST /atletas – Cadastro de atletas com validação de CPF duplicado
✅ GET /atletas – Listagem de atletas com:
✅Filtros por nome e CPF (query parameters)
✅Paginação com fastapi-pagination

## 📂 Organização do Projeto
```bash
workout_api/
│
├── app/
│   ├── __init__.py
│   ├── main.py              # Ponto de entrada da aplicação
│   ├── database.py          # Conexão e sessão com o banco de dados
│   ├── models/
│   │   └── atleta_model.py  # Modelo Atleta com SQLAlchemy
│   ├── schemas/
│   │   └── atleta_schema.py # Validações e serializações com Pydantic
│   └── routes/
│       └── atleta_route.py  # Rotas da API
│
├── requirements.txt
└── README.md
```

## 🧪 Testando a API
* Acesse o Swagger UI em http://127.0.0.1:8000/docs
* Criar um atleta (POST /atletas)

### Exemplo Json Atletas
```bash
{
  "nome": "Ana Silva",
  "cpf": "12345678901",
  "centro_treinamento": "Academia X",
  "categoria": "Elite"
}
```

## Filtrar atletas (GET /atletas)
* Todos: /atletas
* Por nome: /atletas?nome=ana
* Por CPF: /atletas?cpf=12345678901
* Paginado: /atletas?page=1&size=10

## 🧠 Lições e aprendizados
Durante o desenvolvimento, apliquei boas práticas como:

* Separação de responsabilidades (routers, schemas, models, database)
* Validação de dados sensíveis (CPF único)
* Tratamento de exceções
* Paginação eficiente para consultas
* Documentação automática com Swagger

## 👩‍💻 Feito com dedicação por:
Enaile Lopes

## 🪪 Licença
Distribuído sob a licença MIT.  
Veja o arquivo [LICENSE](LICENSE) para mais detalhes.


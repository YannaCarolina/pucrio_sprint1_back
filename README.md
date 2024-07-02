# pucrio_sprint1_back
Pasta do Backend da Sprint (Desenvolvimento Full Stack Básico)
Pet Creche - Backend
# Descrição
Pet Creche é um sistema que possibilita o cadastro de alunos (pets) que estão matriculados na creche. O sistema permite registrar informações detalhadas dos pets, como nome, idade, dono, raça, frequência, informações de saúde e observações.

# Tecnologias Utilizadas
Flask: Framework web utilizado como base para o desenvolvimento do backend.
Python: Linguagem de programação principal do projeto.
Swagger: Utilizado para a documentação da API.
VS Code: Ambiente de desenvolvimento integrado (IDE) utilizado para escrever o código.

# Instalação
1. Clone o repositório para sua máquina local:
git clone <URL_DO_REPOSITORIO>
2. Navegue até o diretório do projeto:
cd pet-creche-backend
3. Crie um ambiente virtual:
python -m venv venv
4. Ative o ambiente virtual:
No Windows:
venv\Scripts\activate
No Linux/MacOS:
source venv/bin/activate
5. Instale as dependências necessárias:
pip install -r requirements.txt

# Executando o Projeto
Certifique-se de que o ambiente virtual está ativado.
Execute a aplicação Flask:
flask run
A aplicação estará disponível em http://127.0.0.1:5000/.

# Documentação da API
A documentação da API está disponível via Swagger. Para acessá-la, inicie a aplicação e navegue até http://127.0.0.1:5000/.

# Endpoints Principais
GET /pets: Retorna a lista de todos os pets cadastrados.
POST /pets: Adiciona um novo pet.
GET /pets/<id>: Retorna os detalhes de um pet específico.
PUT /pets/<id>: Atualiza as informações de um pet específico.
DELETE /pets/<id>: Remove um pet específico do cadastro.

# Estrutura do Projeto
BACK/
│
├── api_flask/
│   ├── app.db
│   ├── app.py
│   ├── init_db.py
│   └── requirements.txt
│
├── venv/
│
└── README.md

# Contribuição
1. Faça um fork do projeto.
2. Crie uma branch para sua feature (git checkout -b feature/nova-feature).
3. Commit suas mudanças (git commit -am 'Adiciona nova feature').
4. Faça um push para a branch (git push origin feature/nova-feature).
5. Crie um Pull Request.

## Preparar o Ambiente Virtual (Venv)
O ambiente virtual isola as bibliotecas do seu projeto do resto do seu computador.

Abra o terminal na pasta raiz do seu projeto Django.

**Crie o ambiente:**
python -m venv venv

**Ative o ambiente:**

No Windows:
.\venv\Scripts\activate

## Instalar as Dependências
Agora que o "ambiente" está isolado, vamos instalar tudo o que o Django precisa.

**Verifique se existe um arquivo chamado requirements.txt. Se houver, basta rodar:**
pip install -r requirements.txt

**Preparar Mudanças (Sempre que alterar o models.py):**
python manage.py makemigrations

**Aplicar Mudanças:**
python manage.py migrate

## Ligar o Servidor:

**No vs code (BackEnd Django)**

Ative o ambiente virtual (venv):

No Windows (PowerShell/CMD):

Bash venv\Scripts\activate

Baixe as dependências do Python (caso tenha um arquivo requirements.txt):

Bash pip install -r requirements.txt

Crie/atualize as tabelas no banco de dados (Migrations):

Bash python manage.py makemigrations python manage.py migrate

nicie o servidor do Django:

Bash python manage.py runserver

(Deixe esse terminal quieto rodando. Seu back-end agora está ativo em http://127.0.0.1:8000/).

---

**No Terminal (Front-end gerado pelo AI Studio):**

Entre na pasta do front-end (onde está o arquivo package.json)

instale as dependências na primeira vez e inicie o servidor do Vite:

Bash npm install npm run dev

(Ele vai rodar geralmente na porta 5173, abrindo a interface visual em http://localhost:5173/).

---


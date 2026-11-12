
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


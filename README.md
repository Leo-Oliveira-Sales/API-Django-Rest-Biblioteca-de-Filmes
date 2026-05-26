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

python manage.py runserver

---

*Abra o Projeto do Front End no VACode e Rode:*

npm install

npm run dev

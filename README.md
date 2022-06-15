Plataforma open-source para gestão de requisitos de software!


Versão atual: 1.0


Requisitos para Instalação do AppCycle
* Python 3
* Django 3.x
* Instalar o conteúdo de Requirements.txt
* Criar superuser para acesso ao <url_servidor>/admin

A documentação de uso encontra-se na aba "wiki" deste repositório e caso encontre um bug, você pode abrir um issue.

Para mais informações, acesse www.appcycle.com.br


Faça o fork deste projeto e ajude a colaborar com o AppCycle! Sua ideia será bem-vinda!


Instruções para instalação

1. Clonar o repositório em sua máquina local
2. Instalar o arquivo requirements.txt

pip install -r requirements.txt

3. Criar a base de dados

python manage.py migrate

4. Executar o servidor de desenvolvimento

python manage.py runserver

5. O projeto estará disponível em 127.0.0.1:8000 

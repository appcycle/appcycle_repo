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


Instalar Django

Short instruction for installing Django by Linux:

1) To install a pipenv

   $ pip3 install pipenv

2) To create the folder for project

   $ cd ~/Desktop
   $ mkdir django
   $ cd django

3) To install a Django

  $ pipenv install django==2.1

4) To activated virtual envirenment

  $ pipenv shell

5) To create a new project

   (django-JmZ1NTQw) $ django-admin startproject test_project .

6) To run and check server

   (django-JmZ1NTQw) $ python manage.py runserver
   
   
   http://127.0.0.1:8000
   
   CTRL+C: $ exit


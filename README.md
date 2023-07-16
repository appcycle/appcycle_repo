Seja bem-vindo(a) ao AppCycle, uma plataforma open-source para gestão de requisitos de software! Desenvolvida idealmente para micro e pequenas empresas Brasileiras. 
<br>
Versão atual: 2023.2
<br>
Site: www.appcycle.com.br
<br>
Documentação do usuário: https://github.com/appcycle/appcycle_repo/wiki
<br>

<h2> Requisitos para Instalação do AppCycle </h2>
* Python 3 <br>
* Django 4.2.3 <br>
* Instalar o conteúdo de Requirements.txt

A documentação de uso encontra-se na aba "wiki" deste repositório. Caso encontre um bug, você pode abrir uma issue.

<br>

<h2> Instruções para instalação </h2>

1. Clonar o repositório em sua máquina local
2. Instalar o arquivo requirements.txt
<code> pip install -r requirements.txt </code>
3. Criar a base de dados
<code>python manage.py migrate </code> 
5. Executar o servidor de desenvolvimento
<code> python manage.py runserver </code> 
6. O projeto estará disponível em  <code> 127.0.0.1:8000 </code>
7. Configurar superusuário para o acesso em <url_servidor>/admin
<code> python manage.py  createsuperuser </code>

<h3> Organização das pastas do projeto </h3>
Para o correto funcionamento, as pastas do projeto devem estar arranjadas da seguinte maneira:
 <code>
|.qualidade  
  |.. apps   
  |.. qualidade  
      |... init.py 
      |... asgi.py 
      |... settings.py 
      |... urls.py 
      |... wsgi.py 
  |.. static 
  |.. templates 
  |.. venv  </code>

<h2> Avalie sua experiência com o AppCycle </h2>
Com a preocupação de manter um produto que atenda as necessidades das empresas brasileiras, lançamos uma pesquisa de avaliação de experiência, no qual você pode avaliar, anonimamente, a plataforma AppCycle. O questionário tem apenas 1 questão. Segue o link para avaliação: https://forms.gle/ocJ1sPBaEFXpbR6Y8

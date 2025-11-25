# UC3 — Django Static Blog/Empresa

Projeto didático de Blog no DJANGO: Admin, ORM, Models, Partials.

## Requisitos
- Python 3.11+
- venv
- pip

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
# acesse http://127.0.0.1:8000/admin/
```

## Conteúdo do projeto
- `blog/models.py` com nomes descritivos: `titulo`, `Descricao`, `esta_ativo`.
- Admin otimizado: filtros, busca, edição em lista, ações de publicar/despublicar.
- Templates com **partials**: `_navbar`, `_footer`, `_alert`, `_posts`.
- View de lista com filtro por termo e categoria e paginação.
- Configuração de `TIME_ZONE='America/Sao_Paulo'` e `LANGUAGE_CODE='pt-br'`.

## Fluxo recomendado
1. Crie categorias no admin.
2. Cadastre POST com `esta_ativo=False` para revisão.
3. Publique via ação do admin.



## Deploy
Pré-requisitos
Um projeto Django funcional.
Um repositório Git (preferencialmente GitHub, GitLab ou Bitbucket) com o código do seu projeto.
Uma conta na Vercel, conectada ao seu provedor Git.
Conhecimento básico da linha de comando (CLI) ou preferência por deploy via dashboard da Vercel. 

### Passo a Passo
1. Preparar o Projeto Django
Instalar WhiteNoise: Para servir arquivos estáticos em produção, instale e configure o WhiteNoise.

```bash
    pip install whitenoise
```

No seu arquivo settings.py, adicione 'whitenoise.middleware.WhiteNoiseMiddleware' ao MIDDLEWARE, preferencialmente logo após o SecurityMiddleware.
Configurar settings.py:

Defina DEBUG = False (use variáveis de ambiente para gerenciar isso entre desenvolvimento e produção).
Adicione o domínio da Vercel (.vercel.app) e seu domínio personalizado (se houver) ao ALLOWED_HOSTS. 
Exemplo: ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app', 'seusite.com'].

Configure STATIC_ROOT para o local onde os arquivos estáticos serão coletados, por exemplo: 
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build').
Gerar requirements.txt: Crie um arquivo requirements.txt com todas as dependências do seu projeto.

```bash
    pip freeze > requirements.txt
```
 
2. Adicionar Arquivos de Configuração da Vercel
Crie os arquivos vercel.json e build_files.sh na raiz do seu projeto. O build_files.sh conterá comandos para instalar dependências, executar migrações e coletar arquivos estáticos durante o processo de build. O vercel.json configurará o processo de build e as rotas na Vercel. 
Você pode encontrar o conteúdo completo sugerido para ambos os arquivos nas referências. Lembre-se de ajustar a versão do Python no build_files.sh e substituir {nome_do_projeto} no vercel.json e build_files.sh pelo nome do diretório principal do seu projeto. 
3. Configurar o WSGI
No arquivo wsgi.py do seu projeto, é necessário expor a aplicação WSGI com a variável app, além da variável application, para garantir a compatibilidade com o builder da Vercel. Você pode encontrar um exemplo completo do arquivo wsgi.py nas referências. 
4. Fazer Deploy
Envie suas alterações para o repositório Git.
No painel da Vercel, importe seu projeto Django.
Configure as variáveis de ambiente necessárias (como SECRET_KEY, DATABASE_URL, DEBUG=False) nas configurações do projeto na Vercel.
Clique em "Deploy". A Vercel usará o vercel.json para o processo. 
Após o deploy, a Vercel fornecerá o URL para acessar sua aplicação. 

# Nba-Store 

A NBA Store é um projeto de e-commerce que oferece uma variedade de produtos relacionados à NBA, como camisetas, regatas, tênis e jaquetas. Este projeto foi desenvolvido usando o framework Django e utiliza um banco de dados hospedado na AWS (Amazon Web Services).

![image](https://github.com/Lucas-Benediht/Nba-Store/assets/110697669/a1aa4595-d764-44b2-9114-bcd09f80a00e)

## Funcionalidades

- Verificar os produtos e adicionar os mesmos ao carrinho de compras
- Páginas de detalhes dos produtos.
- Carrinho de compras para adicionar e remover itens.
- Páginas separadas por categorias (Ex: Jaquetas, Regatas, etc.)
- Área de administração para gerenciar produtos e pedidos.


## Pré-requisitos
Antes de começar a usar a NBA Store, você deve ter os seguintes pré-requisitos instalados:

-Python 3.x
-Django
-Uma conta na AWS (para hospedagem do banco de dados)
## Deploy

Para fazer o deploy desse projeto rode

```bash
  npm run deploy
```


## Screenshots
- Pagina inicial:
```
https://github.com/Lucas-Benediht/Nba-Store/assets/110697669/de5eb045-fb80-42f2-abd2-53cd9396dea9
```

-Categorias:
```
https://github.com/Lucas-Benediht/Nba-Store/assets/110697669/34e91d5d-13b9-4c97-80fe-6d341e841edf
```
- Descrição dos produtos:
```
https://github.com/Lucas-Benediht/Nba-Store/assets/110697669/f50b7229-697a-4f88-a72b-7c45325155d7
```

- Carrinho de compras:
```
https://github.com/Lucas-Benediht/Nba-Store/assets/110697669/c618aac2-5339-4b98-b56d-2455696559d5
```

## Instalação

1. Clone este repositório:

```bash
git clone https://github.com/SeuNome/NBA-Store.git
```

2. Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente para a conexão com o banco de dados AWS. Você pode definir as variáveis em um arquivo .env na raiz do projeto ou como variáveis de ambiente do sistema.
```bash
AWS_ACCESS_KEY_ID=SEU_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY=SEU_SECRET_ACCESS_KEY
AWS_STORAGE_BUCKET_NAME=SUA_BUCKET_NAME
AWS_S3_CUSTOM_DOMAIN=SEU_CUSTOM_DOMAIN
AWS_DEFAULT_ACL=public-read
AWS_LOCATION=static/upload/produtos
AWS_QUERYSTRING_AUTH=False
```

4.Execute as migrações do banco de dados:
```bash
python manage.py migrate
```

5.Crie um superusuário para acessar a área de administração:
```bash
python manage.py createsuperuser
```

6.Inicie o servidor de desenvolvimento:
```bash
python manage.py runserver
```
## Uso
A NBA Store está agora em execução em http://localhost:8000/. Você pode começar a cadastrar produtos no painel de administração e navegar pelo site.



## Contribuição

Contribuições são bem-vindas! Se você deseja melhorar ou expandir este projeto, fique à vontade para criar um fork e enviar um pull request.

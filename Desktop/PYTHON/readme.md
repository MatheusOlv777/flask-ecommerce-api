API de E-commerce com Flask
Este é um projeto de API de backend para um e-commerce simples, desenvolvido com o framework Flask em Python. A API gerencia a autenticação de usuários, um catálogo de produtos e um carrinho de compras básico. É um projeto ideal para estudo e prática de desenvolvimento web com Python.

Funcionalidades
Autenticação de Usuário: Rotas para login e logout de usuários.

Produtos: Rotas para listar, adicionar, atualizar e deletar produtos. As operações de modificação requerem autenticação.

Carrinho de Compras: Funcionalidades para adicionar e remover produtos do carrinho do usuário autenticado.

Checkout: Rota para finalizar a compra e limpar o carrinho.

Tecnologias Utilizadas
Flask: O micro-framework web.

Flask-SQLAlchemy: Extensão para o banco de dados.

Flask-Cors: Para lidar com requisições de diferentes origens.

Flask-Login: Para gerenciar as sessões de usuário.

SQLite: Banco de dados simples para desenvolvimento.

Instalação
Siga os passos abaixo para configurar e executar o projeto em seu ambiente local.

Clone o repositório.

Crie um ambiente virtual e ative-o.

Instale as dependências usando o requirements.txt:

pip install -r requirements.txt

Como Usar a API
Para testar a API, você pode usar ferramentas como Insomnia ou Postman.

Rotas
Autenticação
POST /login: Autentica um usuário.

POST /logout: Faz logout do usuário. Requer autenticação.

Produtos
GET /api/products: Lista todos os produtos.

POST /api/products/add: Adiciona um novo produto. Requer autenticação.

GET /api/products/<int:product_id>: Obtém os detalhes de um produto específico.

PUT /api/products/update/<int:product_id>: Atualiza um produto. Requer autenticação.

DELETE /api/products/delete/<int:product_id>: Deleta um produto. Requer autenticação.

Carrinho de Compras
POST /api/cart/add/<int:product_id>: Adiciona um produto ao carrinho. Requer autenticação.

DELETE /api/cart/remove/<int:product_id>: Remove um produto do carrinho. Requer autenticação.

GET /api/cart/: Visualiza o conteúdo do carrinho. Requer autenticação.

POST /api/car/checkout: Finaliza a compra e limpa o carrinho. Requer autenticação.
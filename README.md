ERP de Controle de Estoque simples — README

📘 Sobre o Projeto

Este é um sistema web simples desenvolvido em Python (Flask) que simula o módulo de estoque de um sistema ERP.

O projeto permite cadastrar, excluir, listar produtos e visualizar relatórios com gráficos, utilizando SQLite como banco de dados e Matplotlib para gerar visualizações.

O código foi desenvolvido com técnicas simples, adequadas para iniciantes e ideal para fins acadêmicos.

🧾 Funcionalidades

✅ Cadastro de Produtos
•Nome

•Categoria

•Preço

•Quantidade inicial

Salvo automaticamente no banco SQLite

✅ Exclusão de Produtos

•Remoção pelo ID diretamente na listagem

✅ Listagem Completa

•Exibição de todos os produtos cadastrados

Tabela contendo:

•ID

•Nome

•Categoria

•Preço

•Quantidade

•Produtos com quantidade menor que 5 aparecem destacados em vermelho

✅ Relatórios Gráficos

•Gráfico de barras mostrando quantidade em estoque por produto

•Gerado automaticamente com Matplotlib

•Salvo no diretório /static/grafico.png

✅ Interface Web Simples e Moderna

•Construída com HTML + CSS

•Layout limpo e responsivo

🛠️ Tecnologias Utilizadas

•Python 3

•Flask

•SQLite3

•Matplotlib

•HTML5

•CSS3

📁 Estrutura do Projeto
meu_estoque/
│ app.py
│ estoque.db
│
├── static/
│     style.css
│     grafico.png
│
└── templates/
      index.html
      cadastrar.html
      listar.html
      relatorios.html

▶️ Como Executar Localmente
1. Instale as dependências
   
•pip install flask matplotlib

3. Execute o servidor
   
•python app.py

5. Acesse no navegador
   
•http://127.0.0.1:5000/


O arquivo estoque.db será criado automaticamente na primeira execução do sistema.

🧪 Funcionalidades Implementadas (Resumo Técnico)

•CRUD parcial (Create, Read, Delete)

•Banco de dados criado automaticamente

•Templates usando Jinja2

•Rotas simples e organizadas

•Geração de gráficos em tempo de execução

•Sistema 100% funcional e de fácil manutenção


👥 Colaboradores

Nome	RGM

Gabriel Eustáquio	42957613

Yan Marcos	042733588

Pedro Vitor	42921601

Guilherme Ferreira	42923921

📌 Observações

•Este projeto foi desenvolvido com foco didático, utilizando técnicas simples e diretas para facilitar o entendimento e a implementação por iniciantes.

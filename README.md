# API para o curso da Pós Tech da FIAP

API desenvolvida em Flask com o objetivo de fazer um we scraping do site http://vitibrasil.cnpuv.embrapa.br/
- **Web Scraping**: Extrai dados de páginas web (título, cabeçalhos, parágrafos) usando BeautifulSoup.

## 📁 Estrutura do Projeto

```bash
intro_api/
├── app/
│   ├── __init__.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth_routes.py
│   │   └── scrape_routes.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── GetEmbrapaData.py
│   └── config.py
├── requirements.txt
├── README.md
├── Procfile
└── run.py

```

- **`app/`**: Diretório principal do aplicativo.
  - **`routes/`**: Contém as rotas organizadas por funcionalidades.
  - **`services/`**: Serviços para lógica de negócios, como scraping.
  - **`config.py`**: Configurações da aplicação Flask.
- **`Procfile`**: Arquivo de configuração para rodar a aplicação no Render
- **`run.py`**: Ponto de entrada para iniciar o aplicativo.
- **`requirements.txt`**: Lista de dependências do projeto.
- **`README.md`**: Documentação do projeto.


### Deploy<br>
A aplicação disponível em: https://fivemlet.onrender.com <br>
Não é necessário fazer login, apenas clique em "entrar".
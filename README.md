# API para o curso da Pós Tech da FIAP

Este projeto é uma API desenvolvida em Flask, com o objetivo de realizar web scraping do site [Embrapa VitiBrasil](http://vitibrasil.cnpuv.embrapa.br/).

- **Web Scraping**: Extrai dados de páginas web usando BeautifulSoup.

- **Documentação**: Acesse a documentação interativa via Swagger para visualizar os endpoints em https://fivemlet-postech.onrender.com (Não é necessário fazer login, apenas clique em "entrar").


## 📁 Estrutura do Projeto

```bash
5mlet_postech/
├── app/
│   ├── __init__.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth_routes.py
│   │   └── scrape_routess.py
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

## 🛠️ Como Executar o Projeto Localmente

### 1. Clone o Repositório

```bash
git clone https://github.com/PatySutto/5mlet_postech.git
cd 5mlet_postech
```

### 2. Crie um Ambiente Virtual

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3. Instale as Dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o Aplicativo

```bash
python run.py
```

O aplicativo estará disponível em `http://localhost:5000`.


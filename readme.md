# Web Scraping com Python, Scrapy e BigQuery

## Objetivo
Este projeto consiste em construir um Crowler para obter dados do site de noticias www.theguardian.com/au.

## Requisitos
Executar o comando abaixo para instalar a dependências
```
pip install -r requirements.txt
```

## Configurações GCP
- Criar uma conta de serviço e gerar a chave JSON
- Conceder papel de _Proprietário de dados_ e _Usuário de Jobs_ do BigQuery
- Definir variável de ambiente _GOOGLE_APPLICATION_CREDENTIALS_ com o caminho para arquivo JSON que contém a chave da conta de serviço

  ```
    export GOOGLE_APPLICATION_CREDENTIALS="{KEY_PATH}"
  ```
- Criar a tabela para carregar os dados obtidos
  ```
  create or replace table PROJECT.DATASET.TABLE (
    headline string,
    url string,
    author string,
    tags string,
    posted_at string,
    text string
  )
  ```
- Atribuir o nome da tabela criada à variável TABLE_ID no construtor da classe TheGuardianPipeline no modulo webscraping/pipelines.py 
  
### Executando o Crawler
Para executar o crawler, rodar o comando abaixo:

  ```
  scrapy crawl theguardian
  ```
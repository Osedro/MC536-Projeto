# Linguagem Utilizada e Programas Utilizados

## Linguagem
A linguagem utilizada para gerar as consultas foi o  **SQL**(Structured Query Language), portanto é interessante que você esteja familiarizado com esse tipo de comando: 
~~~sql 
SELECT * FROM tabela
WHERE condicao
GROUP BY elemento;
~~~

## Como Executar

1. Caso queira simplesmente executar o projeto, você deve clicar nesse botão: 
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Osedro/MC536-Projeto/HEAD) - Clicando no botão você será redirecionado a uma página e a partir dela conseguirá executar os notebooks que estão em `final/notebooks`.

2. Caso queira fazer no seu repositório:
~~~
├── binder  <- pasta do binder
│
├── final   <- projeto finalizado
│
├── stage02    <- etapa 02 do trabalho
│
├── stage03    <- etapa 03 do trabalho
│
└── stage03    <- etapa 04 do trabalho
~~~
Crie um repositório e copie a pasta `binder` para seu repositório. 
Copie a url de ser repositório, depois vá até https://mybinder.org/ e cole a url de seu repositório em `GitHub repository name or URL`, você pode então clicar em launch para lançar o binder.
Caso queira executar várias vezes, facilitará se você gerar o seguinte botão:  [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Osedro/MC536-Projeto/HEAD) e colar no readme do seu repositório, _(o botão pode ser gerado no próprio site do binder)._


Seguindo os passos acima você será capaz de reproduzir os comandos SQL e analisar os resultados que obtivemos.

## Jupyter Notebook

Um [Jupyter Notebook](https://jupyter.org/index.html) é um ambiente computacional web para a internet rica para criação de documentos para a plataforma Jupyter. O termo "notebook" pode, dependendo do contexto, fazer referência a entidades distintas como **Jupyter (aplicativo Web)**, **Jupyter Python (servidor Web)** ou ao formato de documento para a plataforma. Um documento **Jupyter Notebook é estruturado formato JSON**, contendo uma lista ordenada de células de entrada / saída que podem conter código, **texto (usando Markdown)**, matemática, gráficos e texto enriquecido, geralmente terminando com a extensão ".ipynb". [Wikipedia](https://pt.wikipedia.org/wiki/Projeto_Jupyter)

No caso do nosso projeto utilizamos o Jupyter Notebook para gerar as querys/consultas **SQL**.


[![Binder](https://img.shields.io/badge/Binder%20Launch:-Jupyter-blue.svg?colorA=&logo=data:image/png;base64,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)](https://mybinder.org/v2/gh/Osedro/MC536-Projeto/HEAD)

## CSV - Comma-Separated-Values
Utilizamos para a realização das consultas, arquivos que tem a extesão `.csv`, esses arquivos podem ser interpretados por programas de planilhas, mas também são de grande uso para realizar consultas em dados, por terem uma estrutura simples, de texto separados por virgulas ou ponto e vírgula. 
Os CSV's utilizados nesse projeto estão no diretório `https://github.com/Osedro/MC536-Projeto/tree/main/final/data/csv`[CSV's](https://github.com/Osedro/MC536-Projeto/tree/main/final/data/csv)


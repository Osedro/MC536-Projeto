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


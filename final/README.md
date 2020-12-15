# Apresentação Final

## Slides da Apresentação da Etapa

> Coloque um link para o arquivo dos slides da apresentação que estão na pasta `slides`.

## Modelo Conceitual Atualizado

> Coloque aqui a imagem do modelo conceitual atualizado em ER ou UML, como o exemplo a seguir:
> <img src="https://github.com/Osedro/MC536-Projeto/blob/main/final/images/Modelo_Conceitual.png" width="75%" />

## Modelos Lógicos Atualizados

> Coloque aqui os dois modelos lógicos dos bancos de dados relacionados aos modelos conceituais. O modelo lógico da etapa anterior pode ser copiado ou apresentado revisado. Para o modelo relacional, sugere-se o formato a seguir. Para outros modelos lógicos o formato é livre, pode ser adotado aqueles apresentados em sala.

> <img src="https://github.com/Osedro/MC536-Projeto/blob/main/final/images/Modelo_Logico.png" width="75%" />

> UF está sendo usado como chave 


## Programa de extração e conversão de dados atualizado

> Coloque um link para o arquivo do notebook que executa a extração e conversão de dados. Ele estará dentro da pasta `notebook`. Se por alguma razão o código não for executável no Jupyter, coloque na pasta `src`. Se a extração e conversão envolverem queries executadas atraves de uma interface de um SGBD não executável no Jupyter, como o Cypher, apresente na forma de markdown.

## Conjunto de queries de dois modelos

> Acrescente um link para o arquivo do notebook que executa o segundo conjunto de queries. Ele estará dentro da pasta `notebook`. Se por alguma razão o código não for executável no Jupyter, coloque na pasta `src`. Se as queries forem executadas atraves de uma interface de um SGBD não executável no Jupyter, como o Cypher, apresente na forma de markdown.
> O link para queries da etapa 3 também deve aparecer aqui e as queries poderão ser revisadas.

## Bases de Dados
> Elencar as bases de dados utilizadas no projeto. Trata-se de uma atualização daquelas apresentadas na Etapa 3.

título da base | link | breve descrição
----- | ----- | -----
Brasil.io  | [Brasil.io/covid19](https://brasil.io/covid19/) | Compilação de boletins epidemiológicos diários de casos e óbitos confirmados por município.
Dados.gov.br  | [Dados.gov.br](https://dados.gov.br/dataset/distribuicao-de-respiradores1) | Dados relacionados a gestão de recursos públicos, como gastos com equipamentos e insumos para saúde. Há dados voltados especificamente para covid.



## Arquivos de Dados
> Elencar os arquivos usados no projeto que estão disponíveis no Github do projeto (manter os da Etapa 3 e acrescentar os da Etapa 4).

nome do arquivo | link | breve descrição
----- | ----- | -----
casos_por_estado.csv | [Casos Covid-19 por Estado](https://github.com/Osedro/MC536-Projeto/blob/main/final/data/csv/casos_por_estado.csv) | CSV com casos de Covid-19 por estado e região do Brasil: <br> Ex: _Norte, Nordeste, Sul, Sudeste, etc._
covid19_por_municipio.csv | [Casos Covid-19 por Municipio](https://github.com/Osedro/MC536-Projeto/blob/main/final/data/csv/covid19_por_municipio.csv) | CSV com casos de Covid-19 por município.
distribuicao_respiradores.csv | [Distribuicao de respiradores](https://github.com/Osedro/MC536-Projeto/blob/main/final/data/csv/distribuicao_respiradores.csv) | CSV com dados referente a: <br> _fornecedor, quantidade de respiradores e valores  por estado._


> Os arquivos devem ser colocados na pasta `data`, em subpasta conforme seu papel (externo, interim, processado, raw). A diferença entre externo e raw é que o raw é em formato não adaptado para uso. A pasta `raw` é opcional, pois pode ser substituída pelo link para a base original da seção anterior.
> Coloque arquivos relacionais (usualmente CSV), XML ou JSON que não estejam disponíveis online e sejam acessados pelo notebook.

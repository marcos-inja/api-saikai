# API [**Saikai**](https://saikaiscan.com.br/)
Api não oficial do site saikaiscan.

Essa aplicação vai fazer a coleta das informações de uma novel, dependendo do que for passado na url da **API**.
> Olhe o arquivo crawler.ipynb, para entender de maneira mais simples como é feito o scraping no site Saikai.
## Motivação:
Antes de tudo, quero apenas usar esse projeto para programar melhor, e aprender a construir apis usando o flask. Como gosto muito de ler novels, resolvi usar o site da saikai, para pegar os dados de suas novels.
## Como usar:
- Instale as dependencias:
    ```sh
    pip install requirements.txt
    ```
- Entre na pasta `src` e rode com:
    ```sh
    cd src; python3 main.py
    ```
- Acesse a url:
> O nome passado por parametro, deve ser o mesmo que esta na url do site da saikai. Veja [*aqui*](https://saikaiscan.com.br/)

```sh
your_localhost:5000/info_novel/name_of_novel
```

- Exemplo
    ```sh
    http://127.0.0.1:5000/info_novel/king-of-gods-kog
    ```
## Formato dos dados:
```json


{
  "image": "https://s3-alpha.saikai.com.br/series/a-guerra-dos-nove-mundos-gnm.jpg",
  "name_of_novel": "A Guerra dos Nove Mundos",
  "initals": "GNM",
  "genre_of_novel": "Fantasia",
  "chapters_of_novel": 232,
  "status_of_active": "Em Andamento",
  "rated_novel": {
    "average": 5.0,
    "people_ratings": 3
  },
  "original_language": "Português",
  "author": "Maurício Argôlo",
  "group": {
    "reviewer": "solidsnake",
    "QC": "bru"
  },
  "synopsis": "O Mundo Celestial, antes deslumbrante e pacífico foi repentinamente atacado. A paz que perdurou milhões de anos chegou ao fim sendo substituída por morte e destruição. Como último ato de desespero, os príncipes do Mundo Celestial sacrificaram suas vidas para que uma centelha de esperança fosse criada.Em um mundo, a milhões de quilômetros de distância de onde a tragédia aconteceu, a noite estava deslumbrante e bela na qual a lua brilhava magnanimamente no céu estrelado, uma criança acabou de nascer, uma criança mortal que recebeu a última luz de esperança produzida pelos Deuses.Assim começa a história de Sagwa, filha de um Clã Mortal, que vivia uma vida simples e pacífica até que os horrores de uma poderosa guerra alcançaram o seu vilarejo, consequentemente, Sagwa teve seu primeiro contato com os terrores do mundo. Agora, Sagwa precisa encontrar dentro de si a força necessária para superar as dificuldades que lhe foram impostas e pavimentar sua caminhada marcial para então descobrir o quão alto ela pode chegar."
}

```
## Objetivos:
- Criar modelos de exemplos usando o Jupyter Notebook.
- Criar formas de pegar os dados de cada novel.
- Passar as informações para um formato padrão.
- Usar o o micro-framework Flask para criar a API baseada em rest.
- Buscar novas formas de fazer o Web scraping.
- Analizar mais páginas, para ver as diferenças entre elas.
- Fazer uma documentação
## Para fazer:
- [X] Coletar sinopse.
- [X] Coletar Status (andamento/concluido).
- [X] Numero de capitulos.
- [X] Tradutor.
- [X] Avaliação.

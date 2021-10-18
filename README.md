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

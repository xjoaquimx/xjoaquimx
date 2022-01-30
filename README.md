## Projeto backend python watt.io passo a passo de como executar

# requerimentos de pacotes para executar
python>=3.9.7
git

# clonando repositório e instalando modulos
```bash
mkdir filme
cd filme
git clone https://github.com/xjoaquimx/xjoaquimx.git
pip install -r requeriments.txt
```

# iniciando api
```bash
python -m uvicorn main:app --reload
```

# testando api
url local de teste da api: http://127.0.0.1:8000/docs

clique em POST > try it out(para enviar um post)

insere o request body e clique em executar
{
  "id": 0,
  "nome_filme": "string",
  "genero": "string"
}

em Server response > Code > verifique se o status é igual a 201

insere o request body e clique em executar novamente
{
  "id": 1,
  "nome_filme": "O Lobo de Wall Street",
  "genero": "Drama"
}

em Server response > Code > verifique se o status é igual a 201 novamente

clique em GET /filmes > try it out > execute (para receber os dados do banco de dados)

em Server response > Code > verifique se o status é igual a 200 > verifique os dados recebidos em Response Body

clique em GET /filmes {filmes_id} > try it out > em filme_id digite o id do filme > execute (para receber o dado do banco de dados)


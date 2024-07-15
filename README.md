
# Pilar

Este teste visa identificar a lógica aplicada no desenvolvimento das soluções e o tipo de arquitetura utilizada.

## Tecnologia utilizada

- [Fastapi](https://fastapi.tiangolo.com/)
- [Docker](https://www.docker.com/)


## Variáveis de Ambiente

Para rodar esse projeto, você vai precisar renomar o arquivo .env.example para .env.

```
cp .env.example .env
```


## Instalação

Para realizar a instalação, execute os seguintes comandos:


```bash
  make build
```

## Health check

Para verificar se o serviço está em execução, acesse a seguinte URL:
- http://localhost:8000/api/


## Documentação

Para explorar a documentação da API, acesse a seguinte URL:
- http://localhost:8000/docs


## Postman

Dentro do projeto existe um arquivo chamado *Pilar.postman_collection.json* importe para o postman, dessa forma terá todos os endpoints disponíveis.

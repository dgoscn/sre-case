## Overview
O projeto visa coletar as últimas postagens do Twitter e gerar alguns
insights, como os usuários mais seguidos e a quantidade de hashtags por hashtag e
língua.

## Requirements 

* Docker: 19.03.12
* docker-compose: 1.26

## Deployment

Antes de dar início a implantação, é preciso definir as credenciais da API do Twitter e MongoDB.
Token Bearer para autenticação pelo Twitter. O projeto possui um arquivo .env na pasta raiz, é necessário preencher antes de continuar:

```
BEARER_TOKEN=#TWITTER API BEARER
ROOT_USERNAME=
ROOT_PASSWORD=
ROOT_DATABASE=
MONGO_IP=
```


**Primeiro Passo: `./start.sh`**

Para executar o processo, seria necessário a execução do comando acima, o processo pode levar um tempo para o build acontecer.


O `docker-compose` rodando no background criaria os seguintes serviços:

* **`filebeat`** 
* **`localhost:8000`** - API
* **`localhost:27017`** - MongoDB
* **`localhost:9200`** - Elasticsearch
* **`localhost:5601/app/kibana`** - Kibana
* **`localhost:9090`** - Prometheus
* **`localhost:3000`** - Grafana


## API

Os seguintes endpoints possíveis de serem checados:

* **`/`** raiz passando as hashtags como parametros
* **`/most-followed-users`** 
* **`/total-hashtag-lang`** 
* **`/total-per-hour`** 
* **`/metrics`** 

## Queries

`postman` ou curl com `elasticsearch`

## Infrastructure

![infrastructure](https://github.com/dgoscn/sre-case/blob/main/infra_design/infra_design.png)


## Logs
**Kibana**

## Dashboard 
**Grafana**

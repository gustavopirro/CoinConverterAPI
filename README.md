# Coin Converter API

API Criada para conversão de valores entre diferentes moedas.

## Endpoints
### Conversor de moedas
``
http://127.0.0.1:8000/v1/coinconverter
``

``
Porta padrão é 8000, mas pode ser alterada na inicialização do servidor (Descrito abaixo).
``
#### Parametros
| Nome   |      Tipo      |  Descrição | Obrigatorio
|:----------:|:-------------:|:----------:|:------:|
| from |  String | Moeda que será convertida  | Sim
| to | String |   Moeda de conversão  | Sim
| amount | Number | Quantia da moeda informada no parametro from | Sim


## Guia de uso

### Clonar o repositório:
``
git clone https://github.com/gustavopirro/coin-converter.git
``

### Baixar e instalar dependências:
``
pip install -r requirements.txt
``

### Com o terminal aberto na pasta raiz do projeto deve se executar o comando para fazer as migrações:
``
python manage.py migrate
``

### Rodando o servidor de forma local, com o terminal na pasta raiz do projeto executar o comando:
``
python manage.py runserver
``
### Caso a porta 8000 esteja ocupada é necessário informar outra porta a ser utilizada:
``
python manage.py runserver 127.0.0.1:porta_desejada
``

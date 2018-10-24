# Eventex

Sistema de Eventos encomendado pela Morena.

[![Build Status](https://travis-ci.org/rqclima/eventex.svg?branch=master)](https://travis-ci.org/rqclima/eventex)
[![Coverage Status](https://coveralls.io/repos/github/rqclima/eventex/badge.svg?branch=master)](https://coveralls.io/github/rqclima/eventex?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/86ff47ac18b3415b8f9ea0b026f9dff2)](https://www.codacy.com/app/rqclima/eventex?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=rqclima/eventex&amp;utm_campaign=Badge_Grade)

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.6
3. Ative o virtualenv
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes.

```console
git clone git@github.com:rqclima/eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?

1. Crie uma instância no heroku.
2. Envie as configurações para o heroku.
3. Defina uma SECRET_KEY segura para instância.
4. Defina DEBUG=False
5. Configure o serviço de e-mail.
6. Envie o código para o heroku.

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configura o email
git push heroku master --force 
```

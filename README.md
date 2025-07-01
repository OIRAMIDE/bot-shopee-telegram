
# Bot da Shopee para Telegram 🤖🛍️

Um bot feito em Python que busca automaticamente promoções da Shopee e publica em um grupo do Telegram usando link de afiliado.

## Funcionalidades
- Scraping de ofertas direto da Shopee (sem usar API externa)
- Postagem automática no Telegram
- Suporte a links com ID de afiliado
- Roda no Windows com Chrome/Chromedriver

## Como rodar

1. Instale as dependências:
```bash
pip install python-telegram-bot selenium beautifulsoup4
```

2. Crie um arquivo `.env` com:
```
TELEGRAM_BOT_TOKEN=seu_token
TELEGRAM_GROUP_ID=seu_id
SHOPEE_AFFILIATE_ID=seu_id_afiliado
```

3. Coloque o `chromedriver` na mesma pasta ou configure no PATH

4. Execute:
```bash
python bot_shopee.py
```

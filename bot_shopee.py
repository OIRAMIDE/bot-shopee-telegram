
import os
import asyncio
from telegram import Bot
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

BOT_TOKEN    = os.getenv("TELEGRAM_BOT_TOKEN")
GROUP_ID     = int(os.getenv("TELEGRAM_GROUP_ID"))
AFFILIATE_ID = os.getenv("SHOPEE_AFFILIATE_ID")

async def send_offer(bot: Bot, title: str, url: str, price: str):
    message = f"*{title}*\n💰 {price}\n🔗 {url}?adid={AFFILIATE_ID}"
    await bot.send_message(chat_id=GROUP_ID, text=message, parse_mode="Markdown")

def fetch_offers(limit=10):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get("https://shopee.com.br/flash_sale")
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    offers = []
    for card in soup.select("div.shopeep-product-item-selector")[:limit]:
        title = card.select_one("div.title").get_text(strip=True)
        price = card.select_one("div.price").get_text(strip=True)
        link  = card.select_one("a")["href"]
        offers.append((title, "https://shopee.com.br" + link, price))
    return offers

async def main():
    bot = Bot(BOT_TOKEN)
    offers = fetch_offers()
    for title, url, price in offers:
        await send_offer(bot, title, url, price)

if __name__ == "__main__":
    asyncio.run(main())

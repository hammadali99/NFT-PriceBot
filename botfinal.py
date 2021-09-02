import coinmarketcapapi
from pycoingecko import CoinGeckoAPI
import re
import telebot

API_KEY_BOT = "APIKEY"
API_KEY_CMC = "APIKEY"

cg = CoinGeckoAPI()
bot = telebot.TeleBot(API_KEY_BOT, parse_mode=None)

KodaRaw = cg.get_price(ids='koda-finance', vs_currencies='usd')

price = re.findall(r'(?<=: )+([0-9].[0-9]*)', str(KodaRaw))

cgprice = '$ ' + price[0]
print(cgprice)

cmc = coinmarketcapapi.CoinMarketCapAPI(API_KEY_CMC)

data_id_map = cmc.cryptocurrency_map()
data = cmc.cryptocurrency_info(symbol='KODA')
data_quote = cmc.cryptocurrency_quotes_latest(symbol='KODA')

pprice = re.findall(r"price':(.[0-9].........)", str(data_quote))

cmcprice = '$' + pprice[0]
print(cmcprice)


@bot.message_handler(regexp='CG:CHECK KODA')
def KODA(message):
  bot.reply_to(message, cgprice)

@bot.message_handler(regexp='CMC:CHECK KODA')
def KODA(message):
  bot.reply_to(message, cmcprice)

bot.polling(none_stop=True)

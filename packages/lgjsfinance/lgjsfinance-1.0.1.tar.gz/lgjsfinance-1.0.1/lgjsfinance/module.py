import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime
import binance

class DataRecover():
    def __init__(self, entreprise):
        self.corp = entreprise

    def get_day_data(self, date_string, interval="1m"):
        return yf.download(self.corp, start=datetime.strptime(date_string, "%Y-%m-%d").replace(hour=0, minute=0, second=0, microsecond=1), end=datetime.strptime(date_string, "%Y-%m-%d").replace(hour=23, minute=59, second=59, microsecond=59), interval=interval, progress=False)

    def get_data(self):
        start_of_day = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        return yf.download(self.corp, start=start_of_day, progress=False)
    
    def show_graph(self, data):
        plt.figure(figsize=(10, 6))
        plt.plot(data.index, data['Close'], label='Prix de clôture')
        plt.title('Graphique de clôture')
        plt.xlabel('Date')
        plt.ylabel('Prix de clôture (en $)')
        plt.legend()
        plt.grid(True)
        plt.show()

    def get_close_prices_hourly(self, interval="1m"):
        historique_prix = yf.download(self.corp, start=datetime.now().replace(hour=0, minute=0, second=0, microsecond=0), interval=interval, progress=False)
        return historique_prix

class Provider:
    def __init__(self, id):
        self.id = id

    def get_data(self, currency, interval, limit, start, end):

        if self.id == 1:
            client = binance.Client()
            data = client.get_klines(symbol=currency, interval=interval, limit=limit)

            result = []
            for entry in data:
                result.append({
                    "OpenTime": entry[0],
                    "Open": entry[1],
                    "High": entry[2],
                    "Low": entry[3],
                    "Close": entry[4],
                    "Volume": entry[5],
                    "CloseTime": entry[6],
                    "QuoteAssetVolume": entry[7],
                    "TradesNumber": entry[8],
                    "TakerBuyBaseAssetVolume": entry[9],
                    "TakerBuyQuoteAssetVolume": entry[10],
                    "CanBeIgnored": entry[11]
                })
            return result

        elif self.id == 2:
            return yf.download(currency, interval=interval, start=start, end=end, progress=False).tail(limit).to_dict('records')

class Financer:

    def __init__(self, provider):
        self.provider = Provider(provider)

    def get_data(self, currency, interval="1m", limit=60, start=datetime.now().replace(hour=0, minute=0, second=0, microsecond=0), end=None):
        return self.provider.get_data(currency, interval, limit, start, end)


    
class Settings:
    PROVIDER_BINANCE = 1
    PROVIDER_YAHOO = 2

    INTERVAL_1MIN = "1m"

    INTERVAL_1HOUR = "1h"
    INTERVAL_4HOUR = "4h"

    INTERVAL_1DAY = "1d"
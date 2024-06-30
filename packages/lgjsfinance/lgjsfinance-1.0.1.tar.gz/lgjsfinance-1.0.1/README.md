```
# Import des packages
from lgjsfinance import Financer, Settings

finance = Financer(Settings.PROVIDER_BINANCE)
print(finance.get_data("EURUSDT", Settings.INTERVAL_1MIN))
```
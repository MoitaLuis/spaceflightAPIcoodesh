import schedule
import time
from mongo import refresh_articles

# Horário de atualização dos artigos.
schedule.every().day.at("09:00").do(refresh_articles)

# Atualizar todos os artigos.
while True:
    schedule.run_pending()
    time.sleep(1)
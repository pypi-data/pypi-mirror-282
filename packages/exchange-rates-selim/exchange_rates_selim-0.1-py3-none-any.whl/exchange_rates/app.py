import click

from exchange_rates.httpClient import ExchangeClient


@click.command()
@click.option("--currency", default="Dolar", help="Öğrenmek istediğiniz exchange adını giriniz")
def cli(currency):
    client = ExchangeClient()
    try:
        print(client.scrape_exchange_rate(currency))
    except Exception as e:
        print(e)

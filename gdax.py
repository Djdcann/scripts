import GDAX
from datetime import datetime

publicClient = GDAX.PublicClient()

ids = ["BTC-USD", "ETH-USD", "ETH-BTC"]
currency = {}


# iso string to datetime
def getTime():

    return datetime.strptime(publicClient.getTime()['iso'], "%Y-%m-%dT%H:%M:%S.%fZ")


if __name__ == '__main__':

    for i in ids:
        currency[i] = publicClient.getProductTicker(product=i)
        currency[i]['price'] = float(currency[i]['price'])
        currency[i]['ask'] = float(currency[i]['ask'])
        currency[i]['bid'] = float(currency[i]['bid'])
        print "%s\t%.2f\t%f\t%f" % (i, currency[i]['price'], currency[i]['ask'], currency[i]['bid'])

    eth_btc = float(publicClient.getProductTicker(product="ETH-BTC")["ask"])
    eth_usd = float(publicClient.getProductTicker(product="ETH-USD")["ask"])
    btc_usd = float(publicClient.getProductTicker(product="BTC-USD")["bid"])

    calc = (eth_usd/btc_usd)
    print "calc\t%f" % calc
    print "ratio\t%f" % (eth_btc/(eth_usd/btc_usd))
    dt = getTime()
    print dt
    print publicClient.getProductTicker()



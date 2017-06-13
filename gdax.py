import GDAX
publicClient = GDAX.PublicClient()
eth_btc = float(publicClient.getProductTicker(product="ETH-BTC")["ask"])
eth_usd = float(publicClient.getProductTicker(product="ETH-USD")["ask"])
btc_usd = float(publicClient.getProductTicker(product="BTC-USD")["bid"])
print eth_usd
print btc_usd
print eth_btc, eth_usd/btc_usd
print eth_btc/(eth_usd/btc_usd)
print publicClient.getProductTicker(product="ETH-BTC")
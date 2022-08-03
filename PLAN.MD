```buildoutcfg
Ping : need to do this
```
```buildoutcfg
SIMPLE 

/simple/price : done
des :Get the current price of any cryptocurrencies in any other supported currencies that you need.


/simple/token_price/{id}: not done
des :Get current price of tokens (using contract addresses) for a given platform in any other currency that you need.


/simple/supported_vs_currencies : done
des :Get list of supported_vs_currencies.

```
```buildoutcfg
COIN 

/coins/list : done
des :List all supported coins id, name and symbol (no pagination required)

/coins/markets: not done
des :List all supported coins price, market cap, volume, and market related data

/coins/{id}: not done
des :Get current data (name, price, market, ... including exchange tickers) for a coin

/coins/{id}/tickers: not done
des :Get coin tickers (paginated to 100 items)

/coins/{id}/history: not done
des :Get historical data (name, price, market, stats) at a given date for a coin

/coins/{id}/market_chart: not done
des :Get historical market data include price, market cap, and 24h volume (granularity auto)

/coins/{id}/market_chart/range: not done
des :Get historical market data include price, market cap, and 24h volume within a range of timestamp (granularity auto)

/coins/{id}/status_updates: not done
des :Get status updates for a given coin

/coins/{id}/ohlc: not done
des :Get coin's OHLC

```
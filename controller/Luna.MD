**Assets Request**
``````

{
    "config": { //API request as recognized and processed by LunarCRUSH
        "data": "assets", //API endpoint request
        "end": 1577836799, //A unix timestamp (in second2) to set the earliest date/time for data to be retreived
        "indicators": "timeSeries", //A comma-separated list of keys/metrics to be included for each asset
        "interval": "day", //Time series time buckets in hour or day intervals
        "start": 1575158400, //A unix timestamp (in seconds to set the latest date/time for data to be retreived
        "symbol": "'BTC'", //A comma-separted list of symbols to get data for
        "time_series_indicators": "social_volume", //A comma-separated list of keys/metrics to be included for each assets time series array
        "data_points": 24 //Number of data points in the time series array
    },
    "usage": {
        "day": 1,
        "month": 1
    },
    "data": [{ //API endpoint request
        "id": 1, //LunarCRUSH internal ID for the asset
        "name": "Bitcoin", //The full name of the asset
        "symbol": "BTC", //The symbol for the asset
        "timeSeries": [{ //An array of metrics for hourly or daily data points
            "social_volume": 67752, //Number of social posts
            "time": 1575158400 //A unix timestamp (in seconds)
        },{ //An array of metrics for hourly or daily data points
            "social_volume": 75390, //Number of social posts
            "time": 1575244800 //A unix timestamp (in seconds)
        },{ //An array of metrics for hourly or daily data points
            "social_volume": 77012, //Number of social posts
            "time": 1575331200 //A unix timestamp (in seconds)
        },{ //An array of metrics for hourly or daily data points
            "social_volume": 88750, //Number of social posts
            "time": 1575417600 //A unix timestamp (in seconds)
        },{ //An array of metrics for hourly or daily data points
            "social_volume": 79901, //Number of social posts
            "time": 1575504000 //A unix timestamp (in seconds)
        },{ //An array of metrics for hourly or daily data points
            "social_volume": 71657, //Number of social posts
            "time": 1575590400 //A unix timestamp (in seconds)
        },{ //An array of metrics for hourly or daily data points
            "social_volume": 37069, //Number of social posts
            "time": 1575676800 //A unix timestamp (in seconds)
        },{ //An array of metrics for hourly or daily data points
            "social_volume": 68213, //Number of social posts
            "time": 1575763200 //A unix timestamp (in seconds)
        },{ //An array of metrics for hourly or daily data points
            "social_volume": 79290, //Number of social posts
            "time": 1575849600 //A unix timestamp (in seconds)
        },{ //An array of metrics for hourly or daily data points
            "social_volume": 77833, //Number of social posts
            "time": 1575936000 //A unix timestamp (in seconds)
        },{ //An array of metrics for hourly or daily data points
            "social_volume": 76056, //Number of social posts
            "time": 1576022400 //A unix timestamp (in seconds)
        },{ //An array of metrics for hourly or daily data points
            "social_volume": 77292, //Number of social posts
            "time": 1576108800 //A unix timestamp (in seconds)
        },{ //An array of metrics for hourly or daily data points
            "social_volume": 71721, //Number of social posts
            "time": 1576195200 //A unix timestamp (in seconds)
        },{ //An array of metrics for hourly or daily data points
            "social_volume": 67985, //Number of social posts
            "time": 1576281600 //A unix timestamp (in seconds)
        },{ //An array of metrics for hourly or daily data points
            "social_volume": 66644, //Number of social posts
            "time": 1576368000 //A unix timestamp (in seconds)
        },{ //An array of metrics for hourly or daily data points
            "social_volume": 86209, //Number of social posts
            "time": 1576454400 //A unix timestamp (in seconds)
        },{ //An array of metrics for hourly or daily data points
            "social_volume": 90830, //Number of social posts
            "time": 1576540800 //A unix timestamp (in seconds)
        },{ //An array of metrics for hourly or daily data points
            "social_volume": 95013, //Number of social posts
            "time": 1576627200 //A unix timestamp (in seconds)
        },{ //An array of metrics for hourly or daily data points
            "social_volume": 91053, //Number of social posts
            "time": 1576713600 //A unix timestamp (in seconds)
        },{ //An array of metrics for hourly or daily data points
            "social_volume": 78344, //Number of social posts
            "time": 1576800000 //A unix timestamp (in seconds)
        },{ //An array of metrics for hourly or daily data points
            "social_volume": 66029, //Number of social posts
            "time": 1576886400 //A unix timestamp (in seconds)
        },{ //An array of metrics for hourly or daily data points
            "social_volume": 72892, //Number of social posts
            "time": 1576972800 //A unix timestamp (in seconds)
        },{ //An array of metrics for hourly or daily data points
            "social_volume": 83171, //Number of social posts
            "time": 1577059200 //A unix timestamp (in seconds)
        },{ //An array of metrics for hourly or daily data points
            "social_volume": 70785, //Number of social posts
            "time": 1577145600 //A unix timestamp (in seconds)
        } ]
    } ]
}
``````

**MARKET PAIRS**
```
{
    "config": { //API request as recognized and processed by LunarCRUSH
        "data": "market-pairs", //API endpoint request
        "limit": 1,
        "symbol": "'LTC'", //A comma-separted list of symbols to get data for
    },
    "usage": {
        "day": 1,
        "month": 1
    },
    "data": [{ //API endpoint request
        "name": "Litecoin", //The full name of the asset
        "symbol": "LTC", //The symbol for the asset
        "total_rows": 961,
        "marketPairs": [{ //list of trading pairs over all exchanges known to LunarCRUSH
            "id": 81610, //LunarCRUSH internal ID for the asset
            "asset_id": 4, //The LunarCRUSH id for an asset/coin
            "exchange_id": 57,
            "unique_key": "4:bitforex:LTC:USD",
            "1d": "{"volume":"240234448.12","volume_base":"1322679.74","volume_change":"43636470.77","volume_base_change":"245113.74","price_change":"-3.95000000","price_quote_change":"-3.95000000"}",
            "1d_volume": 240234448.12,
            "30d": "{"volume":"534067491.31","volume_base":"2936741.31","volume_change":"434229903.28","volume_base_change":"2283394.52","price_change":"-3.30000000","price_quote_change":"-3.30000000"}",
            "30d_volume": 534067491.31,
            "exchange": "bitforex", //Name of the exchange
            "from_symbol": "LTC",
            "to_symbol": "USD",
            "price": 180.35, //Current price in USD
            "type": "derivative", //Type of social post / source
            "last_updated": 1632034535,
            "name": "Bitforex", //The full name of the asset
            "exchange_lunar_id": "bitforex",
            "pairing_url": "https://www.bitforex.com/en/spot/{{symbol1}}_{{symbol2}}",
            "market_sort": "LTC_USD",
            "logo": "https://dkhpfm5hits1w.cloudfront.net/exchanges/bitforex.png"
        } ]
    } ]
}
```

**MARKET**
```
{
    "config": { //API request as recognized and processed by LunarCRUSH
        "data": "market", //API endpoint request
        "limit": 10,
        "sort": "acr",
        "total_rows": 2970,
        "btc": {
            "id": 1, //LunarCRUSH internal ID for the asset
            "s": "BTC", //symbol
            "n": "Bitco
 in", //name
            "p": 48251.87226113, //Price
            "p_btc": 1, //Price (BTC)
            "v": 34991424540.25, //Volume (USD)
            "vt": 0.00985323997023885, //Volatility
            "pc": -1.04, //Percent Change (24 Hours)
            "pch": -0.17, //Percent Change (1 Hour)
            "mc": 908108680032, //Market Cap
            "gs": 61.5, //Galaxy Score™
            "ss": 956584063, //Social Score/Engagement
            "as": 3.5124999999999997, //Average Sentiment - using a scoring system from 1 to 5 with 1 being very bearish and 5 being very bullish we provide the average over all coins
            "bl": 170123, //Bullish Sentiment - number of posts that we classified as bullish
            "br": 40823, //Bearish Sentiment - number of posts that we classified as bearish
            "sp": 160099, //Tweet Spam
            "na": 128, //News Articles
            "md": 2,
            "t": 246371, //Number of tweets (24 hours)
            "r": 3702, //Reddit Activity (24 hours)
            "yt": 7,
            "sv": 261465, //Social Volume
            "u": 38556, //URL Shares
            "c": 10326, //Social Contributors (24 Hours)
            "sd": 19.515986240058325, //Social Dominance
            "d": 36.18191453811557, //Market Dominance
            "cr": 3,
            "acr": 141, //ALTRank
            "tc": 1523264400,
            "timeSeries": [{ //An array of metrics for hourly or daily data points
                "p": 47955.62603844, //Price
                "ss": 28837771, //Social Score/Engagement
                "na": 1, //News Articles
                "ts": 5323, //Tweet Spam
                "sv": 8517, //Social Volume
                "u": 1296 //URL Shares
            },{ //An array of metrics for hourly or daily data points
                "p": 48125.72735385, //Price
                "ss": 26785608, //Social Score/Engagement
                "na": 4, //News Articles
                "ts": 6206, //Tweet Spam
                "sv": 9132, //Social Volume
                "u": 1377 //URL Shares
            },{ //An array of metrics for hourly or daily data points
                "p": 48273.90003013, //Price
                "ss": 30129959, //Social Score/Engagement
                "na": 3, //News Articles
                "ts": 7831, //Tweet Spam
                "sv": 9751, //Social Volume
                "u": 1373 //URL Shares
            },{ //An array of metrics for hourly or daily data points
                "p": 48300.87075919, //Price
                "ss": 29312443, //Social Score/Engagement
                "na": 2, //News Articles
                "ts": 7734, //Tweet Spam
                "sv": 9330, //Social Volume
                "u": 1485 //URL Shares
            },{ //An array of metrics for hourly or daily data points
                "p": 48380.50409609, //Price
                "ss": 22697473, //Social Score/Engagement
                "na": 9, //News Articles
                "ts": 9196, //Tweet Spam
                "sv": 9942, //Social Volume
                "u": 2759 //URL Shares
            },{ //An array of metrics for hourly or daily data points
                "p": 48231.22748127, //Price
                "ss": 34816458, //Social Score/Engagement
                "na": 4, //News Articles
                "ts": 7147, //Tweet Spam
                "sv": 8715, //Social Volume
                "u": 1728 //URL Shares
            } ]
        }
    },
    "usage": {
        "day": 1,
        "month": 1
    },
    "data": [{ //API endpoint request
        "id": 19, //LunarCRUSH internal ID for the asset
        "s": "ATOM", //symbol
        "n": "Cosmos", //name
        "p": 39.17577635, //Price
        "p_btc": 0.000811901684104362, //Price (BTC)
        "v": 3972697538.09, //Volume (USD)
        "vt": 0.07303934060762839, //Volatility
        "pc": 8.82, //Percent Change (24 Hours)
        "pch": 0.07, //Percent Change (1 Hour)
        "mc": 10945436790, //Market Cap
        "gs": 65, //Galaxy Score™
        "ss": 20652837, //Social Score/Engagement
        "as": 3.7500000000000004, //Average Sentiment - using a scoring system from 1 to 5 with 1 being very bearish and 5 being very bullish we provide the average over all coins
        "bl": 4504, //Bullish Sentiment - number of posts that we classified as bullish
        "br": 402, //Bearish Sentiment - number of posts that we classified as bearish
        "sp": 1233, //Tweet Spam
        "md": 1,
        "t": 5464, //Number of tweets (24 hours)
        "r": 168, //Reddit Activity (24 hours)
        "sv": 5796, //Social Volume
        "u": 281, //URL Shares
        "c": 208, //Social Contributors (24 Hours)
        "sd": 0.42305455660642105, //Social Dominance
        "d": 0.4361007302607996, //Market Dominance
        "cr": 3.4,
        "acr": 1, //ALTRank
        "tc": 1523426400,
        "timeSeries": [{ //An array of metrics for hourly or daily data points
            "p": 39.23866546, //Price
            "ss": 530887, //Social Score/Engagement
            "ts": 24, //Tweet Spam
            "sv": 97, //Social Volume
            "u": 2 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 39.36055677, //Price
            "ss": 108139, //Social Score/Engagement
            "ts": 36, //Tweet Spam
            "sv": 151, //Social Volume
            "u": 10 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 39.3217286, //Price
            "ss": 194823, //Social Score/Engagement
            "ts": 30, //Tweet Spam
            "sv": 117, //Social Volume
            "u": 12 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 39.49067226, //Price
            "ss": 351171, //Social Score/Engagement
            "ts": 69, //Tweet Spam
            "sv": 126, //Social Volume
            "u": 12 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 38.87700644, //Price
            "ss": 158557, //Social Score/Engagement
            "ts": 84, //Tweet Spam
            "sv": 151, //Social Volume
            "u": 15 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 39.21548338, //Price
            "ss": 609396, //Social Score/Engagement
            "ts": 119, //Tweet Spam
            "sv": 145, //Social Volume
            "u": 25 //URL Shares
        } ]
    },{ //API endpoint request
        "id": 2753, //LunarCRUSH internal ID for the asset
        "s": "OM", //symbol
        "n": "MANTRA DAO", //name
        "p": 0.34965291, //Price
        "p_btc": 0.000007246411250277, //Price (BTC)
        "v": 336249727.58, //Volume (USD)
        "vt": 0.16735038946051625, //Volatility
        "pc": 46.36, //Percent Change (24 Hours)
        "pch": 11.75, //Percent Change (1 Hour)
        "mc": 124876668, //Market Cap
        "gs": 65.5, //Galaxy Score™
        "ss": 1471105, //Social Score/Engagement
        "as": 3.3791666666666664, //Average Sentiment - using a scoring system from 1 to 5 with 1 being very bearish and 5 being very bullish we provide the average over all coins
        "bl": 1051, //Bullish Sentiment - number of posts that we classified as bullish
        "br": 484, //Bearish Sentiment - number of posts that we classified as bearish
        "sp": 1105, //Tweet Spam
        "t": 1818, //Number of tweets (24 hours)
        "sv": 1824, //Social Volume
        "u": 58, //URL Shares
        "c": 85, //Social Contributors (24 Hours)
        "sd": 0.13417100401862048, //Social Dominance
        "d": 0.004975480389881767, //Market Dominance
        "cr": 3,
        "acr": 2, //ALTRank
        "tc": 1593187200,
        "timeSeries": [{ //An array of metrics for hourly or daily data points
            "p": 0.29490325, //Price
            "ss": 11469, //Social Score/Engagement
            "ts": 35, //Tweet Spam
            "sv": 55, //Social Volume
            "u": 1 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 0.29452123, //Price
            "ss": 2273, //Social Score/Engagement
            "ts": 26, //Tweet Spam
            "sv": 36, //Social Volume
            "u": 4 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 0.31481775, //Price
            "ss": 8882, //Social Score/Engagement
            "ts": 38, //Tweet Spam
            "sv": 36, //Social Volume
            "u": 4 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 0.3005122, //Price
            "ss": 21140, //Social Score/Engagement
            "ts": 30, //Tweet Spam
            "sv": 45, //Social Volume
            "u": 4 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 0.31273143, //Price
            "ss": 10265, //Social Score/Engagement
            "ts": 23, //Tweet Spam
            "sv": 55, //Social Volume
            "u": 1 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 0.36010049, //Price
            "ss": 6513, //Social Score/Engagement
            "ts": 35, //Tweet Spam
            "sv": 34, //Social Volume
            "u": 1 //URL Shares
        } ],
        "df": 1,
        "dot": 1
    },{ //API endpoint request
        "id": 3267, //LunarCRUSH internal ID for the asset
        "s": "GALA", //symbol
        "n": "Gala Token", //name
        "p": 0.12128422, //Price
        "p_btc": 0.000002513565055955, //Price (BTC)
        "v": 1099000700.39, //Volume (USD)
        "vt": 0.11484163798329446, //Volatility
        "pc": 16.02, //Percent Change (24 Hours)
        "pch": -0.42, //Percent Change (1 Hour)
        "mc": 914785780, //Market Cap
        "gs": 63.5, //Galaxy Score™
        "ss": 1653858, //Social Score/Engagement
        "as": 3.3416666666666663, //Average Sentiment - using a scoring system from 1 to 5 with 1 being very bearish and 5 being very bullish we provide the average over all coins
        "bl": 745, //Bullish Sentiment - number of posts that we classified as bullish
        "br": 347, //Bearish Sentiment - number of posts that we classified as bearish
        "sp": 286, //Tweet Spam
        "t": 1439, //Number of tweets (24 hours)
        "r": 6, //Reddit Activity (24 hours)
        "sv": 1476, //Social Volume
        "u": 159, //URL Shares
        "c": 39, //Social Contributors (24 Hours)
        "sd": 0.11153190738367265, //Social Dominance
        "d": 0.03644795126446436, //Market Dominance
        "cr": 3,
        "acr": 3, //ALTRank
        "tc": 1613419200,
        "timeSeries": [{ //An array of metrics for hourly or daily data points
            "p": 0.12178237, //Price
            "ss": 363717, //Social Score/Engagement
            "ts": 3, //Tweet Spam
            "sv": 89, //Social Volume
            "u": 9 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 0.11841839, //Price
            "ss": 16405, //Social Score/Engagement
            "ts": 5, //Tweet Spam
            "sv": 67, //Social Volume
            "u": 4 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 0.12479217, //Price
            "ss": 1402, //Social Score/Engagement
            "ts": 6, //Tweet Spam
            "sv": 51, //Social Volume
            "u": 7 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 0.12735396, //Price
            "ss": 13862, //Social Score/Engagement
            "ts": 13, //Tweet Spam
            "sv": 31, //Social Volume
            "u": 2 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 0.12232307, //Price
            "ss": 59012, //Social Score/Engagement
            "ts": 19, //Tweet Spam
            "sv": 133, //Social Volume
            "u": 10 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 0.12092679, //Price
            "ss": 20024, //Social Score/Engagement
            "ts": 58, //Tweet Spam
            "sv": 54, //Social Volume
            "u": 8 //URL Shares
        } ],
        "df": 1,
        "e2": 1
    },{ //API endpoint request
        "id": 2108, //LunarCRUSH internal ID for the asset
        "s": "ALGO", //symbol
        "n": "Algorand", //name
        "p": 2.08120156, //Price
        "p_btc": 0.000043132037420992, //Price (BTC)
        "v": 1436590585.61, //Volume (USD)
        "vt": 0.03055948777519635, //Volatility
        "pc": 5.46, //Percent Change (24 Hours)
        "pch": -1.52, //Percent Change (1 Hour)
        "mc": 12332505442, //Market Cap
        "gs": 62.5, //Galaxy Score™
        "ss": 15607726, //Social Score/Engagement
        "as": 3.558333333333333, //Average Sentiment - using a scoring system from 1 to 5 with 1 being very bearish and 5 being very bullish we provide the average over all coins
        "bl": 6261, //Bullish Sentiment - number of posts that we classified as bullish
        "br": 1374, //Bearish Sentiment - number of posts that we classified as bearish
        "sp": 1241, //Tweet Spam
        "na": 1, //News Articles
        "t": 9641, //Number of tweets (24 hours)
        "r": 849, //Reddit Activity (24 hours)
        "sv": 11110, //Social Volume
        "u": 1693, //URL Shares
        "c": 200, //Social Contributors (24 Hours)
        "sd": 0.8279544382755518, //Social Dominance
        "d": 0.4913659210124118, //Market Dominance
        "cr": 3.1,
        "acr": 4, //ALTRank
        "tc": 1525503600,
        "timeSeries": [{ //An array of metrics for hourly or daily data points
            "p": 2.09013418, //Price
            "ss": 120679, //Social Score/Engagement
            "ts": 39, //Tweet Spam
            "sv": 390, //Social Volume
            "u": 66 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 2.10139304, //Price
            "ss": 167209, //Social Score/Engagement
            "ts": 26, //Tweet Spam
            "sv": 324, //Social Volume
            "u": 62 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 2.13583709, //Price
            "ss": 202040, //Social Score/Engagement
            "ts": 21, //Tweet Spam
            "sv": 109, //Social Volume
            "u": 18 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 2.11613524, //Price
            "ss": 133992, //Social Score/Engagement
            "ts": 25, //Tweet Spam
            "sv": 210, //Social Volume
            "u": 30 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 2.11685121, //Price
            "ss": 114359, //Social Score/Engagement
            "na": 1, //News Articles
            "ts": 44, //Tweet Spam
            "sv": 505, //Social Volume
            "u": 104 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 2.08392199, //Price
            "ss": 182577, //Social Score/Engagement
            "ts": 50, //Tweet Spam
            "sv": 485, //Social Volume
            "u": 112 //URL Shares
        } ]
    },{ //API endpoint request
        "id": 2205, //LunarCRUSH internal ID for the asset
        "s": "HEX", //symbol
        "n": "HEX", //name
        "p": 0.50358562, //Price
        "p_btc": 0.000010436602693356, //Price (BTC)
        "v": 58009796.26, //Volume (USD)
        "vt": 0.08238942356604007, //Volatility
        "pc": 17.57, //Percent Change (24 Hours)
        "pch": -0.55, //Percent Change (1 Hour)
        "mc": 288142483519, //Market Cap
        "gs": 72.5, //Galaxy Score™
        "ss": 2402959, //Social Score/Engagement
        "as": 3.6250000000000004, //Average Sentiment - using a scoring system from 1 to 5 with 1 being very bearish and 5 being very bullish we provide the average over all coins
        "bl": 1068, //Bullish Sentiment - number of posts that we classified as bullish
        "br": 151, //Bearish Sentiment - number of posts that we classified as bearish
        "sp": 198, //Tweet Spam
        "t": 1477, //Number of tweets (24 hours)
        "r": 268, //Reddit Activity (24 hours)
        "sv": 1800, //Social Volume
        "u": 99, //URL Shares
        "c": 63, //Social Contributors (24 Hours)
        "sd": 0.13236276946311348, //Social Dominance
        "d": 11.480505519578841, //Market Dominance
        "cr": 4,
        "acr": 5, //ALTRank
        "tc": 1575741600,
        "timeSeries": [{ //An array of metrics for hourly or daily data points
            "p": 0.49591754, //Price
            "ss": 118546, //Social Score/Engagement
            "ts": 5, //Tweet Spam
            "sv": 76, //Social Volume
            "u": 3 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 0.51739996, //Price
            "ss": 28518, //Social Score/Engagement
            "ts": 4, //Tweet Spam
            "sv": 53, //Social Volume
            "u": 4 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 0.49742915, //Price
            "ss": 56854, //Social Score/Engagement
            "ts": 4, //Tweet Spam
            "sv": 54, //Social Volume
            "u": 4 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 0.50094885, //Price
            "ss": 52690, //Social Score/Engagement
            "ts": 2, //Tweet Spam
            "sv": 58, //Social Volume
            "u": 5 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 0.50782397, //Price
            "ss": 21516, //Social Score/Engagement
            "ts": 2, //Tweet Spam
            "sv": 52, //Social Volume
            "u": 2 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 0.503527, //Price
            "ss": 103185, //Social Score/Engagement
            "ts": 5, //Tweet Spam
            "sv": 41, //Social Volume
            "u": 5 //URL Shares
        } ]
    },{ //API endpoint request
        "id": 72, //LunarCRUSH internal ID for the asset
        "s": "XVG", //symbol
        "n": "Verge", //name
        "p": 0.026833529, //Price
        "p_btc": 5.56113736992e-7, //Price (BTC)
        "v": 123112728.59, //Volume (USD)
        "vt": 0.06868421499441502, //Volatility
        "pc": 12.19, //Percent Change (24 Hours)
        "pch": -1.25, //Percent Change (1 Hour)
        "mc": 441598279, //Market Cap
        "gs": 72, //Galaxy Score™
        "ss": 3249559, //Social Score/Engagement
        "as": 3.354166666666666, //Average Sentiment - using a scoring system from 1 to 5 with 1 being very bearish and 5 being very bullish we provide the average over all coins
        "bl": 537, //Bullish Sentiment - number of posts that we classified as bullish
        "br": 229, //Bearish Sentiment - number of posts that we classified as bearish
        "sp": 1299, //Tweet Spam
        "t": 850, //Number of tweets (24 hours)
        "r": 8, //Reddit Activity (24 hours)
        "sv": 907, //Social Volume
        "u": 75, //URL Shares
        "c": 56, //Social Contributors (24 Hours)
        "sd": 0.066253714113777, //Social Dominance
        "d": 0.017594668504207985, //Market Dominance
        "cr": 4.4,
        "acr": 6, //ALTRank
        "tc": 1523311200,
        "timeSeries": [{ //An array of metrics for hourly or daily data points
            "p": 0.027961495, //Price
            "ss": 16294, //Social Score/Engagement
            "ts": 39, //Tweet Spam
            "sv": 24, //Social Volume
            "u": 5 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 0.027780802, //Price
            "ss": 22430, //Social Score/Engagement
            "ts": 21, //Tweet Spam
            "sv": 19, //Social Volume
            "u": 1 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 0.027365865, //Price
            "ss": 6089, //Social Score/Engagement
            "ts": 44, //Tweet Spam
            "sv": 18, //Social Volume
            "u": 4 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 0.027593143, //Price
            "ss": 24137, //Social Score/Engagement
            "ts": 34, //Tweet Spam
            "sv": 26, //Social Volume
            "u": 7 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 0.027353806, //Price
            "ss": 14096, //Social Score/Engagement
            "ts": 55, //Tweet Spam
            "sv": 44, //Social Volume
            "u": 4 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 0.026603938, //Price
            "ss": 26423, //Social Score/Engagement
            "ts": 61, //Tweet Spam
            "sv": 66, //Social Volume
            "u": 9 //URL Shares
        } ]
    },{ //API endpoint request
        "id": 2239, //LunarCRUSH internal ID for the asset
        "s": "KDA", //symbol
        "n": "Kadena", //name
        "p": 2.26864946, //Price
        "p_btc": 0.00004701681724851, //Price (BTC)
        "v": 5322710.71, //Volume (USD)
        "vt": 0.10213103682767863, //Volatility
        "pc": 18.03, //Percent Change (24 Hours)
        "pch": 0.76, //Percent Change (1 Hour)
        "mc": 335253829, //Market Cap
        "gs": 58.5, //Galaxy Score™
        "ss": 20776790, //Social Score/Engagement
        "as": 3.5166666666666675, //Average Sentiment - using a scoring system from 1 to 5 with 1 being very bearish and 5 being very bullish we provide the average over all coins
        "bl": 2567, //Bullish Sentiment - number of posts that we classified as bullish
        "br": 662, //Bearish Sentiment - number of posts that we classified as bearish
        "sp": 631, //Tweet Spam
        "t": 4296, //Number of tweets (24 hours)
        "r": 24, //Reddit Activity (24 hours)
        "sv": 4302, //Social Volume
        "u": 122, //URL Shares
        "c": 73, //Social Contributors (24 Hours)
        "sd": 0.3172366704181506, //Social Dominance
        "d": 0.013357570141303537, //Market Dominance
        "cr": 3.3,
        "acr": 7, //ALTRank
        "tc": 1524258000,
        "timeSeries": [{ //An array of metrics for hourly or daily data points
            "p": 2.13624476, //Price
            "ss": 968845, //Social Score/Engagement
            "ts": 39, //Tweet Spam
            "sv": 54, //Social Volume
            "u": 1 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 2.0829664, //Price
            "ss": 720307, //Social Score/Engagement
            "ts": 5, //Tweet Spam
            "sv": 51, //Social Volume
            "u": 1 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 2.17785448, //Price
            "ss": 1894181, //Social Score/Engagement
            "ts": 5, //Tweet Spam
            "sv": 62, //Social Volume
            "u": 4 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 2.0896002, //Price
            "ss": 191162, //Social Score/Engagement
            "ts": 15, //Tweet Spam
            "sv": 110, //Social Volume
            "u": 5 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 2.15978764, //Price
            "ss": 291874, //Social Score/Engagement
            "ts": 18, //Tweet Spam
            "sv": 290, //Social Volume
            "u": 8 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 2.26682325, //Price
            "ss": 584762, //Social Score/Engagement
            "ts": 27, //Tweet Spam
            "sv": 241, //Social Volume
            "u": 8 //URL Shares
        } ]
    },{ //API endpoint request
        "id": 20, //LunarCRUSH internal ID for the asset
        "s": "XTZ", //symbol
        "n": "Tezos", //name
        "p": 6.47228297, //Price
        "p_btc": 0.000134135374788635, //Price (BTC)
        "v": 905759851.54, //Volume (USD)
        "vt": 0.02307937321056848, //Volatility
        "pc": 2.82, //Percent Change (24 Hours)
        "pch": -1, //Percent Change (1 Hour)
        "mc": 5469910305, //Market Cap
        "gs": 59.5, //Galaxy Score™
        "ss": 28041373, //Social Score/Engagement
        "as": 3.6125000000000007, //Average Sentiment - using a scoring system from 1 to 5 with 1 being very bearish and 5 being very bullish we provide the average over all coins
        "bl": 15939, //Bullish Sentiment - number of posts that we classified as bullish
        "br": 2434, //Bearish Sentiment - number of posts that we classified as bearish
        "sp": 3029, //Tweet Spam
        "na": 1, //News Articles
        "md": 2,
        "t": 24007, //Number of tweets (24 hours)
        "r": 192, //Reddit Activity (24 hours)
        "sv": 26157, //Social Volume
        "u": 5026, //URL Shares
        "c": 462, //Social Contributors (24 Hours)
        "sd": 1.9641767035739395, //Social Dominance
        "d": 0.21793848196638055, //Market Dominance
        "cr": 2.7,
        "acr": 8, //ALTRank
        "tc": 1523469600,
        "timeSeries": [{ //An array of metrics for hourly or daily data points
            "p": 6.43240006, //Price
            "ss": 879661, //Social Score/Engagement
            "ts": 108, //Tweet Spam
            "sv": 632, //Social Volume
            "u": 186 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 6.45804757, //Price
            "ss": 636338, //Social Score/Engagement
            "ts": 122, //Tweet Spam
            "sv": 714, //Social Volume
            "u": 228 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 6.44015851, //Price
            "ss": 410725, //Social Score/Engagement
            "ts": 101, //Tweet Spam
            "sv": 642, //Social Volume
            "u": 132 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 6.47128534, //Price
            "ss": 965194, //Social Score/Engagement
            "ts": 121, //Tweet Spam
            "sv": 789, //Social Volume
            "u": 172 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 6.52269099, //Price
            "ss": 952874, //Social Score/Engagement
            "ts": 143, //Tweet Spam
            "sv": 899, //Social Volume
            "u": 196 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 6.46869403, //Price
            "ss": 1365709, //Social Score/Engagement
            "ts": 108, //Tweet Spam
            "sv": 988, //Social Volume
            "u": 201 //URL Shares
        } ],
        "nft": 1
    },{ //API endpoint request
        "id": 3079, //LunarCRUSH internal ID for the asset
        "s": "SOL", //symbol
        "n": "Solana", //name
        "p": 162.44390594, //Price
        "p_btc": 0.0033665824418353, //Price (BTC)
        "v": 6327431533.99, //Volume (USD)
        "vt": 0.06058151816744794, //Volatility
        "pc": 2.51, //Percent Change (24 Hours)
        "pch": -0.65, //Percent Change (1 Hour)
        "mc": 48240591472, //Market Cap
        "gs": 55, //Galaxy Score™
        "ss": 39686074, //Social Score/Engagement
        "as": 3.3708333333333322, //Average Sentiment - using a scoring system from 1 to 5 with 1 being very bearish and 5 being very bullish we provide the average over all coins
        "bl": 7124, //Bullish Sentiment - number of posts that we classified as bullish
        "br": 2280, //Bearish Sentiment - number of posts that we classified as bearish
        "sp": 12957, //Tweet Spam
        "na": 12, //News Articles
        "t": 14614, //Number of tweets (24 hours)
        "r": 1008, //Reddit Activity (24 hours)
        "sv": 16534, //Social Volume
        "u": 3336, //URL Shares
        "c": 940, //Social Contributors (24 Hours)
        "sd": 1.251587629939735, //Social Dominance
        "d": 1.922057344332999, //Market Dominance
        "cr": 2.6,
        "acr": 9, //ALTRank
        "tc": 1533927600,
        "timeSeries": [{ //An array of metrics for hourly or daily data points
            "p": 162.74182572, //Price
            "ss": 1033520, //Social Score/Engagement
            "ts": 445, //Tweet Spam
            "sv": 384, //Social Volume
            "u": 53 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 164.49821618, //Price
            "ss": 1697687, //Social Score/Engagement
            "ts": 444, //Tweet Spam
            "sv": 442, //Social Volume
            "u": 27 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 162.12280414, //Price
            "ss": 473616, //Social Score/Engagement
            "ts": 407, //Tweet Spam
            "sv": 416, //Social Volume
            "u": 15 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 161.86961781, //Price
            "ss": 666801, //Social Score/Engagement
            "ts": 491, //Tweet Spam
            "sv": 512, //Social Volume
            "u": 79 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 163.0136543, //Price
            "ss": 353368, //Social Score/Engagement
            "ts": 384, //Tweet Spam
            "sv": 365, //Social Volume
            "u": 105 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 162.37727092, //Price
            "ss": 867168, //Social Score/Engagement
            "ts": 428, //Tweet Spam
            "sv": 395, //Social Volume
            "u": 92 //URL Shares
        } ]
    },{ //API endpoint request
        "id": 3377, //LunarCRUSH internal ID for the asset
        "s": "NEAR", //symbol
        "n": "Near Protocol", //name
        "p": 9.19505809, //Price
        "p_btc": 0.000190563757614173, //Price (BTC)
        "v": 413426183.95, //Volume (USD)
        "vt": 0.0383305336499897, //Volatility
        "pc": 5.28, //Percent Change (24 Hours)
        "pch": -0.63, //Percent Change (1 Hour)
        "mc": 4259779443, //Market Cap
        "gs": 69, //Galaxy Score™
        "ss": 3088748, //Social Score/Engagement
        "as": 3.4749999999999996, //Average Sentiment - using a scoring system from 1 to 5 with 1 being very bearish and 5 being very bullish we provide the average over all coins
        "bl": 776, //Bullish Sentiment - number of posts that we classified as bullish
        "br": 293, //Bearish Sentiment - number of posts that we classified as bearish
        "sp": 650, //Tweet Spam
        "t": 1195, //Number of tweets (24 hours)
        "r": 3, //Reddit Activity (24 hours)
        "sv": 1313, //Social Volume
        "u": 220, //URL Shares
        "c": 53, //Social Contributors (24 Hours)
        "sd": 0.09815097167292075, //Social Dominance
        "d": 0.16972305093748957, //Market Dominance
        "cr": 2.8,
        "acr": 10, //ALTRank
        "tc": 1610460000,
        "timeSeries": [{ //An array of metrics for hourly or daily data points
            "p": 8.85722522, //Price
            "ss": 21204, //Social Score/Engagement
            "ts": 23, //Tweet Spam
            "sv": 28, //Social Volume
            "u": 10 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 8.86095705, //Price
            "ss": 71292, //Social Score/Engagement
            "ts": 17, //Tweet Spam
            "sv": 38, //Social Volume
            "u": 10 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 8.95846963, //Price
            "ss": 8834, //Social Score/Engagement
            "ts": 15, //Tweet Spam
            "sv": 32, //Social Volume
            "u": 8 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 9.15821559, //Price
            "ss": 175670, //Social Score/Engagement
            "ts": 22, //Tweet Spam
            "sv": 47, //Social Volume
            "u": 10 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 9.265029, //Price
            "ss": 127207, //Social Score/Engagement
            "ts": 23, //Tweet Spam
            "sv": 58, //Social Volume
            "u": 11 //URL Shares
        },{ //An array of metrics for hourly or daily data points
            "p": 9.22586375, //Price
            "ss": 183149, //Social Score/Engagement
            "ts": 23, //Tweet Spam
            "sv": 50, //Social Volume
            "u": 13 //URL Shares
        } ]
    } ]
}

```


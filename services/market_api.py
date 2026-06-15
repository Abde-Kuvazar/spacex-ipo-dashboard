import pandas as pd
import yfinance as yf


def get_market_caps():

    companies = {

        "Apple": "AAPL",
        "Microsoft": "MSFT",
        "Nvidia": "NVDA",
        "Alphabet": "GOOG",
        "Amazon": "AMZN",
        "Tesla": "TSLA"

    }

    rows = []

    try:

        for company, ticker in companies.items():

            info = yf.Ticker(ticker).info

            rows.append({

                "Company": company,

                "Ticker": ticker,

                "Sector": info.get("sector", "Technology"),

                "Market Cap": f"${info.get('marketCap',0)/1e9:.0f}B",

                "Raw Market Cap": info.get("marketCap",0)

            })

        return pd.DataFrame(rows)

    except Exception:

        # ---------- FALLBACK ----------

        return pd.DataFrame([

            {

                "Company":"Apple",

                "Ticker":"AAPL",

                "Sector":"Technology",

                "Market Cap":"$4300B",

                "Raw Market Cap":4300e9

            },

            {

                "Company":"Microsoft",

                "Ticker":"MSFT",

                "Sector":"Technology",

                "Market Cap":"$3900B",

                "Raw Market Cap":3900e9

            },

            {

                "Company":"Nvidia",

                "Ticker":"NVDA",

                "Sector":"Technology",

                "Market Cap":"$4200B",

                "Raw Market Cap":4200e9

            },

            {

                "Company":"Alphabet",

                "Ticker":"GOOG",

                "Sector":"Technology",

                "Market Cap":"$2400B",

                "Raw Market Cap":2400e9

            },

            {

                "Company":"Amazon",

                "Ticker":"AMZN",

                "Sector":"Consumer",

                "Market Cap":"$2500B",

                "Raw Market Cap":2500e9

            },

            {

                "Company":"Tesla",

                "Ticker":"TSLA",

                "Sector":"Automotive",

                "Market Cap":"$1000B",

                "Raw Market Cap":1000e9

            }

        ])
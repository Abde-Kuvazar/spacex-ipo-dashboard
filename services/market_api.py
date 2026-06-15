import yfinance as yf
import pandas as pd
from utils.helper import format_market_cap

SPACEX_VALUATION = 450_000_000_000
SPACEX_IPO_SIZE = 35_000_000_000

COMPANIES = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Nvidia": "NVDA",
    "Amazon": "AMZN",
    "Alphabet": "GOOGL",
    "Tesla": "TSLA"
}

COMPANY_SECTORS = {

    "Apple":"Technology",

    "Microsoft":"Technology",

    "Nvidia":"AI",

    "Alphabet":"Technology",

    "Amazon":"Consumer",

    "Tesla":"EV"

}

def get_market_caps():

    rows = []

    for company, ticker in COMPANIES.items():

        info = yf.Ticker(ticker).info
        market_cap = info.get("marketCap", 0)

        rows.append({

            "Company":company,

            "Ticker":ticker,

            "Sector":COMPANY_SECTORS[company],

            "Market Cap":format_market_cap(market_cap),

            "Raw Market Cap":market_cap

        })

    df = pd.DataFrame(rows)

    return df

def add_spacex(df, valuation):

    spacex_market_cap = valuation

    spacex_row = {
        "Company": "🚀 SpaceX",
        "Ticker": "SPACEX",
        "Market Cap": format_market_cap(spacex_market_cap),
        "Raw Market Cap": spacex_market_cap
    }

    df.loc[len(df)] = spacex_row

    df = df.sort_values(
        by="Raw Market Cap",
        ascending=False
    ).reset_index(drop=True)

    return df[["Company", "Ticker", "Market Cap", "Raw Market Cap"]]



    return df.iloc[0]["Company"]
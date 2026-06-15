def get_spacex_rank(df):

    rank = df.index[df["Ticker"] == "SPACEX"].tolist()

    if rank:
        return rank[0] + 1

    return None


def get_total_market_cap(df):

    return df["Raw Market Cap"].sum()


def get_spacex_market_share(df):

    spacex = df[df["Ticker"] == "SPACEX"]["Raw Market Cap"].iloc[0]

    total = get_total_market_cap(df)

    return round((spacex / total) * 100, 2)


def get_largest_company(df):

    return df.iloc[0]["Company"]
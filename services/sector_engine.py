import pandas as pd


def calculate_sector_scores():

    sectors = pd.read_csv(

        "data/sector_weights.csv"

    )

    companies = pd.read_csv(

        "data/companies.csv"

    )

    sectors["Impact Score"] = (

        sectors["Exposure"] * .45

        +

        sectors["Correlation"] * .35

        +

        sectors["CapitalRotation"] * .20

    )

    merged = companies.merge(

        sectors,

        on="Sector",

        suffixes=("_company", "_sector")

    )

    merged["Expected Change"] = (

        merged["Exposure_company"]

        *

        merged["Impact Score"]

        *

        18

    )

    merged = merged.sort_values(

        "Expected Change",

        ascending=False

    )

    return merged
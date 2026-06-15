import pandas as pd


def predict_week1_return(

    valuation,

    regime="Neutral"

):

    ipos = pd.read_csv(

        "data/historical_ipos.csv"

    )

    historical = ipos["Week1_Return"].mean()

    valuation_factor = valuation / 450

    regime_factor = {

        "Bull": 1.20,

        "Neutral": 1.00,

        "Bear": 0.82

    }

    prediction = (

        historical

        * valuation_factor

        * regime_factor[regime]

    )

    return round(prediction, 2)
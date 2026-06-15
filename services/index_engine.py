import json


def load_assumptions():

    with open("data/assumptions.json", "r") as f:

        return json.load(f)


def calculate_index_weights(

    valuation,

    float_pct

):

    assumptions = load_assumptions()

    sp500_cap = assumptions["sp500_market_cap"]

    nasdaq_cap = assumptions["nasdaq_market_cap"]

    passive_assets = assumptions["passive_assets"]

    public_value = valuation * float_pct / 100

    sp500_weight = (

        public_value

        /

        (sp500_cap + public_value)

    ) * 100

    nasdaq_weight = (

        public_value

        /

        (nasdaq_cap + public_value)

    ) * 100

    passive_inflow = (

        passive_assets

        *

        (sp500_weight / 100)

    )

    return {

        "public_value": public_value,

        "sp500": sp500_weight,

        "nasdaq": nasdaq_weight,

        "passive": passive_inflow

    }
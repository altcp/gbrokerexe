""" Automated Tests and (or) Usage Examples """
from gbrokerexe.oanda import oandacandle


def test_read():

    endpoint = "https://api-fxtrade.oanda.com/v3/instruments/"
    authorization = "YOUR_API"

    payload = {"count": 100, "price": "M", "granularity": "S5"}
    df1, error = oandacandle(authorization, endpoint, "EURUSD", payload).get()

    # If succesful, error == 0
    assert error == 1

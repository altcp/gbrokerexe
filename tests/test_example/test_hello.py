""" Automated Tests and (or) Usage Examples """
import pytest

import gbrokerexe.oanda as exe


def read():

    endpoint = "https://api-fxtrade.oanda.com/v3/instruments/"
    authorization = "YOUR_API"

    payload = {"count": 100, "price": "M", "granularity": "S5"}
    df = exe.oandacandle(authorization, endpoint, "EURUSD", payload).get()

    assert not df.empty

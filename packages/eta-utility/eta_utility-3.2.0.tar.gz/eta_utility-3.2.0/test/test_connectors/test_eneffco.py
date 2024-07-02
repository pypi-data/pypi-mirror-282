import asyncio
from datetime import datetime, timedelta

import pandas as pd
import pytest
import requests

from eta_utility.connectors import DFSubHandler, EnEffCoConnection, Node

from ..utilities.requests.eneffco_request import request

# Results used for local tests
sample_series = pd.Series(
    data=[1, 2, 3], index=pd.DatetimeIndex(["2020-11-05 10:00:00", "2020-11-05 10:00:01.1", "2020-11-05 10:15:01.7"])
)


@pytest.fixture()
def eneffco_nodes(config_eneffco):
    return {
        "node": Node(
            "CH1.Elek_U.L1-N",
            config_eneffco["url"],
            "eneffco",
            eneffco_code="CH1.Elek_U.L1-N",
        ),
        "node2": Node("Pu3.425.ThHy_Q", config_eneffco["url"], "eneffco", eneffco_code="Pu3.425.ThHy_Q"),
        "node_write": Node("RM.Elek_P.Progn", config_eneffco["url"], "eneffco", eneffco_code="RM.Elek_P.Progn"),
    }


async def stop_execution(sleep_time):
    await asyncio.sleep(sleep_time)
    raise KeyboardInterrupt


@pytest.fixture(autouse=True)
def _local_requests(monkeypatch):
    monkeypatch.setattr(requests, "request", request)


def test_check_access(config_eneffco):
    # Check access to see, whether anything responds
    try:
        result = requests.request("GET", config_eneffco["url"])
    except Exception as e:
        pytest.fail(str(e))

    assert result.status_code == 200, "Could not access eneffco server for testing."


def test_eneffco_read(config_eneffco):
    """Test eneffco read function"""

    node = Node(
        "CH1.Elek_U.L1-N",
        config_eneffco["url"],
        "eneffco",
        eneffco_code="CH1.Elek_U.L1-N",
    )
    node2 = Node("Pu3.425.ThHy_Q", config_eneffco["url"], "eneffco", eneffco_code="Pu3.425.ThHy_Q")

    # Test reading a single node
    server = EnEffCoConnection(
        node.url, config_eneffco["user"], config_eneffco["pw"], api_token=config_eneffco["postman_token"]
    )
    # The interval is arbitrary here. range int[1,10]
    res = server.read_series(
        datetime.now() - timedelta(seconds=10),
        datetime.now(),
        [node, node2],
        timedelta(seconds=1),
    )

    assert isinstance(res, pd.DataFrame)
    assert set(res.columns) == {"CH1.Elek_U.L1-N", "Pu3.425.ThHy_Q"}

    res2 = server.read({node, node2})
    assert isinstance(res2, pd.DataFrame)
    assert set(res2.columns) == {"CH1.Elek_U.L1-N", "Pu3.425.ThHy_Q"}
    assert len(res2.index) == 10


def test_eneffco_read_info(config_eneffco, eneffco_nodes):
    """Test the read_info() method"""
    server = EnEffCoConnection(
        eneffco_nodes["node"].url,
        config_eneffco["user"],
        config_eneffco["pw"],
        api_token=config_eneffco["postman_token"],
    )

    res = server.read_info([eneffco_nodes["node"], eneffco_nodes["node2"]])

    assert isinstance(res, pd.DataFrame)
    assert len(res) > 0


def test_eneffco_write(config_eneffco, eneffco_nodes):
    """Test writing a single node"""
    server = EnEffCoConnection(
        eneffco_nodes["node_write"].url,
        config_eneffco["user"],
        config_eneffco["pw"],
        api_token=config_eneffco["postman_token"],
    )

    server.write({eneffco_nodes["node"]: sample_series})


def test_eneffco_subscribe_multi(config_eneffco, eneffco_nodes):
    """Test eneffco subscribe_series function; this needs network access"""

    # Test subscribing nodes with multiple time steps
    server = EnEffCoConnection(
        eneffco_nodes["node"].url,
        config_eneffco["user"],
        config_eneffco["pw"],
        api_token=config_eneffco["postman_token"],
    )
    # changed write_interval from 10 to 1
    handler = DFSubHandler(write_interval=1)
    loop = asyncio.get_event_loop()

    try:
        # changed req_interval from 60 to 10
        server.subscribe_series(
            handler, req_interval=10, data_interval=2, nodes=[eneffco_nodes["node"], eneffco_nodes["node2"]]
        )
        loop.run_until_complete(stop_execution(2))
    except KeyboardInterrupt:
        pass
    finally:
        server.close_sub()
        handler.close()


def test_connection_from_node_ids(config_eneffco):
    server = EnEffCoConnection.from_ids(
        ids=["CH1.Elek_U.L1-N", "Pu3.425.ThHy_Q"],
        url=config_eneffco["url"],
        usr=config_eneffco["user"],
        pwd=config_eneffco["pw"],
        api_token=config_eneffco["postman_token"],
    )
    res = server.read_series(
        from_time=datetime.now() - timedelta(seconds=10),
        to_time=datetime.now(),
        interval=timedelta(seconds=1),
    )

    assert isinstance(res, pd.DataFrame)
    assert set(res.columns) == {"CH1.Elek_U.L1-N", "Pu3.425.ThHy_Q"}

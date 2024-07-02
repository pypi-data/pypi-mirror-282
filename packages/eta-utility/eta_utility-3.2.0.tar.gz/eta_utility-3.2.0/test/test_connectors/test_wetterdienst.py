from datetime import datetime, timedelta, timezone

import pytest

from eta_utility.connectors import Node, WetterdienstConnection

pred_nodes = [
    Node(
        "pred_node1",
        "https://opendata.dwd.de",
        "wetterdienst_prediction",
        parameter="WIND_SPEED",
        mosmix_type="SMALL",
        station_id="K2596",  # Darmstadt prediction ID
    ),
    Node(
        "pred_node2",
        "https://opendata.dwd.de",
        "wetterdienst_prediction",
        parameter="temperature_air_mean_200",
        mosmix_type="LARGE",
        latlon=(49.86376654168076, 8.681726558050716),
        number_of_stations=3,
    ),
]

obsv_nodes = [
    Node(
        "obsv_node1",
        "https://opendata.dwd.de",
        "wetterdienst_observation",
        parameter="temperature_air_mean_200",
        station_id="00917",  # Darmstadt observation ID
        interval=600,
    ),
    Node(
        "obsv_node2",
        "https://opendata.dwd.de",
        "wetterdienst_observation",
        parameter="HUMIDITY",
        station_id="00044",
        interval=3600,
    ),
    Node(
        "obsv_node3",
        "https://opendata.dwd.de",
        "wetterdienst_observation",
        parameter="HUMIDITY",
        latlon=(49.86376654168076, 8.681726558050716),
        number_of_stations=3,
        interval=3600,
    ),
]


class TestWetterdienstConnection:
    @pytest.mark.skip(reason="wetterdienst API for observations is not working properly.")
    def test_observation(self):
        connector = WetterdienstConnection.from_node(obsv_nodes)

        from_datetime = datetime(2024, 1, 16, 15, 00).replace(tzinfo=timezone.utc)
        to_datetime = datetime(2024, 1, 16, 20, 00).replace(tzinfo=timezone.utc)

        result = connector.read_series(from_time=from_datetime, to_time=to_datetime, interval=timedelta(minutes=20))

        assert result.shape == (16, 5)

    def test_prediction(self):
        connector = WetterdienstConnection.from_node(pred_nodes)

        from_datetime = datetime.now()
        to_datetime = from_datetime + timedelta(days=1)

        result = connector.read_series(from_time=from_datetime, to_time=to_datetime)

        assert result.shape == (24, 4)

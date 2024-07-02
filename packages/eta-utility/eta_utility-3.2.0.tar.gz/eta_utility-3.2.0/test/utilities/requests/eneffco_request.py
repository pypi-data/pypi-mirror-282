import json
import pathlib
import re

from requests import Response as _Response


class Response(_Response):
    def __init__(self, json_data=None, status_code=400):
        super().__init__()
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

    def text(self):
        pass


def request(method, url, **kwargs):
    try:
        endpoint = url.split("API/v1.0/", 1)[1]
    except IndexError:
        endpoint = ""

    with open(pathlib.Path(__file__).parent / "eneffco_sample_data.json") as f:
        data = json.load(f)

    if method == "GET":
        re_readseries = re.compile(r"datapoint/(.*)/value\?from=(.*)&to=(.*)&timeInterval=(.*)&")

        if endpoint == "":
            # Empty request
            return Response(status_code=200)
        elif endpoint == "/datapoint":
            # Datapoint IDs
            return Response(data["datapoint"], 200)

        elif endpoint == "/rawdatapoint":
            # Raw Datapoint IDs
            return Response(data["rawdatapoint"], 200)

        elif re.match(r"datapoint\/([^\/]+)$", endpoint):
            # Datapoint Information
            _id = endpoint.split("/")[1]
            return Response(data["datapoint_info"][_id], 200)

        elif re_readseries.match(endpoint):
            # Read Series
            match = re_readseries.match(endpoint)
            _id = match.groups()[0]
            timeinterval = int(match.groups()[3])

            return Response(data["series_data"][_id][::timeinterval], 200)

        elif re.match(r"datapoint\/([^\/]+)/live$", endpoint):
            # Live data
            _id = endpoint.split("/")[1]
            return Response(data["live_data"][_id], 200)

        else:
            return Response(status_code=404)

    elif method == "POST":
        _id = re.match(r"rawdatapoint\/([^\/]+)/value$", endpoint).groups()[0]
        if _id in [i["Id"] for i in data["rawdatapoint"]]:
            return Response(status_code=200)
        else:
            return Response(status_code=400)

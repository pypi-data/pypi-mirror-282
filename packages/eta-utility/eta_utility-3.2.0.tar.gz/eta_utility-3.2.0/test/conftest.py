import asyncio
import pathlib
import platform
import random
import shutil
import socket

import pytest


@pytest.fixture(scope="session")
def temp_dir():
    while True:
        temp_dir = pathlib.Path.cwd() / f"tmp_{random.randint(10000,99999)}"
        try:
            temp_dir.mkdir(exist_ok=False)
        except FileExistsError:
            continue
        else:
            break

    yield temp_dir
    shutil.rmtree(temp_dir)


async def stop_execution(sleep_time):
    await asyncio.sleep(sleep_time)


@pytest.fixture(scope="session")
def config_modbus_port():
    if platform.system() == "Linux" or platform.system() == "Darwin":
        return 5050
    return 502


@pytest.fixture(scope="session")
def config_host_ip():
    try:
        return socket.gethostbyname(socket.gethostname())
    except socket.gaierror:
        return "127.0.0.1"


@pytest.fixture(scope="session")
def config_eneffco():
    """Test configuration for EnEffCo."""
    return {"user": "", "pw": "", "url": "", "postman_token": ""}


@pytest.fixture(scope="session")
def config_cumulocity():
    """Test configuration for Cumulocity."""
    return {"user": "", "pw": "", "url": "", "tenant": ""}


@pytest.fixture(scope="session")
def config_entsoe():
    """Test configuration for entso-e connector"""
    return {"path": pathlib.Path(__file__).parent / "resources/entsoe/"}


@pytest.fixture(scope="session")
def config_forecast_solar():
    """Test configuration for forecast solar."""
    return {"url": "https://api.forecast.solar"}


@pytest.fixture(scope="session")
def config_nodes_file():
    """Test configuration for reading nodes."""
    return {"file": pathlib.Path(__file__).parent / "resources/test_excel_node_list.xls", "sheet": "Sheet1"}


@pytest.fixture(scope="session")
def config_live_connect():
    """Test configuration for live connect."""
    return {"file": pathlib.Path(__file__).parent / "resources/config_live_connect.json"}


@pytest.fixture(scope="session")
def config_fmu():
    """Test configuration for FMU simulator."""
    return {"file": pathlib.Path(__file__).parent / "resources/damped_oscillator/damped_oscillator.fmu"}


@pytest.fixture(scope="session")
def config_etax_resources_path():
    return pathlib.Path(__file__).parent / "resources" / "agents"

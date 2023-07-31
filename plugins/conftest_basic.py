import pytest
import yaml

from api.user_api import UserApi
from common.yaml_structer import Struct


def pytest_addoption(parser):
    group = parser.getgroup("Test api configuration")
    group.addoption("--env-cfg", help="Конфигурационный файл")


@pytest.fixture(scope="session")
def cfg(request):
    cfg = request.config.getoption("--env-cfg")
    with open(cfg, "r") as stream:
        return Struct(**yaml.safe_load(stream))


@pytest.fixture()
def api(cfg):
    user_api = UserApi(host=cfg.gateways.host)
    yield user_api

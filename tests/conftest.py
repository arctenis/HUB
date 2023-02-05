import pytest
import hub

@pytest.fixture
def init_fixture(tmp_path):
    hub.init(tmp_path)



from spektral import models
from tests.test_models.core import MODES, run_model

config = {
    "model": models.GeneralGNN,
    "modes": [MODES["SINGLE"], MODES["DISJOINT"], MODES["MIXED"]],
    "kwargs": {"output": 32, "connectivity": "cat", "pool": "sum"},
    "edges": False,
    "dense": False,
    "sparse": True,
}


def test_model():
    run_model(config)

    config["kwargs"]["pool"] = None
    run_model(config)

    config["kwargs"]["connectivity"] = "sum"
    run_model(config)

    config["kwargs"]["connectivity"] = None
    run_model(config)

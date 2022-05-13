import json
from typing import Any


class HealthChecker:

    @staticmethod
    def check_health() -> Any:
        return json.dumps("Healthy"), 200, {"Content-Type": "application/json"}

import json
from typing import List

from .models import Thruster


def load_thrusters(path: str) -> List[Thruster]:
    with open(path, "r") as f:
        raw = json.load(f)
    return [Thruster(**t) for t in raw]


def is_feasible(thruster: Thruster, delta_v: float, max_power: float) -> bool:
    if thruster.power_W > max_power:
        return False

    if thruster.isp_s < 500 and delta_v > 300:
        return False

    return True


def score_thruster(thruster: Thruster) -> float:
    return thruster.isp_s / thruster.thruster_mass_kg


def select_thrusters(
    thrusters: List[Thruster],
    delta_v: float,
    max_power: float
) -> List[Thruster]:

    feasible = [
        t for t in thrusters
        if is_feasible(t, delta_v, max_power)
    ]

    return sorted(feasible, key=score_thruster, reverse=True)

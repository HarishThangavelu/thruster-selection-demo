from dataclasses import dataclass

@dataclass
class Thruster:
    name: str
    type: str
    thrust_mN: float
    isp_s: float
    power_W: float
    thruster_mass_kg: float
    trl: int

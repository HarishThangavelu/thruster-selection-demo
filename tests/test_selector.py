from src.models import Thruster
from src.selector import select_thrusters

def test_power_filtering():
    thruster = Thruster(
        name="Test",
        type="Ion",
        thrust_mN=1,
        isp_s=2000,
        power_W=200,
        thruster_mass_kg=1,
        trl=5
    )

    result = select_thrusters(
        [thruster],
        delta_v=100,
        max_power=100
    )

    assert len(result) == 0

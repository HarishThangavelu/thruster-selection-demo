import argparse
from .selector import load_thrusters, select_thrusters


def main():
    parser = argparse.ArgumentParser(
        description="Thruster selection demo tool"
    )
    parser.add_argument("--delta-v", type=float, required=True, help="Required delta-v [m/s]")
    parser.add_argument("--power", type=float, required=True, help="Available power [W]")

    args = parser.parse_args()

    thrusters = load_thrusters("data/thrusters.json")
    ranked = select_thrusters(thrusters, args.delta_v, args.power)

    if not ranked:
        print("No feasible thrusters found.")
        return

    print("Feasible thrusters (ranked):")
    for t in ranked:
        print(
            f"- {t.name} | {t.type} | "
            f"Isp={t.isp_s}s | Mass={t.thruster_mass_kg}kg | Power={t.power_W}W"
        )


if __name__ == "__main__":
    main()
 
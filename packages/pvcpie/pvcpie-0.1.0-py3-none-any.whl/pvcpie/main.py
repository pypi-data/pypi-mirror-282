import argparse
from pvcpie.kubernetesUtils import KubernetesUtils
from prettytable import PrettyTable


parser = argparse.ArgumentParser(
    prog="Pvcpie",
    usage="%(prog)s [options]",
    description="Provide input flags as per your requirement",
)

parser.add_argument(
    "-i",
    "--incluster",
    action="store_true",
    help="Use this flag if you want to load in cluster config intead of kube config",
)

parser.add_argument(
    "--api",
    action="store_true",
    help="Use to run in CLI mode",
)


args = parser.parse_args()


def bytes_to_readable(byte_value):
    if byte_value < 1024:
        return f"{byte_value} bytes"
    elif byte_value < 1024 * 1024:
        return f"{byte_value / 1024:.2f} KB"
    elif byte_value < 1024 * 1024 * 1024:
        return f"{byte_value / (1024 * 1024):.2f} MB"
    else:
        return f"{byte_value / (1024 * 1024 * 1024):.2f} GB"


def run_cli_mode(kts):
    nodes = kts.list_all_nodes()
    output = PrettyTable(
        [
            "PVC Name",
            "Namespace",
            "AvailableBytes",
            "CapacityBytes",
            "UsedBytes",
            "% Used",
        ]
    )

    for node in nodes:
        res = kts.get_node_summary(node)
        volumes = kts.get_pvc_summary(res)

        for vol in volumes:
            output.add_row(
                [
                    vol["pvc_name"],
                    vol["namespace"],
                    bytes_to_readable(vol["availableBytes"]),
                    bytes_to_readable(vol["capacityBytes"]),
                    bytes_to_readable(vol["usedBytes"]),
                    f'{(vol["usedBytes"] * 100) / (vol["capacityBytes"]):.2f}',
                ]
            )
    print(output)


def run_api_mode(kts):
    nodes = kts.list_all_nodes()
    data = []

    for node in nodes:
        res = kts.get_node_summary(node)
        volumes = kts.get_pvc_summary(res)

        for vol in volumes:
            data.append(
                {
                    "PVC Name": vol["pvc_name"],
                    "Namespace": vol["namespace"],
                    "AvailableBytes": bytes_to_readable(vol["availableBytes"]),
                    "CapacityBytes": bytes_to_readable(vol["capacityBytes"]),
                    "UsedBytes": bytes_to_readable(vol["usedBytes"]),
                    "% Used": f'{(vol["usedBytes"] * 100) / (vol["capacityBytes"]):.2f}',
                }
            )
    print(data)
    return data


def main():
    kts = KubernetesUtils(incluster_config=args.incluster)

    if args.api:
        run_api_mode(kts)
    else:
        run_cli_mode(kts)

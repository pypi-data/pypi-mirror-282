import json
from kubernetes import client, config


class KubernetesUtils:
    def __init__(self, incluster_config=False):
        try:
            if incluster_config:
                config.load_incluster_config()
            else:
                config.load_kube_config()
        except Exception as e:
            print("Unable to load config")

        self.client = client.CoreV1Api()

    def get_namespaces(self):
        try:
            namespaces = self.client.list_namespace()
            res = [ns.metadata.name for ns in namespaces.items]
            return res
        except Exception as e:
            print(f"Unable to get namespaces. Error: {e}")

    def get_namespace_pods(self, namespace):
        try:
            res = self.client.list_namespaced_pod(namespace)
            pods = [pod.metadata.name for pod in res.items]
            return pods
        except Exception as e:
            print(f"Unable to get namespaces. Error: {e}")

    def get_pod_node_name(self, pod_name, namespace):
        try:
            pod = self.client.read_namespaced_pod(pod_name, namespace)
            return pod.spec.node_name
        except Exception as e:
            print(f"Unable to get namespaces. Error: {e}")

    def list_all_nodes(self):
        try:
            res = self.client.list_node(pretty=True)
            nodes = [node.metadata.name for node in res.items]
            return nodes
        except Exception as e:
            print(f"Unable to get nodes. Error: {e}")

    def get_node_summary(self, node_name):
        try:
            res = self.client.connect_get_node_proxy_with_path(
                node_name, path="/stats/summary"
            )
            res = res.replace("'", '"')
            res = json.loads(res)
            return res
        except Exception as e:
            print(f"Unable to get node summary. Error: {e}")

    def get_pvc_summary(self, node_summary):
        try:
            pods = node_summary["pods"]
            pod_volumes = [pod["volume"] for pod in pods if "volume" in pod]

            pvc_volumes = []
            for volumes in pod_volumes:
                for vol in volumes:
                    if "pvcRef" in vol:
                        pvc_volumes.append(
                            {
                                "pvc_name": vol["pvcRef"]["name"],
                                "namespace": vol["pvcRef"]["namespace"],
                                "availableBytes": vol["availableBytes"],
                                "capacityBytes": vol["capacityBytes"],
                                "usedBytes": vol["usedBytes"],
                            }
                        )
            return pvc_volumes
        except Exception as e:
            print(f"Error parsing summary {e}")

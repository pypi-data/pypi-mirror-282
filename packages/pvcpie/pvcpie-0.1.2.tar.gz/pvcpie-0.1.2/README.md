# Pvcpie
A tool to get pvc usage information from kubernetes for a cluster. It uses [kubernetes nodes metric data](https://kubernetes.io/docs/reference/instrumentation/node-metrics/) to fetch volumes for and calculate their disk usage.

# Usage

You can directly install it from `pip` :
```
pip install pvcpie
```

# Development guide

To run this on your local, clone this repo and run following commands:

1. Install poetry on your local if not present
```
pip install poetry
```

2. Go to project directory and install dependencies using
```
poetry install
```

3. To run on your CLI, run command:
```
poetry run pvcpie
```

or activate poetry shell using `poetry shell`
```
pvcpie
```

If you want to use incluster config instead of kube config use `-i` flag:
```
pvcpie -i
```
or
```
poetry run pvcpie -i
```

or run this in api mode to get the json data. 
```
poetry run pvcpie --api
```
TODO:
[ ] Add a swagger page to get metrics in API mode from cluster

## Customize

To customize it for other requirements, `KubernetesUtils` class can be used. Example:
```
kts= KubernetesUtils()
nodes = kts.list_all_nodes()

    for node in nodes:
        res = kts.get_node_summary(node)
        volumes = kts.get_pvc_summary(res)

```
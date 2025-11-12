from kube import client, config

def list_pods(namespace='default'):
    # Load kubeconfig from ~/.kube/config
    config.load_kube_config()

    v1 = client.CoreV1Api()
    print(f"Listing pods in namespace: {namespace}")
    pods = v1.list_namespaced_pod(namespace)
    for pod in pods.items:
        print(f"{pod.metadata.name}\t{pod.status.phase}")

if __name__ == "__main__":
    list_pods("default")


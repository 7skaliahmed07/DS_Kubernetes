cat > README.md << 'EOF'
# Data Science Demo on Kubernetes

A minimal end-to-end example of deploying a FastAPI + pandas app on local Kubernetes (Minikube).

## Features
- FastAPI web server
- Loads Iris dataset and returns statistics
- Dockerized
- Deployed with Kubernetes Deployment (2 replicas)
- Exposed via Service + port-forward

## Quick Start
```bash
minikube start --driver=docker
minikube image load ds-k8s-demo:latest
kubectl apply -f deployment.yaml
kubectl expose deployment ds-demo --type=ClusterIP --port=8000 --target-port=8000
kubectl port-forward service/ds-demo 8000:8000
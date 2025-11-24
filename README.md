cat > README.md << 'EOF'
# Iris ML Inference API on Kubernetes

A complete MLOps demo: FastAPI + scikit-learn model trained inside the container, served on Kubernetes.

## Features
- Trains Logistic Regression on Iris dataset at container startup
- `/predict` endpoint for real-time inference
- Runs multiple replicas with automatic load balancing
- Fully Dockerized + Kubernetes Deployment + Service

## Test it
```bash
# Forward port (in one terminal)
kubectl port-forward service/ds-demo 8080:8000

# Then test
curl http://localhost:8080
curl -X POST http://localhost:8080/predict -H "Content-Type: application/json" -d '{"sepal_length":5.1,"sepal_width":3.5,"petal_length":1.4,"petal_width":0.2}'



What This Project Actually Does
- Trains a scikit-learn Logistic Regression model on the Iris dataset
- Serves real-time predictions via `/predict` (POST JSON)
- Runs inside Docker containers
- Deployed on real Kubernetes (Minikube) with:
  - Multiple replicas (load-balanced)
  - Auto-healing (crashed pod → instantly replaced)
  - Manual scaling (`kubectl scale`)
  - Real Horizontal Pod Autoscaler (HPA) → scales pods automatically when CPU > 50%
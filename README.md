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



### How This Actually Works (Explained Like You're 10)

1. I wrote a small ML app in Python (trains a model + answers "what flower is this?").

2. Docker = the box  
   I packed the app + Python + all libraries into one portable box (Docker image).

3. Pod = one running box  
   Each pod is just ONE copy of my app running inside the Kubernetes cluster.

4. Deployment = the manager  
   I told Kubernetes: "Please always keep 2 (or 5) copies of my app running."  
   → If one copy crashes → Kubernetes automatically starts a new one.  
   → If traffic is high → I can say "now run 10 copies" with one command.

5. Service = the front door  
   No matter how many copies (pods) are running behind the scenes, outsiders always call the SAME address (`localhost:8080`).  
   Kubernetes automatically spreads the requests across all healthy copies (load balancing).

Result:  
My tiny ML app is now indestructible and can grow/shrink automatically — exactly how Netflix, Google, Spotify run their apps.

From 1 copy → 5 copies in 2 seconds:
```bash
kubectl scale deployment ds-demo --replicas=5
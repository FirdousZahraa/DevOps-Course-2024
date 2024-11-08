# Knative 101: Simplifying Serverless on Kubernetes

**Knative** is an open-source platform that builds on Kubernetes to streamline serverless application deployment. It handles key infrastructure needs like scaling, routing, and networking, allowing developers to focus solely on writing code.

## What is Knative?

Knative offers a Kubernetes-native way to manage serverless workloads, helping teams build, deploy, and scale modern applications without managing the underlying infrastructure. Knative is built on two main components: **Serving** and **Eventing**.

### Key Components of Knative

#### 1. Knative Serving
Knative Serving manages the deployment and scaling of serverless applications. Key features include:
   - **Service**: Core deployment configuration for an app.
   - **Revision**: Tracks configuration versions.
   - **Route**: Routes traffic to specific revisions for easy rollouts and A/B testing.

#### 2. Knative Eventing
Knative Eventing enables event-driven applications, supporting a variety of event sources and linking them to your serverless applications. Key features include:
   - **Event Sources**: Integrate with various cloud providers or HTTP-based events.
   - **Brokers**: Central hubs for routing events.
   - **Triggers**: Link event sources to specific services.

### Why Use Knative?
Knative is highly beneficial for:
- **Simplified serverless deployment**: It abstracts complexities so developers can focus on coding.
- **Event-driven design**: Ideal for building responsive, event-driven applications.
- **Cost-efficient scaling**: Knative scales to zero when not in use, saving cloud costs.
- **Kubernetes-native integration**: Fits seamlessly into Kubernetes environments.

## Deploying a Simple Serverless Application on Knative

### Prerequisites
- A Kubernetes cluster (using Minikube, Google Kubernetes Engine, etc.).
- `kubectl` installed and configured.
- Knative installed on your Kubernetes cluster.

### Step-by-Step Guide

1. **Install Knative**:
   - **Install Knative Serving**:
     ```bash
     kubectl apply -f https://github.com/knative/serving/releases/download/knative-v1.9.0/serving-crds.yaml
     kubectl apply -f https://github.com/knative/serving/releases/download/knative-v1.9.0/serving-core.yaml
     ```
   - **Install a networking layer (e.g., Kourier)**:
     ```bash
     kubectl apply -f https://github.com/knative/net-kourier/releases/download/knative-v1.9.0/kourier.yaml
     ```
   - **Configure Knative to use Kourier**:
     ```bash
     kubectl patch configmap/config-network --namespace knative-serving --type merge --patch '{"data":{"ingress-class":"kourier.ingress.networking.knative.dev"}}'
     ```

2. **Create a Knative Service**:
   - Deploy a simple "Hello World" app with the following YAML configuration (`helloworld.yaml`):
     ```yaml
     apiVersion: serving.knative.dev/v1
     kind: Service
     metadata:
       name: helloworld
       namespace: default
     spec:
       template:
         spec:
           containers:
             - image: gcr.io/knative-samples/helloworld-go
               env:
                 - name: TARGET
                   value: "Knative"
     ```
   - Apply the service:
     ```bash
     kubectl apply -f helloworld.yaml
     ```

3. **Access the Application**:
   - Get the URL of the deployed service:
     ```bash
     kubectl get ksvc helloworld -o jsonpath='{.status.url}'
     ```
   - Access the service:
     ```bash
     curl $(kubectl get ksvc helloworld -o jsonpath='{.status.url}')
     ```
   - You should see the response: **Hello Knative!**

4. **Autoscaling and Scaling to Zero**:
   - Knative automatically scales applications up or down based on traffic, including scaling to zero when idle to save resources.
   - Monitor the pod status:
     ```bash
     kubectl get pods -l serving.knative.dev/service=helloworld
     ```

## Conclusion

Knative brings serverless to Kubernetes, enabling developers to focus on application development without worrying about scaling, networking, or infrastructure. With Knative Serving and Eventing, you can deploy, scale, and manage event-driven applications easily within a Kubernetes-native environment.

For a more detailed explanation, see the full blog post: https://medium.com/@firdouszahra/knative-101-simplifying-server-less-application-deployment-on-kubernetes-e142eb88d01b

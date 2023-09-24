**What is Kubernetes?**
Kubernetes (commonly stylized as k8s) is an open-source container orchestration system for automating application deployment, scaling, and management.
It is a portable, extensible platform for managing containerized applications and services.
It was originally developed and designed by Google and is now maintained by the Cloud Native Computing Foundation.

Many cloud services offer a Kubernetes-based platform or infrastructure as a service on which Kubernetes can be deployed as a platform-providing service.
Amazon Elastic Kubernetes Service (EKS)
Google Kubernetes Engine (GKE)
Azure Kubernetes Service (AKS)
Alibaba Cloud Container Service for Kubernetes (ACK)
CloudStack Kubernetes Service
OpenStack Kubernetes Service
IBM Cloud Kubernetes Service
DigitalOcean Managed Kubernetes
Baidu Cloud Container Engine
Oracle Container Engine for Kubernetes (OKE)
Also, many vendors provide their own branded Kubernetes distributions.

**Why do you need Kubernetes and what can it do?**
Kubernetes has a number of features. It can be thought of as:
a container platform
a micro-services platform
a portable cloud platform and a lot more.
Kubernetes provides a container-centric management environment.
It orchestrates computing, networking, and storage infrastructure on behalf of user workloads (applications running on Kubernetes).
Kubernetes orchestration allows your application services that span multiple containers, schedule those containers across a cluster, scale those containers, and manage the health of those containers over time.
Kubernetes defines a set of building blocks ("primitives"), which collectively provide mechanisms that deploy, maintain, and scale applications based on CPU, memory or custom metrics.
Kubernetes is loosely coupled and extensible to meet different workloads.

**Kubernetes Architecture**
Kubernetes follows a client-server architecture. A Kubernetes cluster consists of at least one master and multiple worker nodes.
It is also possible to have a multi-master setup for high availability, but by default, there is a single master node that acts as a controlling node and point of contact.
Other master nodes work as followers of the master node.
The master node components:
api server
etcd storage
controller-manager
scheduler
The worker node components:
container runtime (ex: docker)
kubelet
kube-proxy

![image](https://github.com/kunalshrivastavapune25/my-notes/assets/118747883/220d1da6-19d9-4116-8741-c89c49e7e2c1)


**Master Components**

**api server:**
It is the central management entity that receives all REST requests for modifications to pods, services, replication sets/controllers and others.
It serves as a frontend to the cluster.
This is the only component that communicates with the etcd cluster, making sure data is stored in etcd and is in agreement with the service details of the deployed pods.
Kubeconfig is a package along with server side tools that can be used for communication. It exposes Kubernetes API.

**etcd storage:**
It is an open source, highly available, distributed key value storage which is used to store the Kubernetes cluster data (such as number of pods, their state, namespace, etc), API objects and service discovery details.
It is accessible only by the Kubernetes API server for security reasons. etcd enables notifications to the cluster about configuration changes with the help of watchers.
Notifications are API requests on each etcd cluster node to trigger the update of information in the node's storage.

**controller-manager:**
It is responsible for most of the collectors that regulate the state of the cluster and perform a task (for example, the replication controller controls the number of replicas in a pod, and the endpoints controller populates endpoint objects like services and pods and others).
When a change in a service configuration occurs, the controller spots the change and starts working towards the new desired state.

**kube-scheduler:**
It is responsible for distributing (or scheduling) the workload on the various worker nodes based on resource utilization.
Worker Node Components

**container runtime (docker):**
The container runtime is responsible for running containers on the worker node.
It pulls images from a repository, provides resources, and manages the container lifecycle.

**kubelet:**
The kubelet is the primary "node agent" that runs on each node. It regularly takes new or modified specifications from the etcd through the API server and ensures that pods and their containers are healthy and running in the desired state.
It also reports to the master on the health of the worker node.

**kube-proxy:**
It is a proxy service that runs on each worker node and helps in making services available to the external host.
It performs request forwarding to the correct pods/containers across the various isolated networks in a cluster.
It manages pods on the node, volumes, secrets, creating new containers health checkups, etc.

**Command line interface**
kubectl is a command line interface that interacts with the API server and sends commands to the master node. Each command will convert into an API call.

**$ kubectl --help
kubectl controls the Kubernetes cluster manager.
Basic Commands (Beginner):
  create         Create a resource from a file or from stdin.
  expose         Take a replication controller, service, deployment or pod and expose it as a new Kubernetes Service
  run            Run a particular image on the cluster
  set            Set specific features on objects
**

**Workloads Overview**
A containerized application can deploy on Kubernetes using either "pods or workloads".

**Pods**
A pod is a smallest and simplest unit that you create or deploy in Kubernetes. A single pod has usually one, or multiple containers, and their shared resources.
A pod represents a single instance of an application in Kubernetes. You can scale pods by having multiple instances of the application.
Usually, pods get scaled and managed by the workloads.

**Workloads**
Workloads are controller objects that set deployment rules for pods.
These controller objects represent the applications, daemons, and batch jobs running on your cluster.
Based on the rules, Kubernetes performs application scheduling, scaling, and upgrade.

**Types of workloads**
Kubernetes divides workloads into different types. The most popular types supported by Kubernetes are:

**Deployments DaemonSets StatefulSets ReplicaSets Jobs CronJobs Deployments**

Deployments are best used for stateless applications. Pods managed by deployment workload are treated as independent and disposable.

If a pod encounters disruption, Kubernetes removes it and then recreates it.

**DaemonSets**
Daemonsets ensures that every node in the cluster runs a copy of the pod.
For use cases where you're collecting logs or monitoring node performance, this daemon-like workload works best.

**ReplicaSets**
A ReplicaSet's purpose is to run a specified number of pods at any given time.

**StatefulSets**
Like a Deployment , a StatefulSet manages Pods, are best used when your application needs to maintain its identity and store data.
An application would be something like Zookeeper - an application that requires a database for storage.

**Jobs**
Jobs launch one or more pods and ensure that a specified number of them successfully terminate.
Jobs are best used to run a finite task to completion as opposed to managing an ongoing desired application state.

**CronJobs**
CronJobs are similar to jobs. CronJobs, however, runs to completion on a cron-based schedule.




**Kubernetes Pods**
Pod is the basic building block of Kubernetes, the smallest deployable unit in the Kubernetes that can be created and managed.

Pod is a group of one or more containers (such as Docker containers) with shared storage/network, and a specification for how to run the containers.

A pod represents a single instance of an application in Kubernetes.

Here is manifest for a Pod:
```console
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:latest
    imagePullPolicy: IfNotPresent
    ports:
    - containerPort: 80
Create a pod:

$ kubectl create -f nginx.yaml
pod "nginx" created
Verify the pod is running:

$ kubectl get pod nginx
NAME        READY   STATUS    RESTARTS   AGE
nginx       1/1     Running   0          48s
Edit pod configuration:

$ kubectl edit pod nginx
Delete a pod

$ kubectl delete -f nginx.yaml
pod "nginx" deleted
        -- or --
$ kubectl delete pod nginx
pod "nginx" deleted

```

**Pod Lifecycle**
Pending

The Pod Has Been Accepted By The Kubernetes System, but one or more of the Container images has not been created. This includes time before being scheduled as well as time spent downloading images over the network, which could take a while.

Running

The Pod has been bound to a node, and all of the Containers have been created. At least one Container is still running, or is in the process of starting or restarting.

Succeeded

All Containers in the Pod have terminated in success, and will not be restarted.

Failed

All Containers in the Pod have terminated, and at least one Container has terminated in failure. That is, the Container either exited with non-zero status or was terminated by the system.

Unknown

For some reason the state of the Pod could not be obtained, typically due to an error in communicating with the host of the Pod.

Completed

The pod has run to completion as there is nothing to keep it running eg. Completed Jobs.

CrashLoopBackOff

This means that one of the containers in the pod has exited unexpectedly, and perhaps with a non-zero error code even after restarting due to restart policy.

Multi-Container Pods
Pods are designed to support multiple containers. The containers in a Pod are automatically co-located and co-scheduled on the same node in the cluster.

The containers can share resources and dependencies, communicate with one another, and coordinate when and how they are terminated.

The "one container per Pod" model is the most common use case and Kubernetes manages the Pods rather than the containers directly.

Here is example for multi-container pod

apiVersion: v1
kind: Pod
metadata:
  name: nginx-web
spec:
  volumes:
  - name: shared-files
    emptyDir: {}
  - name: nginx-config-volume
    configMap:
      name: nginx-config
  containers:
  - name: app
    image: php-app:1.0
    volumeMounts:
    - name: shared-files
      mountPath: /var/www/html
  - name: nginx
    image: nginx:latest
    volumeMounts:
    - name: shared-files
      mountPath: /var/www/html
    - name: nginx-config-volume
      mountPath: /etc/nginx/nginx.conf
      subPath: nginx.conf
Init Containers
Like multiple containers in a pod, it can also have one or more init containers, which are run before the application containers are started.

Init containers always run to completion.
Each init container must complete successfully before the next one starts.
Here is example for init containers

apiVersion: v1
kind: Pod
metadata:
  name: wordpress
spec:
  containers:
  - image: wordpress:latest
    name: wordpress
    ports:
    - containerPort: 80
      name: wordpress
  initContainers:
  - name: change-permissions
    image: busybox
    command: ['sh', '-c', 'chown www-data:www-data /var/www/html && chmod -R 755 /var/www/html']







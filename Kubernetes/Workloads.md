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

**Deployments**

DaemonSets
StatefulSets
ReplicaSets
Jobs
CronJobs
Deployments

Deployments are best used for stateless applications. Pods managed by deployment workload are treated as independent and disposable.

If a pod encounters disruption, Kubernetes removes it and then recreates it.

DaemonSets

Daemonsets ensures that every node in the cluster runs a copy of the pod.

For use cases where you're collecting logs or monitoring node performance, this daemon-like workload works best.

ReplicaSets

A ReplicaSet's purpose is to run a specified number of pods at any given time.

StatefulSets

Like a Deployment , a StatefulSet manages Pods, are best used when your application needs to maintain its identity and store data.

An application would be something like Zookeeper - an application that requires a database for storage.

Jobs

Jobs launch one or more pods and ensure that a specified number of them successfully terminate.

Jobs are best used to run a finite task to completion as opposed to managing an ongoing desired application state.

CronJobs

CronJobs are similar to jobs. CronJobs, however, runs to completion on a cron-based schedule.






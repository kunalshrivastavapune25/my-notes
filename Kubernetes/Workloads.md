**Q1 How are containerized application can be deployed on Kubernetes?**\
Ans: **Workloads Overview** : A containerized application can deploy on Kubernetes using either **"pods or workloads"**.

**Q2 What are Pods?**\
**Ans** : A pod is a smallest and simplest unit that you create or deploy in Kubernetes. A single pod has usually one, or multiple containers, and their shared resources.A pod represents a single instance of an application in Kubernetes. You can scale pods by having multiple instances of the application.Usually, pods get scaled and managed by the workloads.
Pod is the basic building block of Kubernetes, the smallest deployable unit in the Kubernetes that can be created and managed.
Pod is a group of one or more containers (such as Docker containers) with shared storage/network, and a specification for how to run the containers.A pod represents a single instance of an application in Kubernetes.
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
```

**Q3 Create a pod?**\
**Ans** :
```console
$ kubectl create -f nginx.yaml
pod "nginx" created
```

**Q4 Verify the pod is running?**\
**Ans** :
```console
$ kubectl get pod nginx
NAME        READY   STATUS    RESTARTS   AGE
nginx       1/1     Running   0          48s
```

**Q5 Edit pod configuration?**\
**Ans** :
```console
$ kubectl edit pod nginx
```

**Q6 Delete a pod?**\
**Ans** :
```console
$ kubectl delete -f nginx.yaml
pod "nginx" deleted
        -- or --
$ kubectl delete pod nginx
pod "nginx" deleted

```


**Q7 What are Pods Lifecycle?**\
**Ans** :\
Pending: The Pod Has Been Accepted By The Kubernetes System, but one or more of the Container images has not been created. This includes time before being scheduled as well as time spent downloading images over the network, which could take a while.\
Running: The Pod has been bound to a node, and all of the Containers have been created. At least one Container is still running, or is in the process of starting or restarting. \
Succeeded: All Containers in the Pod have terminated in success, and will not be restarted.\
Failed: All Containers in the Pod have terminated, and at least one Container has terminated in failure. That is, the Container either exited with non-zero status or was terminated by the system. \
Unknown : For some reason the state of the Pod could not be obtained, typically due to an error in communicating with the host of the Pod. \
Completed : The pod has run to completion as there is nothing to keep it running eg. Completed Jobs. \
CrashLoopBackOff : This means that one of the containers in the pod has exited unexpectedly, and perhaps with a non-zero error code even after restarting due to restart policy. \

**Q8 What are Multi-Container Pods?**\
**Ans** :\
Pods are designed to support multiple containers. The containers in a Pod are automatically co-located and co-scheduled on the same node in the cluster.
The containers can share resources and dependencies, communicate with one another, and coordinate when and how they are terminated.
The "one container per Pod" model is the most common use case and Kubernetes manages the Pods rather than the containers directly.
Here is example for multi-container pod

```console
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
```
**Q8 What are Init Containers?**\
**Ans** :\
Like multiple containers in a pod, it can also have one or more init containers, which are run before the application containers are started.
Init containers always run to completion.
Each init container must complete successfully before the next one starts.
Here is example for init containers
```console
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
```

**Q9 What are Workloads?**\
Ans:**Workloads** -Workloads are controller objects that set deployment rules for pods.These controller objects represent the applications, daemons, and batch jobs running on your cluster.Based on the rules, Kubernetes performs application scheduling, scaling, and upgrade.\
**Types of workloads**\
**Deployments** : are best used for stateless applications. Pods managed by deployment workload are treated as independent and disposable.If a pod encounters disruption, Kubernetes removes it and then recreates it.\
**DaemonSets** :     Daemonsets ensures that every node in the cluster runs a copy of the pod. For use cases where you're collecting logs or monitoring node performance, this daemon-like workload works best.\
**ReplicaSets** : A ReplicaSet's purpose is to run a specified number of pods at any given time.\
**StatefulSets** : Like a Deployment , a StatefulSet manages Pods, are best used when your application needs to maintain its identity and store data.An application would be something like Zookeeper - an application that requires a database for storage.\
**Jobs** : Jobs launch one or more pods and ensure that a specified number of them successfully terminate. Jobs are best used to run a finite task to completion as opposed to managing an ongoing desired application state.\
**CronJobs** : CronJobs are similar to jobs. CronJobs, however, runs to completion on a cron-based schedule.\


**Q10 What are Deployments?**\
Ans: Deployment controller provides declarative updates for Pods and it manage stateless applications running on your cluster.
Deployments represent a set of multiple, identical Pods and upgrade them in a controlled way, performing a rolling update by default. A Deployment runs multiple replicas of your application and automatically replaces any instances that fail or become unresponsive.
In this way, Deployments ensure that one or more instances of your application are available to serve user requests.


**Q11 How to Create a deployment?**\
**Ans** :\
```console
$ kubectl create -f nginx-deployment.yaml
deployment.apps "nginx-deployment" created
```

**Q8 How to Display your deployments?**\
**Ans** :\
```console
$ kubectl get deployments
NAME             DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
nginx-deployment 3         3         3            3           2m
```

**Q8 How to Get details of a deployment?**\
**Ans** :\
```console
$ kubectl describe deployment nginx-deployment
$ kubectl get pods
NAME                                READY     STATUS    RESTARTS   AGE
nginx-deployment-6cf94d8d7c-7bfpt   1/1       Running   0          3m
nginx-deployment-6cf94d8d7c-9mqkv   1/1       Running   0          3m
nginx-deployment-6cf94d8d7c-xnbnl   1/1       Running   0          3m
```

**Q8 How to Check status of the deployment?**\
**Ans** :\
```console
$ kubectl rollout status deployment/nginx-deployment
deployment "nginx-deployment" successfully rolled out
```

**Q8 How to Update the deployment?**\
**Ans** :\
```console
$ kubectl set image deployment/nginx-deployment nginx=nginx:latest
deployment.apps "nginx-deployment" image updated
```

**Q8 How to Rollback to previous revision?**\
**Ans** :\
```console
$ kubectl rollout undo deployment/nginx-deployment
deployment.apps "nginx-deployment"

$ kubectl rollout status deployment/nginx-deployment
deployment "nginx-deployment" successfully rolled out
```

**Q8 How to Check Rollout history?**\
**Ans** :\
```console
$ kubectl rollout history deployment/nginx-deployment
deployments "nginx-deployment"
REVISION  CHANGE-CAUSE
2         < none >
3         < none >
```

**Q8 How to Scale a deployment?**\
**Ans** :\
```console
$ kubectl scale deployment/nginx-deployment --replicas=5
deployment.apps "nginx-deployment" scaled

$ kubectl get pods
NAME                               READY     STATUS    RESTARTS   AGE
nginx-deployment-6cf94d8d7c-98mps  1/1       Running   0          12m
nginx-deployment-6cf94d8d7c-hnhvl  1/1       Running   0          12m
nginx-deployment-6cf94d8d7c-kpzxq  1/1       Running   0          8s
nginx-deployment-6cf94d8d7c-kvtj9  1/1       Running   0          8s
nginx-deployment-6cf94d8d7c-pg7n8  1/1       Running   0          12m
```


**Q8 How to Edit a deployment?**\
**Ans** :\
```console
$ kubectl edit deployment nginx-deployment
```

**Q8 How to Delete a deployment?**\
**Ans** :\
```console
$ kubectl delete deployment nginx-deployment
```

**Q8 How to Writing a Deployment Spec?**\
**Ans** :\
A Deployment manifest needs \
apiVersion  \
kind \
metadata : The metadata field have name, labels, annotations and other information \
spec :The spec field have replicas, deployment strategy, pod template, selector and other details \
 
**Pod Template** \ 
The spec.template is the only required field of the .spec.\
The spec.template is a pod template. It has exactly the same schema as a Pod, except it is nested and does not have an apiVersion or kind.\
```console
 spec:
  template:
    metadata:
      labels:
        app: frontend
```
**Restart Policy** \
Only a spec.template.spec.restartPolicy equal to Always is allowed, which is the default if not specified.
```console
 spec:
  template:
    metadata:
      labels:
        app: frontend
    spec:
      restartPolicy : Always
      containers:
```
**Replicas** \
spec.replicas is an optional field that specifies the number of desired Pods. It defaults to 1.
```console
 spec:
    replicas: 3
```
**Selector** \
spec.selector is an optional field that specifies a label selector for the Pods targeted by this deployment.
```console
  spec:
    replicas: 3
    selector:
      matchLabels:
        app: fronted
```
spec.selector must match .spec.template .metadata.labels, or it will be rejected by the API.
```console
 spec:
  replicas: 3
  selector:
    matchLabels:
      app: fronted
  template:
    metadata:
      labels:
        app: fronted
```console
**Strategy** \
spec.strategy specifies the strategy used to replace old Pods by new ones. spec.strategy.type can be "Recreate" or "RollingUpdate". "RollingUpdate" is the default value.
```console
 spec:
  replicas: 3
  strategy:
    type: RollingUpdate
```

**Deployment Failure**\
Your Deployment may get stuck trying to deploy its newest ReplicaSet without ever completing.\

This can occur due to some of the following factors:\

Insufficient quota\
Readiness probe failures\
Image pull errors\
Insufficient permissions\
Limit ranges\
Application run-time misconfiguration\







**Q5 What are StatefulSets?**\
Ans: StatefulSets represent a set of Pods with unique, persistent identities and stable hostnames. It provides guarantees about the ordering of deployment and scaling.

StatefulSets are valuable for applications that require one or more of the following:

Stable, unique network identifiers
Stable, persistent storage
Ordered, graceful deployment and scaling
Ordered, graceful deletion and termination
If an application doesn't require any stable identifiers or ordered deployment, deletion, or scaling, you should deploy your application with a controller such as Deployments or ReplicaSets that provides a set of stateless replicas.

StatefulSet Components

A Headless Service
A StatefulSet
A PersistentVolume

Below are manifests of a Service, StatefulSet and Persistent volume:

apiVersion: v1
kind: Service
metadata:
  name: nginx
  labels:
    app: nginx
spec:
  ports:
  - port: 80
    name: web
  clusterIP: None
  selector:
    app: nginx

---
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: web
spec:
  selector:
    matchLabels:
      app: nginx
  serviceName: "nginx"
  replicas: 3
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx
        ports:
        - containerPort: 80
          name: web
        volumeMounts:
        - name: www
          mountPath: /usr/share/nginx/html
      volumes:
      - name: www
        persistentVolumeClaim:
          claimName: myclaim

---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: myclaim
spec:
  accessModes:
    - ReadWriteMany
  resources:
    requests:
      storage: 8Gi
Create and manage StatefulSets
Create a statefulset

$ kubectl create -f statefulset.yaml
service "nginx" created
statefulset.apps "web" created
It will create three Pods named web-0,web-1,web-2

$ kubectl get pods
NAME      READY     STATUS    RESTARTS   AGE
web-0     1/1       Running   0          1m
web-1     1/1       Running   0          46s
web-2     1/1       Running   0          18s

$ kubectl get svc nginx
NAME      TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
nginx     ClusterIP   None         < none >      80/TCP    2m
List your statefulsets:

$ kubectl get statefulsets
Get details of a statefulset:

$ kubectl describe statefulset web
Edit a statefulset:

$ kubectl edit statefulset web
Scaling a statefulset:

Scaling a StatefulSet refers to increasing or decreasing the number of replicas.

Scale up a statefulset:

$ kubectl scale statefulset web --replicas=5
statefulset.apps "web" scaled

kubectl get pods -l app=nginx
NAME      READY     STATUS    RESTARTS   AGE
web-0     1/1       Running   0          11m
web-1     1/1       Running   0          10m
web-2     1/1       Running   0          10m
web-3     1/1       Running   0          33s
web-4     1/1       Running   0          19s
Scale down a statefulset:

kubectl scale statefulset web --replicas=2
statefulset.apps "web" scaled

$ kubectl get pods -w -l app=nginx
NAME      READY     STATUS        RESTARTS   AGE
web-0     1/1       Running       0          13m
web-1     1/1       Running       0          12m
web-2     0/1       Terminating   0          12m
web-3     0/1       Terminating   0          2m
web-4     0/1       Terminating   0          1m

$ kubectl get pods -l app=nginx
NAME      READY     STATUS    RESTARTS   AGE
web-0     1/1       Running   0          13m
web-1     1/1       Running   0          12m
Delete a statefulset

$ kubectl delete statefulset web
statefulset.apps "web" deleted
You must delete the Service manually.

$ kubectl delete service nginx
service "nginx" deleted
Limitations:
StatefulSet was a beta resource prior to 1.9 and not available in any Kubernetes release prior to 1.5.

The storage for a given Pod must either be provisioned by a PersistentVolume Provisioner based on the requested storage class, or pre-provisioned by an admin.

Deleting and/or scaling a StatefulSet down will not delete the volumes associated with the StatefulSet. This is done to ensure data safety, which is generally more valuable than an automatic purge of all related StatefulSet resources.

StatefulSets currently require a Headless Service to be responsible for the network identity of the Pods. You are responsible for creating this Service.

StatefulSets do not provide any guarantees on the termination of pods when a StatefulSet is deleted. To achieve ordered and graceful termination of the pods in the StatefulSet, it is possible to scale the StatefulSet down to 0 prior to deletion.


**Q6 What are ReplicaSets?**\
Ans:A ReplicaSet's purpose is to run a specified number of pods at any given time.


While ReplicaSets can be used independently, today it's mainly used by Deployments as a mechanism to orchestrate pod creation, deletion, and updates.

When you use Deployments, you don't have to worry about managing the ReplicaSets that they create.


Therefore, we recommend using Deployments instead of directly using ReplicaSets, unless you require custom update orchestration or don't require updates at all.

Here is the manifest of ReplicaSets

apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: webapp
  labels:
    app: webapp
    tier: frontend
spec:
  replicas: 3
  selector:
    matchLabels:
      tier: frontend
  template:
    metadata:
      labels:
        tier: frontend
    spec:
      containers:
      - name: webapp
        image: webapp:2.0

Create a replicaset:

$ kubectl apply -f replicaSet.yaml
replicaset.apps "webapp" created

$ kubectl get rs
NAME      DESIRED   CURRENT   READY     AGE
webapp    3         3         3         49s

$ kubectl get pods
NAME           READY     STATUS    RESTARTS   AGE
webapp-jcs7v   1/1       Running   0          32s
webapp-kpl9h   1/1       Running   0          32s
webapp-rxwr5   1/1       Running   0          32s
Display your replicasets:

$ kubectl get replicasets
Get details of a replicaset:

$ kubectl describe replicaset webapp
Edit a replicaset:

$ kubectl edit replicaset webapp
Scale a replicaset:

$ kubectl scale  --replicas=5 rs webapp
replicaset.apps "webapp" scaled

$ kubectl get pods
NAME           READY     STATUS    RESTARTS   AGE
webapp-96klr   1/1       Running   0          8s
webapp-d5hv5   1/1       Running   0          8s
webapp-jcs7v   1/1       Running   0          5m
webapp-kpl9h   1/1       Running   0          5m
webapp-rxwr5   1/1       Running   0          5m
Delete a replicaset:

$ kubectl delete replicaset/webapp
replicaset.apps "webapp" deleted
You can delete a ReplicaSet without affecting any of its Pods using kubectl delete with the --cascade=false option.

$ kubectl delete replicaset/webapp --cascade=false




**Q7 What are Jobs?**\
Ans:You might also need to run large computation or batch processing workloads in your clusters. For this, Job controller is useful.

A job creates one or more pods running in parallel. You can specify how many number of pods need to complete in this Job.

When a specified number of pods successfully completed, the job itself is complete.

If the first pod fails or is deleted, the Job controller will start a new Pod.

The job is designed for parallel processing of independent but related work items like sending emails, rendering frames, transcoding files, scanning database keys, etc..

Here is the manifest for a Job:

apiVersion: batch/v1
kind: Job
metadata:
  name: example-job
spec:
  template:
    metadata:
      name: example-job
    spec:
      containers:
      - name: pi
        image: perl
        command: ["perl"]
        args: ["-Mbignum=bpi", "-wle", "print bpi(2000)"]
      restartPolicy: Never

Create a Job:

$ kubectl apply -f example-job.yaml
job.batch "example-job" created
Display your jobs:

$ kubectl get jobs
NAME          DESIRED   SUCCESSFUL   AGE
example-job   1         0            33s

$ kubectl get pods --watch
NAME                READY     STATUS              RESTARTS   AGE
example-job-pzxhn   0/1       ContainerCreating   0          23s
example-job-pzxhn   0/1       Completed           0          51s

$ kubectl get jobs:
NAME          DESIRED   SUCCESSFUL   AGE
example-job   1         1            1m
Get details of a job:

$ kubectl describe job example-job
Edit a job:

$ kubectl edit job example-job
Delete a job:

$ kubectl delete job example-job
job.batch "example-job" deleted


Read more about Jobs
Cron Jobs
A Cron Job creates Jobs on a time-based schedule.

A CronJob object is just like an entry in crontab in Unix/Linux. It runs a job periodically on a given schedule.

You need a working Kubernetes cluster at version >= 1.8 (for CronJob).

For previous versions of the cluster (< 1.8) you need to explicitly enable batch/v2alpha1 API by passing --runtime-config=batch/v2alpha1=true to the API server.

Here is the manifest for Cronjob

apiVersion: batch/v1beta1
kind: CronJob
metadata:
  name: hello
spec:
  schedule: "*/1 * * * *"
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: hello
            image: busybox
            args:
            - /bin/sh
            - -c
            - date; echo Hello from the Kubernetes cluster
          restartPolicy: OnFailure


Jobs
Create a Cron Job:

$ kubectl create -f cronjob.yaml
cronjob.batch "hello" created

$ kubectl get cronjobs hello
NAME      SCHEDULE      SUSPEND   ACTIVE    LAST SCHEDULE   AGE
hello     */1 * * * *   False     0         < none >        28s

$ kubectl get jobs --watch
NAME               DESIRED   SUCCESSFUL   AGE
hello-1550406120   1         1            35s
hello-1550406180   1         0         0s
hello-1550406180   1         0         0s
hello-1550406180   1         1         2s
hello-1550406240   1         0         0s
hello-1550406240   1         0         0s
hello-1550406240   1         1         1s
hello-1550406300   1         0         0s
hello-1550406300   1         0         0s
hello-1550406300   1         1         1s
hello-1550406120   1         1         3m
Get details of a cronjob:

$ kubectl describe cronjob hello
Edit a cronjob:

$ kubectl edit cronjob hello
Delete a cronjob:

$ kubectl delete cronjob hello
Writing a Cron Job Spec

As with all other Kubernetes configs, a cron job needs apiVersion, kind, and metadata fields.

Schedule

The .spec.schedule is a required field of the .spec. It takes a Cron format string, such as 0 * * * * or @hourly, as schedule time of its jobs to be created and executed.





Stateless vs StatefulSet\
A stateless application doesn't manage its state in the Kubernetes cluster. All of the states are stored outside the cluster and the cluster containers access it in some manner.

A stateful application can remember at least some things about its state each time that it runs. The actual state data that it stores may depend on the application and on the conditions under which it operates.

Here, "State" refers to any changeable condition, including the results of internal operations, interactions with other applications or services, environment variables, the contents of memory or temporary storage, or files opened, read from, or written to.

Deployments and ReplicaSets are meant for stateless usage and are rather lightweight.

StatefulSets are used when the state has to be persisted. Therefore the latter use volumeClaimTemplates / claims on persistent volumes to ensure they can keep the state across component restarts.

So if your application is stateful or if you want to deploy stateful storage on top of Kubernetes use a StatefulSet.

If your application is stateless or if the state can be built up from backend-systems during the start then use Deployments.

Stateless\

No Persistent Storage
Scaling can be done independently
Mortal
Stateful

Stable, unique network identifiers
Stable, persistent storage
Ordered, graceful deployment and scaling
Ordered, graceful deletion and termination




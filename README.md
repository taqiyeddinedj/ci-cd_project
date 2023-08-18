# My First CI/CD Pipeline with JENKINS!
## Project Scope and Tools Used:
This project centers around a comprehensive CI/CD pipeline, showcasing the integration of popular tools that are widely utilized in the field.
## GitHub Repository Overview:
When you take a look at my GitHub repository, you'll notice several key files that play a crucial role in this pipeline's functionality.
```
project-root/
├── templates/
│   └── index.html
├── Dockerfile
├── app.py
├── Jenkinsfile
├── deployment-service.yml
├── script.groovy
├── .gitignore
└── requirements.txt
```
The repository contains files such as 'app.py,' which is a Flask web application."
You can run it locally, 
```bash
python3 app.py
```
## Docker Image Creation:
To build the application image, I leverage a Dockerfile.
```
FROM python:3.7-alpine
COPY . /app
WORKDIR /app 
RUN pip install flask
CMD ["python", "app.py"]
```
![image](https://github.com/taqiyeddinedj/ci-cd_project/assets/112349513/3e6563fa-4d17-4e18-8579-5d423899fbe1)
  Check my docker hub repo at: https://hub.docker.com/repository/docker/taqiyeddinedj/my-repo
  
In the deployment stage of our CI/CD pipeline, I've crafted a Kubernetes Deployment configuration file, deployment.yml
which defines the specifications for our application's deployment
The accompanying Service configuration file, service.yml, defines how our application can be accessed

## Jenkins Setup and Building Triggers:
![image](https://github.com/taqiyeddinedj/ci-cd_project/assets/112349513/7d0e6e7a-af08-4def-96e9-6797f2a8a64c)
Inside the Jenkins container, I've included the Docker runtime, enabling it to build Docker images directly.
![image](https://github.com/taqiyeddinedj/ci-cd_project/assets/112349513/d135b954-3ce8-4189-8453-11456598067e)
Using a webhook, any push to the repository automatically triggers the build process.

## Pipeline Stages:
The pipeline consists of several distinct stages, each serving a specific purpose.
![image](https://github.com/taqiyeddinedj/ci-cd_project/assets/112349513/044773bc-5dea-4be8-8ccf-25c6693d2257)

These stages include initialization, testing (which identifies the active branch), building and pushing to Docker Hub, and the final deployment to a Kubernetes cluster.
## Jenkins File and Groovy Syntax:
The pipeline is orchestrated using a Jenkinsfile, written in Groovy syntax.


## Setting up Your Own Kubernetes Cluster:
Establishing my personal Kubernetes cluster quite challenging, but i made it work."
Troubleshooting was a significant aspect of getting the cluster operational.

![image](https://github.com/taqiyeddinedj/ci-cd_project/assets/112349513/a23f6ac1-c96b-49cf-84ed-3de4b60fc50f)


## Integration of Kubernetes with Jenkins:
Connecting Kubernetes with Jenkins was a critical step. I discovered a helpful plugin on Stack Overflow, conveniently provided by the Jenkins community.
[stackoverflow-plugin](https://stackoverflow.com/questions/71084850/jenkins-pipeline-to-deploy-on-kubernetes#:~:text=Download%20Kubernetes%20Continuous%20Plugin%201.0.0%20version%20from%20https%3A%2F%2Fupdates.jenkins.io%2Fdownload%2Fplugins%2Fkubernetes-cd%2F1.0.0%2Fkubernetes-cd.hpi,%22Deploy%22%20button%20as%20shown%20below%3A%20Then%20run%20manually%3A)

An obstacle I encountered was a certificate signing issue, likely related to port forwarding. This led me to seek a cluster accessible from the public network.

## Transition to Azure and Deploying a Cluster**:
To address these challenges, I migrated to Microsoft Azure and successfully deployed a Kubernetes cluster.
![image](https://github.com/taqiyeddinedj/ci-cd_project/assets/112349513/cb89532b-5891-4b6c-835e-e48af6a5db9b)

There's a specific command that needs to be included in the Jenkinsfile for this Azure-based cluster setup.
```bash
kubernetesDeploy (configs: 'deployment-service.yml', kubeconfigId: 'kubernetes')
```
To ensure seamless connectivity, the kubeconfig file is stored in a hidden directory (.kube) within your home directory, and its contents are uploaded to Jenkins as special credentials.

## Azure Cluster Status: 
Currently, the Azure-based Kubernetes cluster is up and running, serving as the backbone of our robust CI/CD pipeline." 

## Conclusion and Summary:
In summary, i have taken you through the intricate process of establishing a comprehensive CI/CD pipeline. From the initial setup of Jenkins and Docker, to overcoming Kubernetes integration challenges, and finally transitioning to a reliable Azure-based cluster, we've covered a wealth of insights and practical steps.


def buildDockerImage() {
    echo "Building the docker image...."
    withCredentials([usernamePassword(credentialsId:'dockr-hub-repo', passwordVariable: 'PASS', usernameVariable: 'USER')]){
        sh "docker build -t taqiyeddinedj/my-repo:webapp-1.0 ."
        sh " echo $PASS | docker login -u $USER --password-stdin"
        sh "docker push taqiyeddinedj/my-repo:webapp-1.0"
    }
}

def deploytok8s() {
    echo "Deploying now the apllication on the kubernetes cluster"
    kubernetesDeploy (configs: 'deployment-service.yml', kubeconfigId: 'kubeconfig')
}

return this
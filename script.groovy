def buildDockerImage() {
    echo "Building the docker image...."
    withCredentials([usernamePassword(credentialsId:'dockr-hub-repo', passwordVariable: 'PASS', usernameVariable: 'USER')]){
        sh "docker build -t taqiyeddinedj/ci_cd_pipline:web-app:1.0"
    }
}
def pushtoHub() {
    sh "echo $PASS | docker login -u $USER --passwd-stdin"
    sh "docker push taqiyeddinedj/ci_cd_pipline:web-app:1.0"
}

def deploytok8s() {
    echo "Deploying now the apllication on the kubernetes cluster"
    kubernetesDeploy (configs: 'deployment-service.yml', kubeconfigId: 'kubeconfig')
}

return this
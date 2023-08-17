#!/usr/bin/env groovy
def gv

pipeline {
    agent any
    stages {
        stage('Init') {
            steps {
                script {
                    gv = load "script.groovy"
                }
            }
        }

        stage('test') {
            steps {
                script {
                    echo "Testing the application"
                    echo "Executing pipeline for branch $BRANCH_NAME"
                }
            }
        }

        stage ('Build'){
            steps {
                script {
                    echo "Building the docker image...."
                    withCredentials([usernamePassword(credentialsId:'dockr-hub-repo', passwordVariable: 'PASS', usernameVariable: 'USER')]){
                        sh "docker build -t taqiyeddinedj/ci_cd_pipline:web-app:1.0"
    }
                    
                }
            }
        }

        stage ('Pushing to dockerhub'){
            steps {
                script {
                    sh "echo $PASS | docker login -u $USER --passwd-stdin"
                    sh "docker push taqiyeddinedj/ci_cd_pipline:web-app:1.0"
                    
                }
            }
        }

        stage ('Deploy to K8S'){
            steps {
                script {
                    echo "Deploying now the apllication on the kubernetes cluster"
                    kubernetesDeploy (configs: 'deployment-service.yml', kubeconfigId: 'kubeconfig')
                    
                }
            }
        }
    }
}

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
                    buildDockerImage()
                    
                }
            }
        }

        stage ('Pushing to dockerhub'){
            steps {
                script {
                    pushtoHub()
                    
                }
            }
        }

        stage ('Deploy to K8S'){
            steps {
                script {
                    deploytok8s()
                    
                }
            }
        }
    }
}
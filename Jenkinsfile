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
                    gv.buildDockerImage()
                    
                }
            }
        }

        stage ('Pushing to dockerhub'){
            steps {
                script {
                    gv.pushtoHub()
                    
                }
            }
        }

        stage ('Deploy to K8S'){
            steps {
                script {
                    gv.deploytok8s()
                    
                }
            }
        }
    }
}
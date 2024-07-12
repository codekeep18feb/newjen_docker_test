pipeline {
    agent any

    environment {
        DOCKER_COMPOSE = '/usr/local/bin/docker-compose'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your-username/your-repo.git'
            }
        }

        stage('Build') {
            steps {
                sh '${DOCKER_COMPOSE} build'
            }
        }

        stage('Test') {
            steps {
                sh '${DOCKER_COMPOSE} run --rm web pytest'
            }
        }

        stage('Deploy') {
            steps {
                sh '${DOCKER_COMPOSE} up -d'
            }
        }
    }

    post {
        always {
            sh '${DOCKER_COMPOSE} down'
        }
    }
}

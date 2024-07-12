pipeline {
    agent any

    environment {
            PATH = "/usr/bin:/usr/local/bin:$PATH"
        }
        
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/codekeep18feb/newjen_docker_test.git'
            }
        }

        stage('Build') {
            steps {
                sh 'docker-compose build'
            }
        }

        stage('Test') {
            steps {
                sh 'docker-compose run --rm web pytest'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }

    post {
        always {
            sh 'docker-compose down'
        }
    }
}

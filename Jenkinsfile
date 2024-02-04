pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = credentials('godfrey-docker-hub-id')
    }

    stages {
        stage('Build Flask App') {
            steps {
                script {
                    docker.build("godfrey22152/profile_application", "-f Dockerfile .")
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'godfrey-docker-hub-id') {
                        docker.image("godfrey22152/profile_application").push()
                    }
                }
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                script {
                    sh 'docker-compose up -d'
                }
            }
        }
    }

    post {
        always {
            // Clean up (optional)
            script {
                sh 'docker-compose down'
            }
        }
    }
}

pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout code from Git repository
                git branch: 'main', url: 'https://github.com/alielesawy/python-flask.git'
            }
        }
        
        stage('Build') {
            steps {
                // Install dependencies
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Test') {
            steps {
                // Run tests
                sh 'pip install pytest'
                sh 'pytest test_app.py'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                // Build Docker image
                sh 'docker build -t flask-jenkins-test:latest .'
            }
        }
        
        stage('Run Container') {
            steps {
                // Run the container (for testing)
                sh 'docker run -d -p 5000:5000 --name flask_test flask-jenkins-test:latest'
            }
        }
    }
    
    post {
        always {
            // Clean up: stop and remove the container
            sh 'docker stop flask_test || true'
            sh 'docker rm flask_test || true'
        }
        success {
            echo 'Build and tests completed successfully!'
        }
        failure {
            echo 'Build or tests failed!'
        }
    }
}
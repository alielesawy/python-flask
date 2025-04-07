pipeline {
    agent any
    
    environment {
        // Add Jenkins user's local bin directory to PATH
        PATH = "/var/lib/jenkins/.local/bin:${env.PATH}"
    }
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/alielesawy/python-flask.git'
            }
        }
        
        stage('Build') {
            steps {
                sh 'pip install --break-system-packages -r requirements.txt'
            }
        }
        
        stage('Test') {
            steps {
                sh 'pip install --break-system-packages pytest'
                sh 'pytest test_app.py'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-jenkins-test:latest .'
            }
        }
        
        stage('Run Container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name flask_test flask-jenkins-test:latest'
            }
        }
    }
    
    post {
        always {
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
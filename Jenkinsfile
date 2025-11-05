pipeline {
    agent any
    
    stages {
        stage('Install dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }
        
        stage('Run tests with coverage') {
            steps {
                sh './venv/bin/pytest --junitxml=report.xml --cov=. --cov-report=html --cov-report=term || true'
            }
        }
        
        stage('Publish Report') {
            steps {
                junit 'report.xml'
                publishHTML([
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'htmlcov',
                    reportFiles: 'index.html',
                    reportName: 'Coverage Report'
                ])
            }
        }
    }
}
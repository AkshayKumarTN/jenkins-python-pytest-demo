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
    
    post {
        failure {
            emailext (
                subject: "❌ Build Failed: ${env.JOB_NAME} - Build #${env.BUILD_NUMBER}",
                body: """
                    <h2>Build Failed!</h2>
                    <p><strong>Job:</strong> ${env.JOB_NAME}</p>
                    <p><strong>Build Number:</strong> ${env.BUILD_NUMBER}</p>
                    <p><strong>Build URL:</strong> <a href="${env.BUILD_URL}">${env.BUILD_URL}</a></p>
                    <p><strong>Console Output:</strong> <a href="${env.BUILD_URL}console">View Console</a></p>
                    <p>Please check the console output for details.</p>
                """,
                to: "atalurna@stevens.edu",
                mimeType: 'text/html'
            )
        }
        unstable {
            emailext (
                subject: "⚠️ Build Unstable: ${env.JOB_NAME} - Build #${env.BUILD_NUMBER}",
                body: """
                    <h2>Build Unstable - Tests Failed!</h2>
                    <p><strong>Job:</strong> ${env.JOB_NAME}</p>
                    <p><strong>Build Number:</strong> ${env.BUILD_NUMBER}</p>
                    <p><strong>Build URL:</strong> <a href="${env.BUILD_URL}">${env.BUILD_URL}</a></p>
                    <p><strong>Test Results:</strong> <a href="${env.BUILD_URL}testReport/">View Test Report</a></p>
                    <p><strong>Coverage Report:</strong> <a href="${env.BUILD_URL}Coverage_20Report/">View Coverage</a></p>
                    <p>Some tests failed. Please review the test report.</p>
                """,
                to: "atalurna@stevens.edu",
                mimeType: 'text/html'
            )
        }
        success {
            emailext (
                subject: "✅ Build Successful: ${env.JOB_NAME} - Build #${env.BUILD_NUMBER}",
                body: """
                    <h2>Build Successful!</h2>
                    <p><strong>Job:</strong> ${env.JOB_NAME}</p>
                    <p><strong>Build Number:</strong> ${env.BUILD_NUMBER}</p>
                    <p><strong>Build URL:</strong> <a href="${env.BUILD_URL}">${env.BUILD_URL}</a></p>
                    <p><strong>Test Results:</strong> <a href="${env.BUILD_URL}testReport/">View Test Report</a></p>
                    <p><strong>Coverage Report:</strong> <a href="${env.BUILD_URL}Coverage_20Report/">View Coverage</a></p>
                    <p>All tests passed successfully! ✅</p>
                """,
                to: "atalurna@stevens.edu",
                mimeType: 'text/html'
            )
        }
    }
}
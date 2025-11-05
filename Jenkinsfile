pipeline {
    agent any
    
    stages {
        stage('Install dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }
        
        stage('Run tests') {
            steps {
                sh './venv/bin/pytest --junitxml=report.xml'
            }
        }
        
        stage('Publish Report') {
            steps {
                junit 'report.xml'
            }
        }
    }
}
```

3. Save (Ctrl + S)

---

### Step 3: Your Project Structure Should Look Like This
```
jenkins-python-pytest-demo/
├── docker-compose.yml
├── requirements.txt
├── Jenkinsfile
└── tests/
    └── test_sample.py
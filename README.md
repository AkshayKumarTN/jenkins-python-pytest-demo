# Jenkins Python Pytest Demo

## Project Overview
CI/CD pipeline using Jenkins, Docker, Python, and Pytest for automated testing.

## Author
Akshay Kumar TN

## Technologies Used
- Jenkins (Docker)
- Python 3
- Pytest
- Git/GitHub

## Project Structure
```
jenkins-python-pytest-demo/
├── docker-compose.yml       # Jenkins container configuration
├── requirements.txt         # Python dependencies
├── Jenkinsfile             # Pipeline configuration
└── tests/
    └── test_sample.py      # Pytest test cases
```

## Setup Instructions

### 1. Start Jenkins
```bash
docker compose up -d
```

### 2. Access Jenkins
- URL: http://localhost:8080
- Get password:
```bash
docker exec -it jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

### 3. Install Python in Jenkins Container
```bash
docker exec -it jenkins bash
apt-get update && apt-get install -y python3 python3-venv python3-pip
exit
```

### 4. Create Pipeline Job
1. New Item → Pipeline
2. Configure with GitHub repository
3. SCM: Git
4. Repository URL: https://github.com/AkshayKumarTN/jenkins-python-pytest-demo
5. Branch: */master
6. Script Path: Jenkinsfile

### 5. Build Pipeline
Click "Build Now" and view results

## Test Results
- ✅ **2 tests pass:**
  - test_addition
  - test_subtraction
- ❌ **1 test fails (intentional):**
  - test_failure_example (demonstrates failure reporting)

## Pipeline Stages
1. **Install dependencies** - Creates Python virtual environment
2. **Run tests** - Executes pytest with JUnit XML reporting
3. **Publish Report** - Displays test results in Jenkins

## Screenshots
See deliverables folder for:
- Jenkins pipeline stage view
- Test results showing passes and failures
- Console output

## Repository
https://github.com/AkshayKumarTN/jenkins-python-pytest-demo
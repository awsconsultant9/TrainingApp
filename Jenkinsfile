pipeline {
    agent any

    environment {
        AWS_INSTANCE_IP = "13.203.160.38"  // Replace with your EC2 instance IP
        SSH_CREDENTIALS_ID = "064474ad-c93c-47d8-b6f1-db68411162b6"  // Replace with your Jenkins SSH credentials ID
        WORKSPACE_DIR = "/var/lib/jenkins/workspace/cicdpipeline"
        PROJECT_DIR = "/var/lib/jenkins/workspace/cicdpipeline/my_project"
        VENV_PATH = "/var/lib/jenkins/workspace/cicdpipeline/venv"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/awsconsultant9/TrainingApp.git'
            }
        }

        stage('Build') {
            steps {
                sh 'echo "Building the application..."'
                sh 'python3 -m venv ${VENV_PATH}'
                sh '''
                    bash -c "
                    source ${VENV_PATH}/bin/activate
                    python3 -m pip install poetry
                    poetry install
                    "
                '''
            }
        }

        stage('Deploy to Local Machine') {
            steps {
                script {
                    dir("${WORKSPACE_DIR}") {
                        sh 'git pull origin main'
                    }
                }
            }
        }

        stage('Start FastAPI App') {
            steps {
                script {
                    // Ensure the FastAPI server starts automatically
                    sh '''
                        cd ${PROJECT_DIR}
                        nohup uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4 > fastapi.log 2>&1 &
                    '''
                }
            }
        }
    }
}

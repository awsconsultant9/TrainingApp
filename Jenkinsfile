pipeline {
    agent any

    environment {
        WORKSPACE_DIR = '/var/lib/jenkins/workspace/cicdpipeline'
        PROJECT_DIR = '/var/lib/jenkins/workspace/cicdpipeline/my_project'
        VENV_PATH = '/var/lib/jenkins/workspace/cicdpipeline/venv'
        
        // AWS EC2 Instance and SSH Credentials
        AWS_INSTANCE_IP = "13.203.160.38"  // Replace with your EC2 instance IP
        SSH_CREDENTIALS_ID = "064474ad-c93c-47d8-b6f1-db68411162b6"  // Replace with your Jenkins SSH credentials ID
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/awsconsultant9/TrainingApp.git'
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                sh 'python3 -m venv ${VENV_PATH}'
                sh 'source ${VENV_PATH}/bin/activate'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'source ${VENV_PATH}/bin/activate && python3 -m pip install poetry && poetry install'
            }
        }

        stage('Build') {
            steps {
                sh 'echo "Building the application..."'
                sh 'source ${VENV_PATH}/bin/activate && poetry install'
            }
        }

        stage('Deploy to Local Machine') {
            steps {
                script {
                    // Navigate to the cloned repository
                    dir("${WORKSPACE_DIR}") {
                        // Pull the latest changes from the main branch
                        sh 'git pull origin main'
                    }

                    // If the project uses a systemd service, restart it here
                    // sh 'sudo systemctl restart my-project'  // Uncomment and replace if needed
                }
            }
        }

        stage('Start FastAPI App') {
            steps {
                sh '''
                    cd ${PROJECT_DIR}
                    nohup uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4 > fastapi.log 2>&1 &
                '''
            }
        }
    }
}

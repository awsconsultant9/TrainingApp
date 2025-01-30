pipeline {
    agent any

    environment {
        AWS_INSTANCE_IP = "13.203.160.38"  // Replace with your EC2 instance IP
        SSH_CREDENTIALS_ID = "064474ad-c93c-47d8-b6f1-db68411162b6"  // Replace with your Jenkins SSH credentials ID
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/awsconsultant9/TrainingApp.git'
            }
        }

        stage('Build') {
            steps {
                // bat 'echo Building on Windows'
                  sh 'echo "Building the application..."'
                poetry install
                // Add build commands here (e.g., npm install, mvn package, etc.)
            }
        }

        stage('Deploy to EC2') {
            steps {
                script {
                    sshagent (credentials: [SSH_CREDENTIALS_ID]) {
                        sh """
                            ssh -o StrictHostKeyChecking=no ubuntu@${AWS_INSTANCE_IP} << EOF
                            cd /home/ubuntu/app
                            git pull origin main
                            sudo systemctl restart myapp  # Restart your application service
                            EOF
                        """
                    }
                }
            }
        }
    }
}

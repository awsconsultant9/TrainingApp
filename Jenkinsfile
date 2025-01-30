pipeline {
    agent any

    environment {
        AWS_INSTANCE_IP = "13.203.160.38"  // Replace with your EC2 instance IP
        SSH_CREDENTIALS_ID = "d5d4a42b-5190-4966-b1e9-df8f35ee3483"  // Replace with your Jenkins SSH credentials ID
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

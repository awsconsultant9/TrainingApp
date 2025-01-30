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
                sh 'poetry install'
                // Add build commands here (e.g., npm install, mvn package, etc.)
            }
        }

stage('Deploy to Local Machine') {
    steps {
        script {
            // Navigate to the cloned repository
            dir('/path/to/cloned/repo') {
                // Pull the latest changes from the main branch
                sh 'git pull origin main'
            }
            
            // Restart the application service
            sh 'sudo systemctl restart myapp'  // Replace with your actual service name
        }
    }
}

    }
}

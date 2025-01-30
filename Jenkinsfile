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
            dir('/var/lib/jenkins/workspace/cicdpipeline') {
                // Pull the latest changes from the main branch
                sh 'git pull origin main'
            }
            
            // Restart the application service
            // sh 'sudo systemctl restart my-project'   Replace with your actual service name
        }
    }
}
    stage('Start FastAPI App') {
    steps {
        script {
            // Start the FastAPI app using uvicorn or gunicorn
            // Optionally use systemd if needed (you can run it as a service)
            sh """
                # Activate the virtual environment if using one
                # source /path/to/virtualenv/bin/activate

                # If using uvicorn to run the FastAPI app:
                nohup uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4 > fastapi.log 2>&1 &

                # Alternatively, if using gunicorn (recommended for production):
                # nohup gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app --host 0.0.0.0 --port 8000 > fastapi.log 2>&1 &

                # If the app is managed by systemd (optional):
               #  sudo systemctl restart fastapi-app
            """
        }
    }


}

    }
}

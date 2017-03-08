pipeline {
    agent any
    stages {
        stage('Test') {
            steps{
                sh 'echo "Fail!"; exit 1'
            }  
        }
        stage('Build') {
            steps {
                sh 'echo "Building..."'
            }
        }

        stage('Deploy'){
            steps{
                retry(3) {
                    sh './flakey-deploy.sh'
                }
                timeout(time: 3, unit: 'MINUTES') {
                    sh './slow-process.sh'
                }
           }
        }
    }
    
    post {
        always {
            "Test and Build complete."
        }
        success {
            "Test and Build succeeded."
        }
        failure {
            "Test and Build failed."
        }
        unstable {
            "Test and Build unstable."
        }
        changed {
            "Pipeline state has changed.."
        }
    }
}

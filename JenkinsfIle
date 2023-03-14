pipeline {
  agent any

  environment {
    NGROK_AUTH_TOKEN = credentials('ngrok-auth-token')
  }
  
  stages {
    stage('Build') {
      steps {
        sh 'echo Pakistan Zindabad'
        sh 'docker build -t myflaskapp .'
      }
    }
    stage('Test') {
      steps {
        sh 'docker run myflaskapp python test.py'
      }
    }
    stage('Deploy') {
      steps {
        sh 'docker run -d -p 8000:5000 myflaskapp'
      }
    }
    stage('Expose') {
      steps {
        ngrok([httpPort: 5000])
    }
    }
  }
}

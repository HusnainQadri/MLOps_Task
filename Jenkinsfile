pipeline {
  agent any
  
  stages {
    stage('Build') {
      steps {
        bat 'echo Pakistan Zindabad'
        bat 'docker build -t myflaskapp .'
      }
    }
    stage('Test') {
      steps {
        bat 'docker run myflaskapp python test.py'
      }
    }
    stage('Deploy') {
      steps {
        bat 'docker run -d -p 8000:5000 myflaskapp'
      }
    }
    stage('Expose') {
      steps {
        ngrok([httpPort: 5000])
    }
    }
  }
}

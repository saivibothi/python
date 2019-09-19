pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'pip install --upgrade pip --user'
        sh 'pip install -r requirements.txt --user'
      }
    }
    stage('test') {
      steps {
        sh 'python doc2.py'
      }   
    }
  }
}

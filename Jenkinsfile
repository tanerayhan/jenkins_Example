pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('hello') {
      steps {
        sh ' pip install rich && python3 hello.py'
      }
    }
  }
}

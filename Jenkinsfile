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
        sh 'sudo stty rows 50 cols 132 &&hoami && pip install rich && python3 hello.py'
      }
    }
  }
}

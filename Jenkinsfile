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
        sh ' python -m rich.table && pip install tabulate && pip install rich && python3 hello.py'
      }
    }
  }
}

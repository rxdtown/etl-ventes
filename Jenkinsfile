pipeline {
    agent any

    environment {
        IMAGE_NAME = "etl-ventes"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup environnement') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Lint') {
            steps {
                sh '''
                    . venv/bin/activate
                    flake8 src/ --max-line-length=100 || true
                '''
            }
        }

        stage('Tests unitaires') {
            steps {
                sh '''
                    . venv/bin/activate
                    python -m pytest tests/ -v --junitxml=results.xml
                '''
            }
            post {
                always {
                    junit 'results.xml'
                }
            }
        }

        stage('Exécution du pipeline ETL') {
            steps {
                sh '''
                    . venv/bin/activate
                    python -m src.pipeline
                '''
            }
        }

        stage('Build image Docker') {
            steps {
                sh 'docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} .'
            }
        }

        stage('Archivage') {
            steps {
                archiveArtifacts artifacts: 'output/*.parquet', fingerprint: true
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline ETL exécuté avec succès et image construite.'
        }
        failure {
            echo '❌ Le pipeline a échoué — voir logs ci-dessus.'
        }
        always {
            cleanWs()
        }
    }
}
pipeline {
    agent any

    environment {
        VIRTUAL_ENV = 'venv'
    }

    stages {
        stage('Setup') {
            steps {
                script {
                    if (!fileExists("${env.WORKSPACE}/${VIRTUAL_ENV}")) {
                        bat "python -m venv ${VIRTUAL_ENV}"
                    }
                    bat "${VIRTUAL_ENV}\\Scripts\\activate && pip install -r requirements.txt"
                }
            }
        }

        stage('Lint') {
            steps {
                bat "${VIRTUAL_ENV}\\Scripts\\activate && flake8 app.py"
            }
        }

        stage('Test') {
            steps {
                bat "${VIRTUAL_ENV}\\Scripts\\activate && pytest"
            }
        }

        stage('Coverage') {
            steps {
                bat """
                call ${VIRTUAL_ENV}\\Scripts\\activate
                coverage run -m pytest
                coverage report
                """
            }
        }


        stage('Security Scan') {
            steps {
                bat """
                call ${VIRTUAL_ENV}\\Scripts\\activate
                python -X utf8 -m bandit -r . || exit /b 0
                """
            }
        }



        stage('Deploy') {
            steps {
                echo "Deploying application... (simulation)"
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}

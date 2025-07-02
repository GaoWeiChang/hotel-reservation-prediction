pipeline{
    agent any // Run on any available agent

    environment {
        VENV_DIR = 'venv'
    }

    stages{
        stage('Cloning Github repo to Jenkins'){
            steps{
                script{
                    // this will show in Jenkins terminal
                    echo 'Cloning Github repo to Jenkins......' 
                    // load source code from Github to Jenkins workspace
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/GaoWeiChang/hotel-reservation-prediction.git']])
                }
            }
        }

        stage('Setting up our Virtual Environment and Installing dependencies'){
            steps{
                script{
                    echo 'Setting up our Virtual Environment and Installing dependencies......'
                    sh '''
                    python -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                    '''
                }
            }
        }
    }
}
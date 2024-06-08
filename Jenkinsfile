pipeline {
    agent any
    stages {
        stage('requirements') {
            steps {
                    echo 'time.sleep(1)'
            }
        }
        stage('dvc_data_get') {
            steps {
                    echo "3"
            }
        }  
                stage('run_data_test') {
            steps {
                    echo "2"
            }
                    stage('run_model_test') {
            steps {
                    echo "2"
            }
        }
    }
}

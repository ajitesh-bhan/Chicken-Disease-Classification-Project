from CNNClassifier.config.configuration import ConfigurationManager
from CNNClassifier.components.data_ingestion import DataIngestion
from CNNClassifier import logger

stage_name ='Data Ingestion'

class DataIngestionStage:
    def __init__(self):
        pass

    def main(self):

        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


## defining seperatily for the DVC stage
if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>> stage {stage_name} started <<<<<<<<<")
        obj = DataIngestionStage()
        obj.main()
        logger.info(f'>>>>>>>> stage {stage_name} completed! <<<<<<<<< ')
    except Exception as e:
        logger.error(f'Error in stage {stage_name}: {e}')

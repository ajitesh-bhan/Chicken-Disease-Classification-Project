from CNNClassifier.pipeline.stage_01_data_ingestion import  DataIngestionStage
from  CNNClassifier import logger


stage_name ='Data Ingestion'

try:
    logger.info(f">>>>>>>> stage {stage_name} started <<<<<<<<<")
    obj = DataIngestionStage()
    obj.main()
    logger.info(f'>>>>>>>> stage {stage_name} completed! <<<<<<<<< ')
except Exception as e:
    logger.error(f'Error in stage {stage_name}: {e}')
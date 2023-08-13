from CNNClassifier.pipeline.stage_01_data_ingestion import  DataIngestionStage
from  CNNClassifier import logger
from CNNClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelStage
from CNNClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelStage
from CNNClassifier.pipeline.stage_03_training import Training_Pipeline
from CNNClassifier.pipeline.stage_04_model_evaluation import Evaluation_Pipeline
stage_name ='Data Ingestion'

try:
    logger.info(f">>>>>>>> stage {stage_name} started <<<<<<<<<")
    obj = DataIngestionStage()
    obj.main()
    logger.info(f'>>>>>>>> stage {stage_name} completed! <<<<<<<<< ')
except Exception as e:
    logger.error(f'Error in stage {stage_name}: {e}')




Stage_Name = 'Prepare Base Model'

try:
    logger.info(f'>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    logger.info(f'><<<<<Prepare base model stage {Stage_Name} satrted')    
    obj= PrepareBaseModelStage()    
    obj.main()
    logger.info(f'<<<stage {Stage_Name} completed')

    logger.info(f'<<<<<<<<<<<<<<<<<<<<<<<<<<<<')

except Exception as e:
    logger.exception(e) 



Stage_Name= 'Training'

try:
    logger.info(f'>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    logger.info(f'><<<<< stage {Stage_Name} satrted')    
    obj= Training_Pipeline()    
    obj.main()
    logger.info(f'<<<stage {Stage_Name} completed')

    logger.info(f'<<<<<<<<<<<<<<<<<<<<<<<<<<<<')

except Exception as e:
    logger.exception(e) 



Stage_Name= 'Evaluation'

try:
    logger.info(f'>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    logger.info(f'><<<<< stage {Stage_Name} satrted')    
    obj= Evaluation_Pipeline()    
    obj.main()
    logger.info(f'<<<stage {Stage_Name} completed')

    logger.info(f'<<<<<<<<<<<<<<<<<<<<<<<<<<<<')

except Exception as e:
    logger.exception(e) 

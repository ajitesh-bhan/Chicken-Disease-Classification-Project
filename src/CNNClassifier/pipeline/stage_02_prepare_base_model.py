from CNNClassifier.config.configuration import ConfigurationManager
from CNNClassifier.components.prepare_base_model import PrepareBaseModel
from CNNClassifier import logger

Stage_Name= 'Prepare Base Model'

class PrepareBaseModelStage:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()


if __name__ == '__main__' : 
    try:
        logger.info(f'>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        logger.info(f'><<<<<Prepare base model stage {Stage_Name} satrted')    
        obj= PrepareBaseModelStage()    
        obj.main()
        logger.info(f'<<<stage {Stage_Name} completed')

        logger.info(f'<<<<<<<<<<<<<<<<<<<<<<<<<<<<')

    except Exception as e:
        logger.exception(e) 


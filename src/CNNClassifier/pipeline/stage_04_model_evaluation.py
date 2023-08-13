from CNNClassifier.config.configuration import ConfigurationManager
from CNNClassifier.components.model_evaluation import Evaluation
from CNNClassifier import logger

Stage_Name= 'Evaluation'

class Evaluation_Pipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()


if __name__ == '__main__' : 
    try:
        logger.info(f'>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        logger.info(f'><<<<<Stage started {Stage_Name} ')    
        obj= Evaluation_Pipeline()    
        obj.main()
        logger.info(f'<<<stage {Stage_Name} completed')

        logger.info(f'<<<<<<<<<<<<<<<<<<<<<<<<<<<<')

    except Exception as e:
        logger.exception(e) 
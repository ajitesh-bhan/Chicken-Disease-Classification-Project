from CNNClassifier.config.configuration import ConfigurationManager
from CNNClassifier.components.training import Training
from CNNClassifier.components.prepare_callbacks import PrepareCallback
from CNNClassifier import logger

Stage_Name= 'Training'

class Training_Pipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        prepare_callbacks_config = config.get_prepare_callback_config()
        prepare_callbacks = PrepareCallback(config=prepare_callbacks_config)
        callback_list = prepare_callbacks.get_tb_ckpt_callbacks()

        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(
            callback_list=callback_list
        )


if __name__ == '__main__' : 
    try:
        logger.info(f'>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        logger.info(f'><<<<<Stage started {Stage_Name} ')    
        obj= Training_Pipeline()    
        obj.main()
        logger.info(f'<<<stage {Stage_Name} completed')

        logger.info(f'<<<<<<<<<<<<<<<<<<<<<<<<<<<<')

    except Exception as e:
        logger.exception(e) 

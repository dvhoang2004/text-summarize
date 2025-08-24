from textSummarize.logging import logger
from textSummarize.components.data_validation import DataValidation
from textSummarize.config.configuration import ConfigurationManager
from textSummarize.entity import DataValidationConfig

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_existed_files()
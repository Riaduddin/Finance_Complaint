from finance_complaint.constant.training_pipeline_config import PIPELINE_NAME
from finance_complaint.constant import TIMESTAMP
from finance_complaint.constant.training_pipeline_config import *
from finance_complaint.entity.config_entity import TrainingPipelineConfig
from finance_complaint.exception import FinancialException
from finance_complaint.logger import logger
import os,sys

class FinanceConfig:
    def __init__(self,pipeline_name=PIPELINE_NAME,timestamp=TIMESTAMP):

        self.timestamp=timestamp
        self.pipeline_name=pipeline_name
        self.pipeline_config=self.get_pipeline_config()

    def get_pipeline_config(self)->TrainingPipelineConfig:
        try:
            artifact_dir=PIPELINE_ARTIFACT_DIR
            pipeline_config=TrainingPipelineConfig(pipeline_name=self.pipeline_name,
                                                   artifact_dir=artifact_dir)
            logger.info(f"Pipelline configuration: {pipeline_config}")

            return pipeline_config
        except Exception as e:
            raise FinancialException(e,sys)

from src.Smart_premium_prediction import logger
from src.Smart_premium_prediction.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline


STAGE_NAME = 'Data Ingestion Stage'
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.initiate_data_ingestion()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
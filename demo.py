#from us_visa.configuration.mongodb_connection import MongoDBClient
from us_visa.components.data_ingestion import DataIngestion

from us_visa.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig
from us_visa.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact
from us_visa.components.data_validation import DataValidation
from us_visa.components.data_transformation import DataTransformation
#ins=MongoDBClient()
di_ins = DataIngestion()
di_art = di_ins.initiate_data_ingestion()
dv_ins=DataValidation(data_ingestion_artifact=di_art,data_validation_config=DataValidationConfig)
dv_art=dv_ins.initiate_data_validation()

dt_ins = DataTransformation(data_ingestion_artifact=di_art, data_transformation_config=DataTransformationConfig, data_validation_artifact=dv_art)

dt_art = dt_ins.initiate_data_transformation()

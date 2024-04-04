from us_visa.configuration.mongodb_connection import MongoDBClient
from us_visa.components.data_ingestion import DataIngestion

ins=MongoDBClient()
di_ins = DataIngestion()
di_art = di_ins.initiate_data_ingestion()
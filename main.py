import pandas as pd
from enrich import enrichBPMN

# ## CSV File

# if csv file do not have column
# ## please add column name
#csv_file = pd.read_csv('Data/testEnrichment.csv', sep=";", parse_dates=True)
#csv_file.columns = ["mainShipmentRouteNumber", "speed", "time", "truckNumber", "timestamp", "shipmentEndCity", "shipmentStartCity", "city", "country","activity"]
#csv_file.to_csv('Data/LHR_AMS_After_Preprocess.csv', index=False)

csv_file = pd.read_csv('Data/LHR_AMS_After_Preprocess.csv', parse_dates=True)
timestamp = 'timestamp'
############### Artifact ################
artifact_dict = {'Truck':['speed','country','city'],'Container':[]}
selected_artifact = 'Truck'
instanceId = 'mainShipmentRouteNumber'

# ## Enrichment
enrichBPMN(csv_file,artifact_dict,selected_artifact,instanceId,timestamp)
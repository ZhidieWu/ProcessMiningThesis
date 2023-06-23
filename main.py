import pandas as pd
from enrich import enrichBPMN

# ## CSV File
csv_file = pd.read_csv('Data/testEnrichment.csv', sep=";", parse_dates=True)


############### Artifact ################
artifact_dict = {'Truck':['speed','country','city'],'Container':[]}
selected_artifact = 'Truck'
instanceId = 'mainShipmentRouteNumber'

# ## add column name
csv_file.columns = ["mainShipmentRouteNumber", "speed", "time", "truckNumber", "timestamp", "shipmentEndCity",
                    "shipmentStartCity", "city", "country","activity"]
# ## Enrichment
enrichBPMN(csv_file,artifact_dict,selected_artifact,instanceId)
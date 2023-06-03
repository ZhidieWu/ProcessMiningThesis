import pm4py
import pandas as pd
bpmn_file = "Data/testPart1.bpmn"
df = pd.read_csv('Data/new_LHR_AMS.csv', sep=";",parse_dates=True)

# ## add column name
df.columns = ["mainShipmentRouteNumber", "speed", "time", "truckNumber", "timestamp", "shipmentEndCity",
                "shipmentStartCity", "city", "country","activity"]

df.to_csv('Data/dataWithColumn.csv', index=False)
df = pd.read_csv('Data/dataWithColumn.csv', sep=";",parse_dates=['time'],infer_datetime_format=True)
dfg,start_activities,end_activities = pm4py.discover_dfg(df,case_id_key="mainShipmentRouteNumber",activity_key="activity",timestamp_key="timestamp")
from simple_salesforce import Salesforce
from dotenv import load_dotenv
import os
import pandas as pd
import datetime
from datetime import date
load_dotenv()

password=os.getenv("password")
username=os.getenv("username")
token=os.getenv("token")
instance_url = os.getenv("instance_url")

today = date.today()
seven_days = datetime.timedelta(7)
last_week = today - seven_days
print(last_week)

sf = Salesforce(username=username, password=password, instance=instance_url, security_token=token)

data = sf.query(f"SELECT CreatedBy.Name, Display, Action, CreatedDate FROM SetupAuditTrail WHERE CreatedBy.Name != null and CreatedDate > {last_week}T01:00:00Z order by CreatedDate desc LIMIT 200")
df = pd.DataFrame(data['records'])

df.to_csv('out.csv')


# Monitoring the SetupAuditTrail Salesforce Object using Python

This project is designed to provide a method of automatic monitoring on the Setup Audit Trail without needing to regularly go into the Salesforce UI and request those logs. Using the SetupAuditTrail object, added in Winter '16, enables programmatic interfacing via SOQL queries. I use the simple-salesforce library to authenticate and then start pulling the data. The SOQL query in it's current form is designed to get the last 7 days of activity and filter out any processes which are not associated with a specific user. From there, the data will be complied into csv files using pandas/dataframes.

### Prereqs

Relevant permissions for your Salesforce org to use the API and view Setup Audit Trail.

The ability to run a Python script

Python libraries:
- simple-salesforce
- pandas
- python-dotenv
- datetime

### Setting Up

When running thisscript locally, it is not completely necessary to use environment variables and the dotenv configurations. Regardless, the authentication method chosen here requires the username, password, and security token. If you don't know or have your security token, please refer to this article: https://help.salesforce.com/s/articleView?id=sf.user_security_token.htm&type=5

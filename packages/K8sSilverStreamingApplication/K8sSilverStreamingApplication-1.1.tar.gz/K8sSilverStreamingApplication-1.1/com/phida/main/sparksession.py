import os
import base64
import pyspark
import json
from pyspark.sql import SparkSession
from com.phida.main import logging
from com.phida.main import config

# Get from Environment Variable Secrets which is defined in the SparkApplication yaml
# TENANT_ID = os.getenv('TENANT_ID')
# SERVICE_PRINCIPAL_ID = os.getenv('SERVICE_PRINCIPAL_ID')
# SERVICE_PRINCIPAL_KEY = os.getenv('SERVICE_PRINCIPAL_KEY')
# SSA_STORAGE_ACCOUNT_NAME = os.getenv('SSA_STORAGE_ACCOUNT_NAME')
# tenant_id = base64.b64decode(TENANT_ID).decode("utf-8")
# client_id = base64.b64decode(SERVICE_PRINCIPAL_ID).decode("utf-8")
# client_secret = base64.b64decode(SERVICE_PRINCIPAL_KEY).decode("utf-8")
# ssa_storage_account_name = base64.b64decode(SSA_STORAGE_ACCOUNT_NAME).decode("utf-8")

tenant_id = os.environ.get("TENANT_ID")
client_id = os.environ.get("SERVICE_PRINCIPAL_ID")
client_secret = os.environ.get("SERVICE_PRINCIPAL_KEY")
ssa_storage_accounts_json = os.environ.get("SSA_STORAGE_ACCOUNTS")
# Parse the JSON string to get the list of storage accounts
ssa_storage_accounts = json.loads(ssa_storage_accounts_json)['storage_accounts']
#print(tenant_id)
#print(client_id)
#print(client_secret)
#print(ssa_storage_account_name)


# Get sparkAppName from the global configuration
appName = config.get_config("sparkAppName")
print("********************************sparkAppName***********************: ", appName)

def create_spark_session(app_name, tenant_id, client_id, client_secret, ssa_storage_accounts):
    builder = SparkSession.builder.appName(app_name) \
        .config('spark.jars.packages', 'org.apache.hadoop:hadoop-azure:3.3.1,com.azure:azure-identity:1.2.3') \
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

    for storage_account in ssa_storage_accounts:
        storage_account_name = storage_account['name']
        builder = builder.config(f"fs.azure.account.auth.type.{storage_account_name}.dfs.core.windows.net", "OAuth") \
            .config(f"fs.azure.account.oauth.provider.type.{storage_account_name}.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider") \
            .config(f"fs.azure.account.oauth2.client.id.{storage_account_name}.dfs.core.windows.net", client_id) \
            .config(f"fs.azure.account.oauth2.client.secret.{storage_account_name}.dfs.core.windows.net", client_secret) \
            .config(f"fs.azure.account.oauth2.client.endpoint.{storage_account_name}.dfs.core.windows.net", f"https://login.microsoftonline.com/{tenant_id}/oauth2/token")

    spark = builder.getOrCreate()
    return spark

spark = create_spark_session(app_name, tenant_id, client_id, client_secret, ssa_storage_accounts)

# # Initialize SparkSession with Azure Active Directory OAuth2 configurations
# spark = SparkSession.builder \
#     .appName(appName) \
#     .config('spark.jars.packages', 'org.apache.hadoop:hadoop-azure:3.3.1,com.azure:azure-identity:1.2.3') \
#     .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
#     .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
#     .config(f"fs.azure.account.auth.type.{ssa_storage_account_name}.dfs.core.windows.net", "OAuth") \
#     .config(f"fs.azure.account.oauth.provider.type.{ssa_storage_account_name}.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider") \
#     .config(f"fs.azure.account.oauth2.client.id.{ssa_storage_account_name}.dfs.core.windows.net", client_id) \
#     .config(f"fs.azure.account.oauth2.client.secret.{ssa_storage_account_name}.dfs.core.windows.net", client_secret) \
#     .config(f"fs.azure.account.oauth2.client.endpoint.{ssa_storage_account_name}.dfs.core.windows.net", f"https://login.microsoftonline.com/{tenant_id}/oauth2/token") \
#     .getOrCreate()

logger = logging.Log4j(spark)
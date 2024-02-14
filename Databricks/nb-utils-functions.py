# Databricks notebook source
def mountStorageAccountCredentialPassthrough(storage_account_name,container_name,mount_name) :

    try:
        configs = {
        "fs.azure.account.auth.type": "CustomAccessToken",
        "fs.azure.account.custom.token.provider.class": spark.conf.get("spark.databricks.passthrough.adls.gen2.tokenProviderClassName")
        }

        #Generate Mount point path
        mount_point_path = f"/mnt/{mount_name}"
              
        #Unmount the mount if it already exists
        if any(mount.mountPoint  ==  mount_point_path for mount in dbutils.fs.mounts()):
            dbutils.fs.unmount(mount_point_path)  

        # Optionally, you can add <directory-name> to the source URI of your mount point.
        dbutils.fs.mount(
        source = f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/",
        mount_point = mount_point_path,
        extra_configs = configs)

        print(f'{mount_point_path} suscefully mounted')

    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise
          
   


# COMMAND ----------



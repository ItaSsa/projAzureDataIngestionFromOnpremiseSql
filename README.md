# projAzureDataIngestionFromOnpremiseSql

This is a  Ingestion, Transfortion and Load project from an on premise SQL Database into a Storage Account in the Azure Cloud. 

The data source is a local sample database AdventuraWorks2019 , and we picked the Person schema up for this project.

Here are the containers in the Storage Account:

![image](https://github.com/ItaSsa/projAzureDataIngestionFromOnpremiseSql/assets/119689138/359c9a0c-cea8-42c0-96c3-132c358753bc)

We used an Azure Data Factory pipeline as:

![image](https://github.com/ItaSsa/projAzureDataIngestionFromOnpremiseSql/assets/119689138/2825b53d-f1ae-4441-b358-26703756bbfe)

The first and second activities are to copy the data from the source in the /bronze container.

The third activity runs a Databricks Notebook that reads data from /bronze container, transforms it, and load in the /silver layer.

The fourth activity runs a Databricks Notebook that reads data from /silver container, transforms it, and load in the /gold layer.

After the read-consumption date is in the /gold layer, we used the Synapse Workspace to create a new SQL database. It was created one view of each file in the gold layer. We created a pipeline to create those views always it would need.  
![image](https://github.com/ItaSsa/projAzureDataIngestionFromOnpremiseSql/assets/119689138/eb94bcd4-b3d7-4e21-9214-5997f0694c0c)

![image](https://github.com/ItaSsa/projAzureDataIngestionFromOnpremiseSql/assets/119689138/4a2448c5-fddc-4eee-8d82-dfca47b2ebdd)


## Techonologies

- Azure Cloud

- Azure Data Factory

- Azure Databricks

- Azure Synapse

- Python

## Author

Itaira Soares de Freitas Santos

https://www.linkedin.com/in/itaira-santos


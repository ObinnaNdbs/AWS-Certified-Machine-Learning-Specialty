# Lab: Running SQL Queries in Amazon Athena

## Overview

In this hands-on lab, we learned how to perform SQL queries on data stored in Amazon S3 using Amazon Athena, with schema extraction powered by AWS Glue.
![image](https://github.com/user-attachments/assets/7fdb782a-eb5f-4259-bf94-28b0b32ae1c1)

## Workflow Summary

1. **Source Data**
   - A `.csv` file (`football_players_data.csv`) was stored in an S3 bucket named `dct-bucket-demo`.
   - This file included player information such as ID, name, age, and release clause.
![image](https://github.com/user-attachments/assets/06794fff-bb2e-471d-85d2-f47073f3dd45)

2. **Schema Extraction with AWS Glue**
   - An AWS Glue Crawler was configured to scan the S3 path and extract the file schema.
   - The crawler output was stored in the **AWS Glue Data Catalog**, under a database named `players`.
![image](https://github.com/user-attachments/assets/cad346ae-b004-47cf-8a60-030ff2dd73e7)

3. **Querying with Athena**
   - Amazon Athena was configured to use the `players` database from the Glue Data Catalog as the data source.
   - Output location for query results was set to a folder in S3.
   - A basic SQL query (`SELECT * LIMIT 10`) was generated using the **Preview Table** option.
![image](https://github.com/user-attachments/assets/4c3526d7-b238-41af-9892-07b4f00e29dd)

   - The query results were saved automatically to the specified S3 output path.
![image](https://github.com/user-attachments/assets/144ccd7c-0a36-4589-b89d-35370f4354df)

## Tools Used

- Amazon S3
- AWS Glue Crawler
- AWS Glue Data Catalog
- Amazon Athena

## Skills Demonstrated

- Setting up a Glue Crawler to extract schema
- Configuring Amazon Athena to use the Data Catalog
- Running basic SQL queries in Athena
- Viewing and downloading query results from S3


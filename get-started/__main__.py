import json
import pulumi
import pulumi_aws as aws

# Criação de um bucket S3 
bucket_name = 'pulumi-ttech'
bucket = aws.s3.Bucket(bucket_name,
    bucket=bucket_name,
)

#Exportando nome do bucket no output
pulumi.export('bucket_name', bucket.id)

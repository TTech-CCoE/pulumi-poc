import json
import pulumi
import pulumi_aws as aws

# Criação de um bucket S3 com configuração de site estático
bucket_name = 'pulumi-ttech'
bucket = aws.s3.Bucket(bucket_name,
    bucket=bucket_name,
)

website = aws.s3.BucketWebsiteConfigurationV2("website",
    bucket=bucket.id,
    index_document={
        "suffix": "index.html",
})

ownership_controls = aws.s3.BucketOwnershipControls(
    'ownership-controls',
    bucket=bucket.id,
    rule={
        "object_ownership": 'ObjectWriter',
    },
)

public_access_block = aws.s3.BucketPublicAccessBlock(
    'public-access-block', bucket=bucket.id, block_public_acls=False
)
# Definindo uma política de bucket para permitir acesso público
bucket_policy = aws.s3.BucketPolicy('bucket-policy',
    bucket=bucket.id,
    policy=json.dumps({
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": "*",
                "Action": "s3:GetObject",
                "Resource": f"arn:aws:s3:::{bucket_name}/*"  # Aqui você usa o nome fixo
            }
        ]
    }),
   
)

bucket_object = aws.s3.BucketObject(
    'index.html',
    bucket=bucket.id,
    source=pulumi.FileAsset('index.html'),
    content_type='text/html',
    acl='public-read',
    opts=pulumi.ResourceOptions(depends_on=[public_access_block, ownership_controls, website]),
)
# Exportando a URL do bucket
pulumi.export('bucket_name', bucket.id)
pulumi.export('bucket_object_url', pulumi.Output.concat("http://", bucket.website_endpoint, "/index.html"))

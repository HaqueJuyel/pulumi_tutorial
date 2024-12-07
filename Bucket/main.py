import pulumi
from pulumi_gcp import storage
import sys 
import os
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'config')))
import variables

#Bucket Creation
bucket = storage.Bucket(
    variables.BUCKET_NAME,
    location=variables.REGION,
    storage_class=variables.STORAGE_CLASS,
    force_destroy=variables.FORCE_DESTROY,
)

pulumi.export("Bucket_url=",bucket.url)
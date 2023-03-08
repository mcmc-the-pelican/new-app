import os

sync_command = f"aws s3 sync s3://static-prod-bucket"
os.system(sync_command)

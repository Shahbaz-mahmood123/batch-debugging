import pulumi
import pulumi_gcp as gcp

    
class PulumiGCPInterface():
    pass 

        
class PulumiGCP(PulumiGCPInterface):
    
    def __init__(self, project_id: str, location: str, name: str) -> None:
        self.project_id = project_id 
        self.location = location
        self.name = name
        
    def pulumi_program(self):

        # Creates a GCP storage bucket with the specified name
        bucket = gcp.storage.Bucket(self.name,
                                    name=self.name, location=self.location, project=self.project_id)

        # Export the bucket's URL
        pulumi.export('bucket_url', bucket.url)
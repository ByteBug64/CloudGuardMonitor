import boto3
import json

client = boto3.client('s3')
buckets = client.list_buckets() ['Buckets']
def check_public_access_block():
    findings = []
    try:
        for bucket in buckets:
            check_public_access = client.get_public_access_block(Bucket=bucket['Name'])
            if check_public_access['PublicAccessBlockConfiguration']['BlockPublicAcls'] == False:    
                findings.append({
                    "severity": "CRITICAL",
                    "title": f"Bucket {bucket['Name']} has public ACLs enabled",
                    "status": "FAIL",
                    })
            else:
                findings.append({
                    "severity": "INFO",
                    "title": f"Bucket {bucket['Name']} has public ACLs blocked",
                    "status": "PASS",
                    })
    except Exception as e:
        findings.append({
            "severity": "ERROR",
            "title": f"Error checking bucket public access: {str(e)}",
            "status": "ERROR",
        })
    return findings   
if __name__ == "__main__": 
    results = check_public_access_block()
    print(json.dumps(results, indent = 2))
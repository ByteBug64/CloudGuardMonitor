import boto3
import json

def check_security_groups():
    findings = []
    client = boto3.client('ec2')
    try:
        security_groups = client.describe_security_groups()['SecurityGroups']
        for security_group in security_groups:
            for Ip_Permission in security_group['IpPermissions']:
                for Ip_Range in Ip_Permission['IpRanges']:
                    if Ip_Permission['FromPort'] == 22 and Ip_Range['CidrIp'] == '0.0.0.0/0':
                        findings.append({
                            'severity': 'CRITICAL',
                            'title': f"Security Group {security_group['GroupId']} has port 22 open to the World",
                            'status': 'FAIL'
                        })
    except Exception as e:
        findings.append({
            'severity': 'ERROR',
            'title': f"Error checking security group {str(e)}",
            'status': 'ERROR'
        })        
    return findings

if __name__ == "__main__":
    results = check_security_groups()
    print(json.dumps(results, indent = 2))
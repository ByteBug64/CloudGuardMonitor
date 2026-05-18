import boto3
import json
client = boto3.client('iam')
def check_mfa():
    findings = []
    try:
        summary = client.get_account_summary()['SummaryMap']
        if summary['AccountMFAEnabled'] == 0:
            findings.append({
            "severity": "CRITICAL",
            "title": "Root MFA is Disabled",
            "status": "FAIL",
            })
        else:
            findings.append({
            "severity": "INFO",
            "title": "Root MFA is Enabled",
            "status": "PASS",
            })
    except Exception as e:
        findings.append({
            "severity": "ERROR",
            "title": f"Error checking root MFA: {str(e)}",
            "status": "ERROR",        
        })
    return findings

def check_password_policy():
    findings = []
    try:
        policy = client.get_account_password_policy()           ['PasswordPolicy']
        if policy['MinimumPasswordLength'] < 14:
            findings.append({
                "severity": "CRITICAL",
                "title": "Minimum password length is less than 14",
                "status": "FAIL",
            })
        else:
            findings.append({
                "severity": "INFO",
                "title": "Minimum password length is 14 or greater",
                "status": "PASS",
            })
    except client.exceptions.NoSuchEntityException:
        findings.append({
            "severity": "CRITICAL",
            "title": "No password policy exists on this account",
            "status": "FAIL",
    })
    except Exception as e:
        findings.append({
            "severity": "ERROR",
            "title": f"Error checking password policy: {str(e)}",
            "status": "ERROR",
        })
    return findings   
if __name__ == "__main__": 
    findings = []
    results = check_mfa() + check_password_policy()        
    print(json.dumps(results, indent=2))
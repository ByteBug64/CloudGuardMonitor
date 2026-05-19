# CloudGuardMonitor

Most breaches on AWS are caused by misconfiguration. This tool scans your AWS environment for misconfigurations to prevent vulnerabilities.

## Technologies Used

- Python 3.8+
- Boto3
- AWS CLI

## AWS Services Scanned

- IAM
- S3
- EC2

## Security Checks

- [IAM] Root account MFA status
- [IAM] Account password policy strength
- [S3] Public access block configuration
- [EC2] Security groups open to 0.0.0.0/0 on port 22

## Prerequisites

- Python 3.8 or higher
- AWS account with appropriate permissions
- AWS CLI installed and configured

## Installation

1. Clone the repository

```bash
git clone https://github.com/ByteBug64/CloudGuardMonitor.git
cd CloudGuardMonitor
```

2. Create and activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies

```bash
pip install boto3 rich
```

4. Configure AWS credentials

```bash
aws configure
```

## Usage

Run all scanners and generate findings report:

```bash
python main.py
```

Results are saved to `findings.json` in the project root.

## Sample Output

```json
[
  {
    "severity": "INFO",
    "title": "Root MFA is Enabled",
    "status": "PASS"
  },
  {
    "severity": "CRITICAL",
    "title": "No password policy exists on this account",
    "status": "FAIL"
  },
  {
    "severity": "CRITICAL",
    "title": "Bucket elasticbeanstalk-us-east-1-886375649091 has public ACLs enabled",
    "status": "FAIL"
  },
  {
    "severity": "CRITICAL",
    "title": "Security Group sg-0fb4dcb5b11283eba has port 22 open to the World",
    "status": "FAIL"
  }
]
```

## Project Structure

CloudGuardMonitor/
├── main.py # Runs all scanners and saves report
├── findings.json # Generated security findings report
└── scanners/
├── iam_scanner.py # IAM security checks
├── s3_scanner.py # S3 security checks
└── ec2_scanner.py # EC2 security checks

## Author

ByteBug — AWS Cloud Security Engineer Project

import json
from scanners.iam_scanner import check_mfa, check_password_policy
from scanners.s3_scanner import check_public_access_block
from scanners.ec2_scanner import check_security_groups

with open('findings.json', 'w') as f:
    json.dump(check_mfa() + check_password_policy() + check_public_access_block() + check_security_groups(), f, indent = 2)
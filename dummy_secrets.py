# dummy_secrets.py - A file full of DUMMY secrets for testing scanners

import os

# 1. AWS Credentials
aws_access_key_id = "AKIAIOSFODNN7EXAMPLE" # Standard AWS Access Key ID format
aws_secret_access_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY" # Standard AWS Secret Access Key format
os.environ['AWS_SESSION_TOKEN'] = "AQoDYXdzEPT//////////wEXAMPLEtcAEXAMPLE" # AWS Session Token

# 2. Generic API Keys
api_key = "da39a3ee5e6b4b0d3255bfef95601890afd80709" # Looks like a hex API key (e.g., SHA1)
another_api_key = "sk_live_abcdefghijklmnopqrstuvwxyz1234567890" # Stripe-like live key
service_token = "ghp_aBcDeFgHiJkLmNoPqRsTuVwXyZaBcDeFgHiJkLmN" # GitHub Personal Access Token format
HEROKU_API_KEY = "52072a28-400a-4ea8-99f0-e1b3a9d9cb65" # Heroku API Key (UUID format)
SENDGRID_API_KEY = "SG.****************************************************************.*******************************************" # SendGrid format (often partially masked in logs, but full key here)

# 3. Database Connection Strings (with credentials)
db_password = "mySuperSecurePassword123!"
DATABASE_URL = "postgres://user:password123@host:port/database"
MONGO_URI = "mongodb+srv://myuser:MyStrongMongoDB_Passw0rd@cluster0.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

# 4. Private Keys (often multi-line)
# This is a very common format for RSA private keys
rsa_private_key = """-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAy2GpA3f3oGfLYUXScK0k58x9qC9zI1u3Q5n... (dummy content)
... many lines of base64 encoded data ...
-----END RSA PRIVATE KEY-----"""

# Sometimes found in comments or as strings directly
ssh_private_key_content = "-----BEGIN OPENSSH PRIVATE KEY-----\nb3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABFwAAAAdzc2gtcn\nNhAAAAAwEAAQAAAQEAvwAA... (dummy content)\n-----END OPENSSH PRIVATE KEY-----"

# 5. Generic Passwords / Credentials in code
USERNAME = "admin"
PASSWORD = "Password123" # A common weak password example
SECRET_PHRASE = "OpenSesameForReal"

# 6. OAuth Tokens
oauth_token = "ya29.a0AfH6SMDz_AbCdEfGhIjKlMnOpQrStUvWxYz1234567890" # Google OAuth like token
bearer_token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c" # JWT Token

# 7. Slack Tokens (legacy and new formats)
slack_legacy_token = "xoxp-123456789012-123456789012-123456789012-abcdef1234567890abcdef1234567890"
slack_bot_token = "xoxb-987654321098-987654321098-aBcDeFgHiJkLmNoPqRsT"
slack_webhook_url = "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"

# 8. Twilio Credentials
TWILIO_ACCOUNT_SID = "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" # x's represent hex, actual SIDs are AC + 32 hex chars
TWILIO_AUTH_TOKEN = " SKxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" # Often starts with SK + 32 hex chars

# 9. High Entropy Strings (that might be generic secrets)
# These are harder to detect with simple regex and might rely on entropy calculations
# or very generic patterns for long alphanumeric strings.
potential_generic_secret = "8mGz8c2aK6nB4gV0jL9sQ3wF7rP1oE5uI2xY"
another_random_string = "ThisIsNotASecretButItIsLongAndLooksRandomPqRsTuVwXyZaBcDeFgHiJkLmN" # Example of a potential false positive for entropy.

# 10. Secrets in Comments (often overlooked)
# TODO: Remove this before production! API_KEY_TEMP = "temp_dev_key_12345_abcde"
# Old credentials, do not use: old_ftp_user = "ftp_user", old_ftp_pass = "ftp_password_123"

# 11. URLs with embedded credentials
ftp_url_with_creds = "ftp://user:verysecret@ftp.example.com/"
http_basic_auth_url = "https://user:P@$$wOrd@api.example.com/data"

# 12. Cloudflare API Key
CLOUDFLARE_API_KEY = "c2547eb745079dac9320b638f5e225cf483cc5cfdda41" # Example format
CLOUDFLARE_AUTH_EMAIL = "user@example.com"

# 13. Mailgun API Key
MAILGUN_API_KEY = "key-abcdef1234567890abcdef1234567890" # Common Mailgun key format

# 14. Artifactory API Key
artifactory_api_key = "AKCabcdefghijklmno1234567890ABCDEFGHIJKLMNO" # Example Artifactory key format

print("This dummy file contains various types of placeholder secrets for testing.")

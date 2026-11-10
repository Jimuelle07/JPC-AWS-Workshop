"""Run this FIRST. It checks your setup and makes one small call to Amazon Bedrock.

    python check_setup.py

If everything is fine you will see a short greeting from the model and the
words "Setup OK". If not, read the hint it prints.
"""

import os
import sys

from config import MODEL_ID, REGION


def fail(message):
    print("\nSetup problem: " + message)
    sys.exit(1)


print("Python version:", sys.version.split()[0])
if sys.version_info < (3, 10):
    fail("Python 3.10 or newer is required. Install a newer Python and try again.")

print("Region:", REGION)
print("Model ID:", MODEL_ID)

has_key = bool(os.getenv("AWS_BEARER_TOKEN_BEDROCK"))
has_iam = bool(os.getenv("AWS_ACCESS_KEY_ID") and os.getenv("AWS_SECRET_ACCESS_KEY"))
if not (has_key or has_iam):
    fail(
        "No AWS credentials found. Set AWS_BEARER_TOKEN_BEDROCK to your Bedrock "
        "API key (see docs/00-pre-work.md, step 5), then run this again."
    )
print("Credentials: found (" + ("Bedrock API key" if has_key else "access keys") + ")")

try:
    import boto3
    from botocore.exceptions import ClientError
except ImportError:
    fail("boto3 is not installed. Activate your virtual environment and run: pip install -r requirements.txt")

client = boto3.client("bedrock-runtime", region_name=REGION)

try:
    response = client.converse(
        modelId=MODEL_ID,
        messages=[{"role": "user", "content": [{"text": "Say hello to a college student in one short sentence."}]}],
        inferenceConfig={"maxTokens": 100},
    )
except ClientError as error:
    code = error.response.get("Error", {}).get("Code", "")
    detail = error.response.get("Error", {}).get("Message", str(error))
    hints = {
        "AccessDeniedException": "Your key or role is not allowed to use this model. Ask the facilitator, or check the model is available in your Region.",
        "ValidationException": "The model ID or Region looks wrong. Copy the exact ID from the Bedrock console and set MODEL_ID.",
        "ResourceNotFoundException": "That model was not found in this Region. Check MODEL_ID and AWS_REGION.",
        "ThrottlingException": "Too many requests right now. Wait a few seconds and run it again.",
        "UnrecognizedClientException": "Your credentials were rejected. Create a fresh Bedrock API key and set it again.",
    }
    print("\nBedrock returned an error: " + code)
    print(detail)
    print("\nHint: " + hints.get(code, "Show this message to a volunteer."))
    sys.exit(1)
except Exception as error:  # network problems, bad key format, and so on
    fail("Could not reach Bedrock. " + str(error))

reply = response["output"]["message"]["content"][0]["text"]
print("\nModel says: " + reply.strip())
print("\nSetup OK. You are ready for the workshop.")

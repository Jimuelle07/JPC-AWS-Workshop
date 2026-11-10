"""Shared settings for every workshop script.

Change these with environment variables, no need to edit this file:

    AWS_REGION  the AWS Region where you use Amazon Bedrock
    MODEL_ID    the Bedrock model (or inference profile) ID to call

The defaults below are a starting point. The facilitator will confirm the
exact MODEL_ID and Region on workshop day. If step0_check_setup.py says the model
was not found, copy the correct ID from the Bedrock console and set MODEL_ID.
"""

import os

REGION = os.getenv("AWS_REGION", "ap-southeast-1")
MODEL_ID = os.getenv("MODEL_ID", "apac.amazon.nova-lite-v1:0")

import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

# Load environment variables from .env file
load_dotenv()

def validate_resource_group(resource_group_name):
    """
    Validates the existence of an Azure Resource Group.

    Args:
        resource_group_name (str): The name of the Azure Resource Group to check.

    Returns:
        bool: True if the Resource Group exists, False otherwise.
    """
    try:
        # Use DefaultAzureCredential for authentication
        credential = DefaultAzureCredential()

        # Get subscription ID from environment variable
        subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID")
        if not subscription_id:
            print("Error: AZURE_SUBSCRIPTION_ID environment variable is not set.")
            return False

        # Create a Resource Management client
        resource_client = ResourceManagementClient(credential, subscription_id)

        # Attempt to get the resource group
        resource_client.resource_groups.get(resource_group_name)

        return True
    except Exception as e:
        print(f"Error validating Resource Group: {e}")  # Print the error message
        return False


def main():
    """
    Main function to take resource group name from the .env file and validate.
    """
    resource_group_name = os.environ.get("AZURE_RESOURCE_GROUP_NAME")
    if not resource_group_name:
        print("Error: AZURE_RESOURCE_GROUP_NAME environment variable is not set.")
        return

    if validate_resource_group(resource_group_name):
        print(f"Success: Azure Resource Group '{resource_group_name}' exists.")
    else:
        print(f"Failure: Azure Resource Group '{resource_group_name}' does not exist or is inaccessible.")


if __name__ == "__main__":
    main()
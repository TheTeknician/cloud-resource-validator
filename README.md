# Simple Azure Resource Validation Tool

## What's This?

This Python script is a basic tool to check if a specific Azure Resource Group exists in Microsoft Azure. It's a simple example of how you can interact with cloud infrastructure programmatically, and it demonstrates fundamental concepts useful in various cloud-related roles.

## Why Did I Make It?

I put this together to learn and demonstrate:

*   How to interact with Azure's Resource Manager API using Python. This is essential for managing Azure resources through code.
*   How to easily authenticate to Azure using `DefaultAzureCredential`. This approach simplifies authentication in many Azure development scenarios.
*   How to perform a simple check – in this case, verifying the presence of a Resource Group. This is a common task in cloud management.
*   How to handle errors from the Azure API in a robust manner.
*   How to manage configuration settings, such as subscription IDs and resource group names, using environment variables.

## What You Need Before You Start

*   An Azure subscription. If you don't have one, you can create a free Azure account.
*   Python 3 installed on your computer.
*   The following Python packages: `azure-identity`, `azure-mgmt-resource`, and `python-dotenv`. You'll install these in the next step.
*   The Azure CLI tool installed and configured. You'll also need to be logged in to Azure using the Azure CLI (`az login`).

## How to Get Started

1.  **Download the code:**

    ```bash
    git clone <your_repository_url>
    cd cloud-resource-validator
    ```

2.  **Install the required Python packages:**

    ```bash
    pip install azure-identity azure-mgmt-resource python-dotenv
    ```

3.  **Configure your Azure credentials:**

    *   First, ensure that you've authenticated with Azure using the CLI by running `az login`.
    *   Next, create a file named `.env` in the project directory. Add your `AZURE_SUBSCRIPTION_ID` and `AZURE_RESOURCE_GROUP_NAME` to this file:

        ```
        AZURE_SUBSCRIPTION_ID=YOUR_AZURE_SUBSCRIPTION_ID
        AZURE_RESOURCE_GROUP_NAME=rg-validation-test
        ```

        **Important:** Protect your credentials! Never commit the `.env` file to a public repository.

4.  **Run the script:**

    ```bash
    python validator.py
    ```

    The script will check for the existence of the Azure Resource Group and report whether it was found.

## Possible Extensions

Here are some potential ways to expand upon this project:

*   Add support for other Azure resource types (e.g., virtual machines, storage accounts).
*   Explore integration with other cloud platforms (e.g., AWS, Google Cloud).
*   Implement more sophisticated validation checks, such as verifying resource configurations.
*   Integrate with testing frameworks to automate validation procedures.
*   Add comprehensive logging capabilities.
*   Develop a command-line interface for improved usability.

## Contributing

Contributions are welcome! Feel free to submit pull requests with enhancements or bug fixes.

## Author

[Charles Oluwawo] - [https://github.com/TheTeknician]


# FlexiAI

FlexiAI is a robust AI framework designed to efficiently manage interactions with both OpenAI and Azure OpenAI services. Featuring an advanced Retrieval-Augmented Generation (RAG) module, this framework provides developers with the tools to seamlessly integrate advanced AI functionalities into their applications, leveraging the extensive capabilities of OpenAI and Azure OpenAI for enhanced performance and scalability.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Multi-Platform Support**: Seamlessly integrates with both OpenAI and Azure OpenAI services, ensuring flexibility and broad compatibility.
- **Configurable and Extensible**: Offers an easily configurable and highly extensible framework, allowing customization to meet specific project needs and scalability requirements.
- **Robust Logging**: Incorporates comprehensive logging capabilities, facilitating effective debugging and monitoring for a smooth development and operational experience.
- **Task Management**: Efficiently manages and executes a wide range of tasks, ensuring streamlined operations and enhanced productivity.
- **Retrieval-Augmented Generation (RAG)**: The framework empowers AI assistants to dynamically call external functions or services, enabling real-time retrieval of information. This capability allows the assistant to handle complex operations efficiently, making the solution more versatile and powerful.
- **Examples and Tests**: Provides a rich set of example scripts and comprehensive tests, enabling quick onboarding and ensuring reliable performance from the outset.
- **Secure and Scalable**: Designed with security and scalability in mind, making it suitable for both small projects and large enterprise applications.
- **Community-Driven**: Actively maintained and supported by a community of developers, ensuring continuous improvement and up-to-date features.

## Installation

### Install with `pip`

To install the FlexiAI framework using `pip`, simply run:

```bash
pip install flexiai
```

After installing, create a `.env` file in your project root directory with the following template:

```bash
# ========================== #
# Example .env file template #
# ========================== #

# Your OpenAI API key
OPENAI_API_KEY='your_openai_api_key_here'

# Your Azure OpenAI API key
AZURE_OPENAI_API_KEY='your_azure_openai_api_key_here'
# Your Azure OpenAI endpoint
AZURE_OPENAI_ENDPOINT='your_azure_openai_endpoint_here'
# Azure OpenAI API version
AZURE_OPENAI_API_VERSION='2024-05-01-preview'

# Credential type (either 'openai' or 'azure')
CREDENTIAL_TYPE='openai'
```

### Install from Source

To install the FlexiAI framework from source, clone the repository and use the provided setup script.

```bash
git clone https://github.com/SavinRazvan/flexiai.git
cd flexiai
python setup.py install
```

Alternatively, you can install the required dependencies using `pip`.

```bash
pip install -r requirements.txt
```

## Setup

Before using FlexiAI, set up your environment variables. You can use a `.env` file in the root directory. Here's an example template:

```bash
# Your OpenAI API key
OPENAI_API_KEY='your_openai_api_key_here'

# Your Azure OpenAI API key
AZURE_OPENAI_API_KEY='your_azure_openai_api_key_here'
# Your Azure OpenAI endpoint
AZURE_OPENAI_ENDPOINT='your_azure_openai_endpoint_here'
# Azure OpenAI API version
AZURE_OPENAI_API_VERSION='2024-05-01-preview'

# Credential type (either 'openai' or 'azure')
CREDENTIAL_TYPE='openai'
```

For more detailed setup instructions, including using virtual environments and troubleshooting, refer to the [Setup Guide](docs/setup.md).

## Usage

### Basic Usage

Here’s a quick example of how to use FlexiAI to interact with OpenAI:

```python
import logging
import os
import platform
from flexiai.core.flexiai_client import FlexiAI
from flexiai.config.logging_config import setup_logging

def clear_console():
    """Clears the console depending on the operating system."""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def main():
    # Setup logging
    setup_logging()

    # Initialize FlexiAI
    flexiai = FlexiAI()

    # Use the given assistant ID
    assistant_id = 'asst_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' # Replace with the actual assistant ID
    
    # Create a new thread
    try:
        thread = flexiai.create_thread()
        thread_id = thread.id
        logging.info(f"Created thread with ID: {thread_id}")
    except Exception as e:
        logging.error(f"Error creating thread: {e}")
        return

    # Variable to store all messages
    all_messages = []
    seen_message_ids = set()

    # Loop to continuously get user input and interact with the assistant
    while True:
        # Get user input
        user_message = input("You: ")

        # Exit the loop if the user types 'exit'
        if user_message.lower() == 'exit':
            print("Exiting...")
            break

        # Run the thread and handle required actions
        try:
            flexiai.create_advanced_run(assistant_id, thread_id, user_message)
            messages = flexiai.retrieve_messages(thread_id, limit=2)  
            
            # Store the extracted messages
            for msg in messages:
                if msg['message_id'] not in seen_message_ids:
                    all_messages.append(msg)
                    seen_message_ids.add(msg['message_id'])

            # Clear console and print the stored messages in the desired format
            clear_console()
            for msg in all_messages:
                role = "🤖 Assistant" if msg['role'] == "assistant" else "🧑 You"
                print(f"{role}: {msg['content']}")
        except Exception as e:
            logging.error(f"Error running thread: {e}")

if __name__ == "__main__":
    main()
```

### Creating `user_flexiai_rag` Directory and Files

In your project root directory, you have to create the following structure to enable Retrieval-Augmented Generation (RAG) module:

```
project_root/
├── user_flexiai_rag/
│   ├── user_function_mapping.py
│   ├── user_helpers.py
│   └── user_task_manager.py
└── .env
```

#### user_flexiai_rag/user_function_mapping.py

```python
from user_flexiai_rag.user_task_manager import UserTaskManager

def register_user_tasks():
    """
    Register user-defined tasks with the FlexiAI framework.

    Returns:
        tuple: A tuple containing the personal function mappings and assistant
        function mappings.
    """
    # Initialize UserTaskManager to access user-defined tasks
    task_manager = UserTaskManager()

    personal_function_mapping = {
        'search_youtube': task_manager.search_youtube,
        'search_products': task_manager.search_products,
        # Add other personal functions here
        # 'my_custom_task': task_manager.my_custom_task
    }

    assistant_function_mapping = {
        # Add other functions that call assistants here -> the functions must end with "_assistant"
        # 'call_example_assistant': task_manager.call_example_assistant,
    }

    return personal_function_mapping, assistant_function_mapping
```

#### user_flexiai_rag/user_helpers.py

```python
import subprocess
import logging

def format_product(product):
    """
    Formats product details into a readable string.

    Args:
        product (dict): A dictionary containing product details. Expected keys are 'product_id', 
                        'product_name', 'brand', 'price', 'stock', 'rating', 'warranty_years', 
                        'category', 'release_date', and 'customer_reviews'.

    Returns:
        str: A formatted string containing the product details.
    """
    return (
        f"Product ID: {product['product_id']}\n"
        f"Product Name: {product['product_name']}\n"
        f"Brand: {product['brand']}\n"
        f"Price: ${product['price']}\n"
        f"Stock: {product['stock']}\n"
        f"Rating: {product['rating']}\n"
        f"Warranty Years: {product['warranty_years']}\n"
        f"Category: {product['category']}\n"
        f"Release Date: {product['release_date']}\n"
        f"Customer Reviews: {product['customer_reviews']}\n\n"
    )
```

#### user_flexiai_rag/user_task_manager.py

```python
import logging
import subprocess
import urllib.parse
import pandas as pd
from config.logging_config import setup_logging
from user_flexiai_rag.user_helpers import format_product

# Set up logging using your custom configuration
setup_logging()

class UserTaskManager:
    """
    UserTaskManager class handles user

-defined tasks.
    """

    def __init__(self):
        """
        Initializes the UserTaskManager instance, setting up the logger.
        """
        self.logger = logging.getLogger(__name__)

    def search_youtube(self, query):
        """
        Searches YouTube for the given query and opens the search results page
        in the default web browser.

        Args:
            query (str): The search query string.

        Returns:
            dict: A dictionary containing the status, message, and result (URL)
        """
        if not query:
            return {
                "status": False,
                "message": "Query cannot be empty.",
                "result": None
            }

        try:
            # Normalize spaces to ensure consistent encoding
            query_normalized = query.replace(" ", "+")
            query_encoded = urllib.parse.quote(query_normalized)
            youtube_search_url = (
                f"https://www.youtube.com/results?search_query={query_encoded}"
            )
            self.logger.info(f"Opening YouTube search for query: {query}")

            # Use PowerShell to open the URL
            subprocess.run(
                ['powershell.exe', '-Command', 'Start-Process', youtube_search_url],
                check=True
            )

            self.logger.info("YouTube search page opened successfully.")
            return {
                "status": True,
                "message": "YouTube search page opened successfully.",
                "result": youtube_search_url
            }
        except subprocess.CalledProcessError as e:
            error_message = f"Subprocess error: {str(e)}"
            self.logger.error(error_message, exc_info=True)
            return {
                "status": False,
                "message": error_message,
                "result": None
            }
        except Exception as e:
            error_message = f"Failed to open YouTube search for query: {query}. Error: {str(e)}"
            self.logger.error(error_message, exc_info=True)
            return {
                "status": False,
                "message": error_message,
                "result": None
            }

    def search_products(self, product_id=None, product_name=None, brand=None, price_range=None, stock=None, rating_range=None, warranty_years=None, category=None, release_date=None, customer_reviews=None):
        """
        Searches for products in the products CSV file based on the given criteria.

        Args:
            product_id (int, optional): The ID of the product.
            product_name (str, optional): The name of the product.
            brand (str or list, optional): The brand of the product or a list of brands.
            price_range (tuple, optional): The price range as a tuple (min_price, max_price).
            stock (int, optional): The stock quantity.
            rating_range (tuple, optional): The rating range as a tuple (min_rating, max_rating).
            warranty_years (int, optional): The number of warranty years.
            category (str, optional): The category of the product.
            release_date (str, optional): The release date of the product.
            customer_reviews (str, optional): A substring to search for in customer reviews.

        Returns:
            dict: A dictionary containing the status, message, and result (formatted product list or None).
        """
        try:
            # Load the CSV file
            df = pd.read_csv('user_flexiai_rag/data/products.csv')

            # Apply filters based on the provided arguments
            if product_id is not None:
                df = df[df['product_id'] == product_id]
            if product_name is not None:
                df = df[df['product_name'].str.contains(product_name, case=False, na=False)]
            if brand is not None:
                if isinstance(brand, list):
                    df = df[df['brand'].isin(brand)]
                else:
                    df = df[df['brand'].str.contains(brand, case=False, na=False)]
            if price_range is not None:
                if isinstance(price_range, tuple) and len(price_range) == 2:
                    df = df[(df['price'] >= price_range[0]) & (df['price'] <= price_range[1])]
                else:
                    error_message = "Invalid price range. Provide a tuple with (min_price, max_price)."
                    self.logger.error(error_message)
                    return {
                        "status": False,
                        "message": error_message,
                        "result": None
                    }
            if stock is not None:
                df = df[df['stock'] == stock]
            if rating_range is not None:
                if isinstance(rating_range, tuple) and len(rating_range) == 2:
                    df = df[(df['rating'] >= rating_range[0]) & (df['rating'] <= rating_range[1])]
                else:
                    error_message = "Invalid rating range. Provide a tuple with (min_rating, max_rating)."
                    self.logger.error(error_message)
                    return {
                        "status": False,
                        "message": error_message,
                        "result": None
                    }
            if warranty_years is not None:
                df = df[df['warranty_years'] == warranty_years]
            if category is not None:
                df = df[df['category'].str.contains(category, case=False, na=False)]
            if release_date is not None:
                df = df[df['release_date'] == release_date]
            if customer_reviews is not None:
                df = df[df['customer_reviews'].str.contains(customer_reviews, case=False, na=False)]

            # Check if any results are found
            if df.empty:
                return {
                    "status": False,
                    "message": "No products found matching the criteria.",
                    "result": None
                }

            # Convert the filtered DataFrame to a list of dictionaries
            results = df.to_dict(orient='records')
            # Format each product using the format_product function
            formatted_results = [format_product(product) for product in results]
            return {
                "status": True,
                "message": f"Found {len(formatted_results)} product(s) matching the criteria.",
                "result": formatted_results
            }
        except FileNotFoundError:
            error_message = "The products.csv file was not found."
            self.logger.error(error_message, exc_info=True)
            return {
                "status": False,
                "message": error_message,
                "result": None
            }
        except pd.errors.EmptyDataError:
            error_message = "The products.csv file is empty."
            self.logger.error(error_message, exc_info=True)
            return {
                "status": False,
                "message": error_message,
                "result": None
            }
        except Exception as e:
            error_message = f"An error occurred while searching for products: {str(e)}"
            self.logger.error(error_message, exc_info=True)
            return {
                "status": False,
                "message": error_message,
                "result": None
            }

    # User can add more custom tasks (assistant personal functions or functions to call other assistants)
```

For detailed usage examples and advanced functionalities, refer to the [Usage Guide](docs/usage.md).

## Documentation

The FlexiAI framework comes with comprehensive documentation to help you get started and make the most out of its capabilities:

- [API Reference](docs/api_reference.md)
- [Setup Guide](docs/setup.md)
- [Usage Guide](docs/usage.md)
- [Contributing Guide](docs/contributing.md)

## Contributing

We welcome contributions from the community. If you want to contribute to FlexiAI, please read our [Contributing Guide](docs/contributing.md) to get started.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.txt) file for details.

## Contact

For any inquiries or support, please contact Savin Ionut Razvan at razvan.i.savin@gmail.com.

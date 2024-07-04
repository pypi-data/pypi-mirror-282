# FlexiAI API Reference

This document provides a detailed reference of the FlexiAI framework's API. It includes descriptions, usage examples, and information on how to extend the functionality with custom tasks.

## Table of Contents

1. [FlexiAI Class](#flexiai-class)
    - [__init__()](#init)
    - [_initialize_openai_client()](#initialize_openai_client)
    - [_initialize_azure_openai_client()](#initialize_azure_openai_client)
    - [create_thread()](#create_thread)
    - [add_user_message(thread_id, user_message)](#add_user_message)
    - [wait_for_run_completion(thread_id)](#wait_for_run_completion)
    - [create_run(assistant_id, thread_id)](#create_run)
    - [create_advanced_run(assistant_id, thread_id, user_message)](#create_advanced_run)
    - [retrieve_messages(thread_id, limit=20)](#retrieve_messages)
2. [Implementing RAG in FlexiAI](#implementing-rag-in-flexiai)
    - [TaskManager](#taskmanager-assistanttask_managerpy)
    - [Function Mapping](#function-mapping-assistantfunction_mappingpy)
    - [User Function Mapping](#user-function-mapping-user_flexiai_raguser_function_mappingpy)
    - [User Task Manager](#user-task-manager-user_flexiai_raguser_task_managerpy)
3. [Configuration](#configuration)
    - [Config Class](#config-class)

---

## FlexiAI Class

The `FlexiAI` class is a core component of the FlexiAI framework, designed to facilitate seamless interaction with both OpenAI and Azure OpenAI services. It provides robust capabilities for dynamic thread management, user message handling, and the execution of threads with various AI assistants. The class also incorporates advanced Retrieval-Augmented Generation (RAG) capabilities, enabling the assistant to dynamically call external functions or services.

### `__init__()`

Initialize the FlexiAI client based on the specified credential type in the configuration.

- **Raises**:
  - `ValueError`: If the specified credential type is unsupported.

**Example Usage**:
```python
from flexiai.core.flexiai_client import FlexiAI

flexiai = FlexiAI()
```

### `_initialize_openai_client()`

Initializes the OpenAI client using the API key from the configuration.

- **Returns**:
  - `OpenAI`: Initialized OpenAI client.

- **Raises**:
  - `ValueError`: If the OpenAI API key is not set.

This method is called internally during the initialization and does not need to be called directly.

### `_initialize_azure_openai_client()`

Initializes the Azure OpenAI client using the API key, endpoint, and API version from the configuration.

- **Returns**:
  - `AzureOpenAI`: Initialized Azure OpenAI client.

- **Raises**:
  - `ValueError`: If the Azure OpenAI API key, endpoint, or API version is not set.

This method is called internally during the initialization and does not need to be called directly.

### `create_thread()`

Creates a new thread.

- **Returns**:
  - `object`: The newly created thread object.

- **Raises**:
  - `OpenAIError`: If the API call to create a new thread fails.
  - `Exception`: If an unexpected error occurs.

**Example Usage**:
```python
thread = flexiai.create_thread()
print(f"Created thread with ID: {thread.id}")
```

### `add_user_message(thread_id, user_message)`

Adds a user message to a specified thread.

- **Args**:
  - `thread_id (str)`: The ID of the thread.
  - `user_message (str)`: The user's message content.

- **Returns**:
  - `object`: The message object that was added to the thread.

- **Raises**:
  - `OpenAIError`: If the API call to add a user message fails.
  - `Exception`: If an unexpected error occurs.

**Example Usage**:
```python
message = flexiai.add_user_message(thread_id="thread_id_here", user_message="Hello, world!")
print(f"Added message with ID: {message.id}")
```

### `wait_for_run_completion(thread_id)`

Waits for any active run in the thread to complete.

- **Args**:
  - `thread_id (str)`: The ID of the thread.

- **Raises**:
  - `OpenAIError`: If the API call to retrieve thread runs fails.
  - `Exception`: If an unexpected error occurs.

**Example Usage**:
```python
flexiai.wait_for_run_completion(thread_id="thread_id_here")
```

### `create_run(assistant_id, thread_id)`

Creates and runs a thread with the specified assistant, handling required actions.

- **Args**:
  - `assistant_id (str)`: The ID of the assistant.
  - `thread_id (str)`: The ID of the thread.

- **Returns**:
  - `object`: The run object.

- **Raises**:
  - `OpenAIError`: If any API call within this function fails.
  - `Exception`: If an unexpected error occurs.

**Example Usage**:
```python
run = flexiai.create_run(assistant_id="assistant_id_here", thread_id="thread_id_here")
print(f"Run ID: {run.id}, Status: {run.status}")
```

### `create_advanced_run(assistant_id, thread_id, user_message)`

Creates and runs a thread with the specified assistant, user message, and handling required actions.

- **Args**:
  - `assistant_id (str)`: The ID of the assistant.
  - `thread_id (str)`: The ID of the thread.
  - `user_message (str)`: The user's message content.

- **Returns**:
  - `object`: The run object.

- **Raises**:
  - `OpenAIError`: If any API call within this function fails.
  - `Exception`: If an unexpected error occurs.

**Example Usage**:
```python
run = flexiai.create_advanced_run(assistant_id="assistant_id_here", thread_id="thread_id_here", user_message="Hello! What is your name?")
print(f"Run ID: {run.id}, Status: {run.status}")
```

### `retrieve_messages(thread_id, limit=20)`

Retrieves the message objects from a specified thread.

- **Args**:
  - `thread_id (str)`: The ID of the thread.
  - `limit (int, optional)`: The number of messages to retrieve. Defaults to 20.

- **Returns**:
  - `list`: A list of dictionaries containing the message_id, role, and content.

- **Raises**:
  - `OpenAIError`: If the API call to retrieve messages fails.
  - `Exception`: If an unexpected error occurs.

**Example Usage**:
```python
messages = flexiai.retrieve_messages(thread_id="thread_id_here", limit=2)
for message in messages:
    print(message)
```

## Implementing RAG in FlexiAI

### Introduction

Retrieval-Augmented Generation (RAG) is a process where the assistant dynamically calls external functions or services to retrieve information that is not readily available in its training data. This is particularly useful for tasks that require up-to-date information or complex operations.

### TaskManager (`assistant/task_manager.py`)

#### Description

The `TaskManager` class handles tasks related to searching YouTube, searching products, and integrates user-defined tasks.

#### Methods

##### `__init__()`

Initialize the TaskManager.

- **Description:** Sets up the logger and initializes user-defined tasks.
- **Example Usage:**
  ```python
  from flexiai.assistant.task_manager import TaskManager

  task_manager = TaskManager()
  ```

### Function Mapping (`assistant/function_mapping.py`)

#### Description

Function mapping connects function names to actual Python functions defined in the `TaskManager`. This mapping allows the assistant to call the appropriate function and perform the required action.

#### Methods

##### `get_function_mappings(task_manager)`

Retrieve function mappings.

- **Description:** Merges internal and user-defined function mappings.
- **Example Usage:**
  ```python
  from flexiai.assistant.function_mapping import get_function_mappings

  personal_functions, assistant_functions = get_function_mappings(task_manager)
  ```

### User Function Mapping (`user_flexiai_rag/user_function_mapping.py`)

#### Description

User-defined functions are registered to the FlexiAI framework through this module.

#### Methods

##### `register_user_tasks()`

Register user-defined tasks.

- **Description:** Integrates user-defined tasks with the FlexiAI framework.
- **Example Usage:**
  ```python
  from flexiai.user_flexiai_rag.user_function_mapping import register_user_tasks

  personal_functions, assistant_functions = register_user_tasks()
  ```

### User Task Manager (`user_flexiai_rag/user_task_manager.py`)

#### Description

The `UserTaskManager` class handles user-defined tasks, including searching YouTube and products.

#### Methods

##### `__init__()`

Initialize the UserTaskManager.

- **Description:** Sets up the logger.
- **Example Usage:**
  ```python
  from flexiai.user_flexiai_rag.user_task_manager import UserTaskManager

  user_task_manager = UserTaskManager()
  ```

##### `search_youtube(query)`

Search YouTube for a

 given query.

- **Description:** Searches YouTube for the given query and opens the search results page in the default web browser.
- **Args:**
  - `query (str)`: The search query string.
- **Returns:**
  - `dict`: A dictionary containing the status, message, and result (URL).
- **Example Usage:**
  ```python
  result = user_task_manager.search_youtube(query="Python tutorials")
  print(result)
  ```

##### `search_products(...)`

Search for products based on various criteria.

- **Description:** Searches for products in the products CSV file based on the given criteria.
- **Args:**
  - Various product attributes such as `product_id`, `product_name`, `brand`, `price_range`, `stock`, `rating_range`, `warranty_years`, `category`, `release_date`, `customer_reviews`.
- **Returns:**
  - `dict`: A dictionary containing the status, message, and result (formatted product list or None).
- **Example Usage:**
  ```python
  result = user_task_manager.search_products(product_name="Laptop")
  print(result)
  ```

## Configuration

### Introduction

The configuration setup for FlexiAI involves setting environment variables and configuring logging.

### Config Class (`flexiai/config/config.py`)

#### Description

The `Config` class handles the configuration settings for the FlexiAI framework, loading values from environment variables.

#### Attributes

- `CREDENTIAL_TYPE`: The type of credentials being used (e.g., 'openai', 'azure').
- `OPENAI_API_KEY`: The API key for OpenAI.
- `AZURE_OPENAI_API_KEY`: The API key for Azure OpenAI.
- `AZURE_OPENAI_ENDPOINT`: The endpoint for Azure OpenAI.
- `AZURE_OPENAI_API_VERSION`: The API version for Azure OpenAI.

**Example .env Configuration**:
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

By following this guide, you can effectively implement and configure Retrieval-Augmented Generation (RAG) within the FlexiAI framework.

# API Reference

This section provides a detailed reference of the FlexiAI framework's API.

## FlexiAI Class

The `FlexiAI` class is a core component of the FlexiAI framework, designed to facilitate seamless interaction with both OpenAI and Azure OpenAI services. It provides robust capabilities for dynamic thread management, user message handling, and the execution of threads with various AI assistants. The class also incorporates advanced Retrieval-Augmented Generation (RAG) capabilities, enabling the assistant to dynamically call external functions or services. This allows for the retrieval of real-time information and execution of complex operations, significantly enhancing the assistant's ability to perform diverse and sophisticated tasks. The `FlexiAI` class is essential for developers looking to build scalable and flexible AI solutions that integrate seamlessly with state-of-the-art AI services.

### Methods

#### `__init__()`

Initialize the FlexiAI client based on the specified credential type in the configuration.

- **Raises**:
  - `ValueError`: If the specified credential type is unsupported.

#### `_initialize_openai_client()`

Initializes the OpenAI client using the API key from the configuration.

- **Returns**:
  - `OpenAI`: Initialized OpenAI client.

- **Raises**:
  - `ValueError`: If the OpenAI API key is not set.

#### `_initialize_azure_openai_client()`

Initializes the Azure OpenAI client using the API key, endpoint, and API version from the configuration.

- **Returns**:
  - `AzureOpenAI`: Initialized Azure OpenAI client.

- **Raises**:
  - `ValueError`: If the Azure OpenAI API key, endpoint, or API version is not set.

#### `create_thread()`

Create a new thread.

- **Returns**:
  - `object`: The newly created thread object.

- **Raises**:
  - `OpenAIError`: If the API call to create a new thread fails.
  - `Exception`: If an unexpected error occurs.

#### `add_user_message(thread_id, user_message)`

Add a user message to a specified thread.

- **Args**:
  - `thread_id (str)`: The ID of the thread.
  - `user_message (str)`: The user's message content.

- **Returns**:
  - `object`: The message object that was added to the thread.

- **Raises**:
  - `OpenAIError`: If the API call to add a user message fails.
  - `Exception`: If an unexpected error occurs.

#### `wait_for_run_completion(thread_id)`

Wait for any active run in the thread to complete.

- **Args**:
  - `thread_id (str)`: The ID of the thread.

- **Raises**:
  - `OpenAIError`: If the API call to retrieve thread runs fails.
  - `Exception`: If an unexpected error occurs.

#### `create_run(assistant_id, thread_id)`

Create and run a thread with the specified assistant, handling required actions.

- **Args**:
  - `assistant_id (str)`: The ID of the assistant.
  - `thread_id (str)`: The ID of the thread.

- **Returns**:
  - `object`: The run object.

- **Raises**:
  - `OpenAIError`: If any API call within this function fails.
  - `Exception`: If an unexpected error occurs.

#### `create_advanced_run(assistant_id, thread_id, user_message)`

Create and run a thread with the specified assistant, user message, and handling required actions.

- **Args**:
  - `assistant_id (str)`: The ID of the assistant.
  - `thread_id (str)`: The ID of the thread.
  - `user_message (str)`: The user's message content.

- **Returns**:
  - `object`: The run object.

- **Raises**:
  - `OpenAIError`: If any API call within this function fails.
  - `Exception`: If an unexpected error occurs.

#### `retrieve_messages(thread_id, limit=20)`

Retrieve the message objects from a specified thread.

- **Args**:
  - `thread_id (str)`: The ID of the thread.
  - `limit (int, optional)`: The number of messages to retrieve. Defaults to 20.

- **Returns**:
  - `list`: A list of dictionaries containing the message_id, role and content_value.

- **Raises**:
  - `OpenAIError`: If the API call to retrieve messages fails.
  - `Exception`: If an unexpected error occurs.

#### `handle_requires_action(run, assistant_id, thread_id)`

Handle required actions from a run.

- **Args**:
  - `run (object)`: The run object requiring actions.
  - `assistant_id (str)`: The ID of the assistant.
  - `thread_id (str)`: The ID of the thread.

- **Raises**:
  - `OpenAIError`: If the API call to submit tool outputs fails.
  - `Exception`: If an unexpected error occurs.

### Implementing RAG in FlexiAI

Retrieval-Augmented Generation (RAG) is a process where the assistant can dynamically call external functions or services to retrieve information that is not readily available in its training data. This is particularly useful for tasks that require up-to-date information or complex operations.

**Usage with `TaskManager` and `function_mapping.py` for Retrieval-Augmented Generation (RAG):**

1. **TaskManager (`assistant/task_manager.py`)**:
    - Manages tasks related to searching YouTube and products.
    - Provides methods like `search_youtube` and `search_products`, which can be mapped to functions in `function_mapping.py`.

    Users should add their custom functions in the `UserTaskManager` class within `user_flexiai_rag/user_task_manager.py`. These functions handle the business logic required to perform specific tasks.

2. **Function Mapping (`assistant/function_mapping.py`)**:
    - Maps function names to the actual functions in the `TaskManager`.
    - Distinguishes between personal functions and assistant functions.

    The `get_function_mappings` function in `function_mapping.py` is responsible for mapping the function names used by the assistant to the actual Python functions defined in the `TaskManager`. This mapping allows the assistant to call the appropriate function and perform the required action.

3. **Using `handle_requires_action`**:
    - Ensures that when a run requires action, it uses the function mappings to execute the appropriate task.
    - Submits the results of these tasks back to the OpenAI API to continue the run.

    The `handle_requires_action` method leverages the function mappings to dynamically call the required functions. It uses the function name provided by the assistant, looks it up in the mapping, and then calls the corresponding function in the `TaskManager` with the provided arguments. The results are then formatted and submitted back to the OpenAI API.

### Example Workflow

1. **Define Functions in `UserTaskManager`**:
    Define the business logic functions in `UserTaskManager` for the tasks you want to perform.

    ```python
    class UserTaskManager:
        def search_youtube(self, query):
            # Implementation of search_youtube method
            pass

        def search_products(self, **kwargs):
            # Implementation of search_products method
            pass
    ```

2. **Map Functions in `user_function_mapping.py`**:
    Map the function names to the functions defined in `UserTaskManager`.

    ```python
    def register_user_tasks():
        task_manager = UserTaskManager()
        
        personal_function_mapping = {
            'search_youtube': task_manager.search_youtube,
            'search_products': task_manager.search_products
        }

        assistant_function_mapping = {
            # Example assistant call
            #'call_example_assistant': task_manager.call_example_assistant,
        }

        return personal_function_mapping, assistant_function_mapping
    ```

3. **Handle Required Actions**:
    Use `handle_requires_action` to process the required actions by calling the mapped functions and submitting the results.

    ```python
    def handle_requires_action(self, run, assistant_id, thread_id):
        """
        Handle required actions from a run.

        This method processes the required actions for a given run. It executes the necessary functions
        and submits the outputs back to the OpenAI API.

        Args:
            run (object): The run object requiring actions.
            assistant_id (str): The ID of the assistant.
            thread_id (str): The ID of the thread.

        Raises:
            OpenAIError: If an error occurs when interacting with the OpenAI API.
            Exception: If an unexpected error occurs during the process.
        """
        self.logger.info(f"Handling required action for run ID: {run.id} with assistant ID: {assistant_id}.")
        
        # Check if the run status indicates that actions are required
        if run.status == "requires_action":
            tool_outputs = []
            
            # Iterate over each tool call that requires an output submission
            for tool_call in run.required_action.submit_tool_outputs.tool_calls:
                function_name = tool_call.function.name
                arguments = json.loads(tool_call.function.arguments)
                
                self.logger.debug(f"Function Name: {function_name}")
                self.logger.debug(f"Arguments: {arguments}")
                
                # Determine the type of action to perform
                action_type = self.determine_action_type(function_name)
                
                # Execute the appropriate function based on the action type
                if action_type == "call_assistant":
                    self.logger.debug(f"Calling another assistant with arguments: {arguments}")
                    status, message, result = self.call_assistant_with_arguments(function_name, **arguments)
                else:
                    self.logger.debug(f"Executing personal function with arguments: {arguments}")
                    status, message, result = self.execute_personal_function_with_arguments(function_name, **arguments)
                
                # Prepare the tool output for submission
                tool_output = {
                    "tool_call_id": tool_call.id,
                    "output": json.dumps({"status": status, "message": message, "result": result})
                }
                self.logger.debug(f"Tool output to be submitted: {tool_output}")
                tool_outputs.append(tool_output)
            
            # Submit the tool outputs to the OpenAI API
            try:
                self.client.beta.threads.runs.submit_tool_outputs(
                    thread_id=thread_id,
                    run_id=run.id,
                    tool_outputs=tool_outputs
                )
                self.logger.info(f"Successfully submitted tool outputs for run ID: {run.id}")
            except OpenAIError as e:
                self.logger.error(f"OpenAI API error when submitting tool outputs: {e}")
                raise
            except Exception as e:
                self.logger.error(f"General error when submitting tool outputs: {e}")
                raise
        else:
            self.logger.info(f"No required action for this run ID: {run.id}")
    ```

## Configuration

### Config Class

The `Config` class handles configuration settings for the FlexiAI framework.

#### Attributes

- `OPENAI_API_KEY`: The OpenAI API key, loaded from the environment variable.
- `AZURE_OPENAI_API_KEY`: The Azure OpenAI API key, loaded from the environment variable.
- `AZURE_OPENAI_ENDPOINT`: The Azure OpenAI endpoint, loaded from the environment variable.
- `AZURE_OPENAI_API_VERSION`: The Azure OpenAI API version, loaded from the environment variable.
- `CREDENTIAL_TYPE`: The type of credentials to use ('openai' or 'azure').

### Initialization

To set the values in the CLI, use the following commands:

```bash
export OPENAI_API_KEY='your_openai_api_key_here'
export AZURE_OPENAI_API_KEY='your_azure_openai_api_key_here'
export AZURE_OPENAI_ENDPOINT='your_azure_openai_endpoint_here'
export AZURE_OPENAI_API_VERSION='2024-05-01-preview'
export CREDENTIAL_TYPE='openai'  # or 'azure'
```

Alternatively, you can use the .env file in the root directory with the following template:

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

For more details on each method and class, refer to the source code.

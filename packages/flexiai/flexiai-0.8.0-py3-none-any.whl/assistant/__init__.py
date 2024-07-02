# assistant/__init__.py
from .task_manager import TaskManager
from .function_mapping import get_function_mappings

# Initialize TaskManager
task_manager = TaskManager()

# Get function mappings
personal_function_mapping, assistant_function_mapping = get_function_mappings(
    task_manager
)

__all__ = [
    'TaskManager',
    'personal_function_mapping',
    'assistant_function_mapping',
    'get_function_mappings',
]

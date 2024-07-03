# delta_logger

A Python library for logging messages to JSON files with rotation and validation.

## Installation

```bash
pip install dict_delta_logger
```

## Usage
```python
from delta_logger import DeltaLogger, LogMessageModel
from pydantic import BaseModel, ValidationError

logger = DeltaLogger("example_log", log_dir="logs", max_files=5)

for i in range(10):
    message = {
        "key1": f"Value {i}",
        "key2": i,
        "key3": {f"nested_key_{i:3d}": f"Nested value {i}"}
    }

    # directly log the dict message
    # delta_logger.log(message)

    class LogMessageModel(BaseModel):
        key1: str
        key2: int
        key3: Dict[str, Any]

    # Validate the message using the Pydantic model
    try:
        validated_message = LogMessageModel(**message)
        # Log the validated message
        delta_logger.log(validated_message.dict())
    except ValidationError as e:
        print(f"Validation error: {e}")

merged_logs = delta_logger.merge_logs()
print(json.dumps(merged_logs, indent=4))
```

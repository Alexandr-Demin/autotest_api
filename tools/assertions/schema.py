from typing import Any
from jsonschema import validate
from jsonschema.validators import Draft202012Validator
import allure

@allure.step("Validate JSON schema")
def validate_json_schema(instance: Any, schema: dict) -> None:
    validate(
        instance=instance,
        schema=schema,
        format_checker=Draft202012Validator.FORMAT_CHECKER,
    )
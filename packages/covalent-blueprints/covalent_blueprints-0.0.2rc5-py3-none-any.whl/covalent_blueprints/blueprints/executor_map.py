"""Executor mapping for Covalent blueprints."""

from pprint import pformat
from typing import Dict

from covalent_cloud.cloud_executor.cloud_executor import CloudExecutor

from covalent_blueprints.reader.script import CovalentScript


class ExecutorMap:
    """Custom dict-like object to contain a map of the blueprint's executors"""

    def __init__(self, script: CovalentScript):
        self._executor_map = {}

        # Map executors

        for electron_name, electron_ in script.electrons.items():
            electron_ = electron_.electron_object  # type: ignore
            executor_data = electron_.get_metadata(  # type: ignore
                "executor_data"
            )
            if not executor_data:
                raise ValueError(
                    f"Electron '{electron_name}' does not have an executor. "
                    "Please assign a CloudExecutor to this electron."
                )

            executor = CloudExecutor(
                num_cpus=executor_data["attributes"]["num_cpus"],
                memory=executor_data["attributes"]["memory"],
                num_gpus=executor_data["attributes"]["num_gpus"],
                gpu_type=executor_data["attributes"]["gpu_type"],
                env=executor_data["attributes"]["env"],
                time_limit=executor_data["attributes"]["time_limit"],
                volume_id=executor_data["attributes"]["volume_id"],
                validate_environment=False,
            )
            self._executor_map[electron_name] = executor

        for service_name, service in script.services.items():
            service_executor = service.executor
            executor = CloudExecutor(
                num_cpus=service_executor.num_cpus,
                memory=service_executor.memory,
                num_gpus=service_executor.num_gpus,
                gpu_type=service_executor.gpu_type,
                env=service_executor.env,
                time_limit=service_executor.time_limit,
                volume_id=service_executor.volume_id,
                validate_environment=False,
            )
            self._executor_map[service_name] = executor

        self._script = script

    def __getitem__(self, key) -> CloudExecutor:
        if key not in self._executor_map:
            raise self._invalid_name_error(key)

        return ExecutorWrapper(self._executor_map[key])

    def __setitem__(self, key, value) -> None:
        if key not in self._executor_map:
            raise self._invalid_name_error(key)

        if not isinstance(value, CloudExecutor):
            raise ValueError(
                f"Invalid assignment (type {type(value).__name__}), "
                "value must be an instance of cc.CloudExecutor."
            )
        if value.env == "default":
            # Set same environment
            old_executor = self._executor_map[key]
            value.env = old_executor.env
        self._executor_map[key] = value

    def __str__(self):
        lines = []
        for target, executor in self._executor_map.items():
            _executor_dict = executor.__dict__.copy()

            # Omit some keys from the string output
            _executor_dict.pop("validate_environment")
            _executor_dict.pop("settings")
            _executor_dict.pop("volume_id")

            lines.append(f"'{target}'\n")
            lines.extend(
                ["    " + line for line in pformat(_executor_dict).splitlines()])
            lines.append("\n")

        return "\n".join(lines)

    def _invalid_name_error(self, invalid_key) -> ValueError:

        valid_keys_dict = {}
        for k in self._executor_map:
            valid_keys_dict[f"'{k}'"] = "service" if k in self._script.services else "task"

        spacer = "    "
        valid_keys = "\n".join(
            f"{spacer}{k:>20} ({v})" for k, v in valid_keys_dict.items()
        )

        return ValueError(
            f"Invalid task or service name '{invalid_key}'. "
            f"Valid names are \n\n{valid_keys}\n\n"
            "Please select a valid task or service name."
        )

    @property
    def map(self) -> Dict[str, CloudExecutor]:
        """Returns a copy of the underlying executor map"""
        return self._executor_map.copy()

    def items(self):
        """Returns the items of the underlying executor map"""
        return self._executor_map.items()


class ExecutorWrapper:
    """Wraps a CloudExecutor object to allow for validated attribute re-assignment"""

    def __init__(self, executor: CloudExecutor):
        self.__dict__["executor"] = executor

    def __setattr__(self, key, value):

        if not hasattr(self.__dict__["executor"], key):
            raise AttributeError(
                f"Attribute '{key}' is not present in CloudExecutor."
            )

        new_dict = self.__dict__["executor"].__dict__.copy()
        new_dict.update({key: value, "validate_environment": False})
        new_executor = CloudExecutor(**new_dict)

        # Update original object with validated attributes.
        self.__dict__["executor"].__dict__.update(**new_executor.__dict__)

    def __getattr__(self, item):

        if item == "__dict__":
            # Avoid recursion error.
            return self.__dict__

        if not hasattr(self.__dict__["executor"], item):
            raise AttributeError(
                f"Attribute '{item}' is not present in CloudExecutor."
            )

        return getattr(self.__dict__["executor"], item)

    def __str__(self):
        return self.__dict__["executor"].__str__().replace("CloudExecutor", "ExecutorWrapper")

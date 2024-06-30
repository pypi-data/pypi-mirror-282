import json
import toml
from pathlib import Path
from quick_api_tests.generators.http.filters import to_snake_case


def generate_project_structure(data: dict, path: Path = Path("")):
    for item, value in data.items():
        directory_path = path / item
        directory_path.mkdir(exist_ok=True)
        init_file_path = directory_path / "__init__.py"
        init_file_path.touch()

        if value:
            generate_project_structure(value, path=directory_path)


def base_project_structure(base_path):
    with open(base_path / "quick_api_tests.toml") as config_file:
        config = toml.load(config_file)

    structure = {}
    for module_type, description in config.items():
        if module_type == "http":
            for service in description:
                (
                    structure.setdefault("clients", {})
                    .setdefault("http", {})
                    .setdefault(
                        to_snake_case(service["service_name"]),
                        {
                            "apis": {},
                            "models": {}
                        },
                    )
                )
                (
                    structure.setdefault("generic", {})
                    .setdefault("helpers", {})
                    .setdefault("http", {})
                    .setdefault(to_snake_case(service["service_name"]), {})
                )
        structure['tests'] = {}
    return structure

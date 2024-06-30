from pathlib import Path
from subprocess import SubprocessError
from typing import Optional

from quick_api_tests.generators.http.parser import OpenAPISpec
from quick_api_tests.generators.http.utils import (
    create_and_write_file,
    run_command,
    is_url,
)
from quick_api_tests.generators.http.filters import (
    to_snake_case,
    to_camel_case,
)

from jinja2 import (
    Environment,
    FileSystemLoader,
)


class HTTPGenerator:
    BASE_PATH = Path.cwd() / "clients" / "http"

    def __init__(self, openapi_spec: OpenAPISpec, templates_dir: Optional[Path] = None):
        self.openapi_spec = openapi_spec
        self.templates_dir = templates_dir or str(Path(__file__).parent / "templates")
        self.env = Environment(loader=FileSystemLoader(self.templates_dir), autoescape=True)
        self.env.filters["to_snake_case"] = to_snake_case
        self.env.filters["to_camel_case"] = to_camel_case

    def generate(self) -> None:
        self._gen_clients()
        # Нет необходимости в генерации фасада для клиента, поэтому пропускаем
        # self._gen_facade()
        self._gen_init_apis()
        self._gen_models()
        run_command(f'black {self.BASE_PATH}')
        run_command(f'ruff check {self.BASE_PATH} --fix')

    def _gen_init_apis(self) -> None:
        rendered_code = self.env.get_template("__init__.jinja2").render(
            api_names=self.openapi_spec.api_tags,
            service_name=self.openapi_spec.service_name,
        )
        file_name = f"{to_snake_case(self.openapi_spec.service_name)}/__init__.py"
        file_path = self.BASE_PATH / file_name
        create_and_write_file(file_path=file_path, text=rendered_code)
        create_and_write_file(file_path=file_path.parent.parent / "__init__.py", text="# coding: utf-8")

    def _gen_facade(self) -> None:
        rendered_code = self.env.get_template("facade.jinja2").render(
            api_names=self.openapi_spec.api_tags,
            service_name=self.openapi_spec.service_name,
        )
        file_name = f"{to_snake_case(self.openapi_spec.service_name)}_client.py"
        file_path = self.BASE_PATH / file_name
        create_and_write_file(file_path=file_path, text=rendered_code)

    def _gen_clients(self) -> None:
        for tag in self.openapi_spec.api_tags:
            handlers = self.openapi_spec.handlers_by_tag(tag)
            models = self.openapi_spec.models_by_tag(tag)
            rendered_code = self.env.get_template("api_client.jinja2").render(
                models=models,
                data_list=handlers,
                api_name=tag,
                service_name=self.openapi_spec.service_name,
                version=self.openapi_spec.version,
            )
            file_name = f"{to_snake_case(tag)}_api.py"
            file_path = self.BASE_PATH / to_snake_case(self.openapi_spec.service_name) / "apis" / file_name
            create_and_write_file(file_path=file_path, text=rendered_code)
            create_and_write_file(file_path=file_path.parent / "__init__.py", text="# coding: utf-8")

    def _gen_models(self) -> None:
        file_path = self.BASE_PATH / to_snake_case(self.openapi_spec.service_name) / "models" / "api_models.py"
        spec = self.openapi_spec.cache_spec_path if is_url(self.openapi_spec.spec_path) else self.openapi_spec.spec_path
        create_and_write_file(file_path=file_path)
        create_and_write_file(file_path=file_path.parent / "__init__.py", text="# coding: utf-8")
        command = f"""datamodel-codegen \
                    --input {spec} \
                    --output {file_path} \
                    --snake-case-field \
                    --capitalise-enum-members"""
        exit_code, stderr = run_command(command)
        if exit_code != 0:
            raise SubprocessError(stderr)

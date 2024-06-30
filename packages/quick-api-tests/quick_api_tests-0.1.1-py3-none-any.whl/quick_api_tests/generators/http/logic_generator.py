from pathlib import Path
from typing import Optional
from quick_api_tests.logger.log import LOGGER
from quick_api_tests.generators.http.parser import OpenAPISpec
from quick_api_tests.generators.http.utils import (
    create_and_write_file,
)
from quick_api_tests.generators.http.filters import (
    to_snake_case,
    to_camel_case,
)

from jinja2 import (
    Environment,
    FileSystemLoader,
)


class HTTPLogicGenerator:
    BASE_PATH = Path.cwd() / "logic" / "http"

    def __init__(self, openapi_spec: OpenAPISpec, templates_dir: Optional[Path] = None):
        self.openapi_spec = openapi_spec
        self.templates_dir = templates_dir or str(Path(__file__).parent / "templates")
        self.env = Environment(loader=FileSystemLoader(self.templates_dir), autoescape=True)
        self.env.filters["to_snake_case"] = to_snake_case
        self.env.filters["to_camel_case"] = to_camel_case

    def generate(self):
        self._gen_client_wrappers()
        self._gen_facade()
        self._gen_logic_facade()

    def _gen_client_wrappers(self):
        for tag in self.openapi_spec.api_tags:
            LOGGER.info(f"Generate client logic for tag: {tag}")
            rendered_code = self.env.get_template("client_logic.jinja2").render(
                api_name=tag,
                service_name=self.openapi_spec.service_name,
            )
            file_name = f"{to_snake_case(self.openapi_spec.service_name)}/{to_snake_case(tag)}_api.py"
            file_path = self.BASE_PATH / file_name
            if file_path.exists():
                LOGGER.warning(f"File: {file_path} exists, skip generate!")
                return
            create_and_write_file(file_path=file_path, text=rendered_code)

    def _gen_facade(self):
        LOGGER.info(f"Generate wrapper facade for service: {self.openapi_spec.service_name}")
        rendered_code = self.env.get_template("wrapper_facade.jinja2").render(
            api_names=self.openapi_spec.api_tags,
            service_name=self.openapi_spec.service_name,
        )
        file_name = f"{to_snake_case(self.openapi_spec.service_name)}/__init__.py"
        file_path = self.BASE_PATH / file_name
        create_and_write_file(file_path=file_path, text=rendered_code)

    def _gen_logic_facade(self):
        LOGGER.info(f"Generate logic facade for service: {self.openapi_spec.service_name}")
        rendered_code = self.env.get_template("logic_facade.jinja2").render(
            api_names=self.openapi_spec.api_tags,
            service_name=self.openapi_spec.service_name,
        )
        file_name = f"{to_snake_case(self.openapi_spec.service_name)}_client.py"
        file_path = self.BASE_PATH / file_name
        if file_path.exists():
            LOGGER.warning(f"File: {file_path} exists, skip generate!")
            return
        create_and_write_file(file_path=file_path, text=rendered_code)

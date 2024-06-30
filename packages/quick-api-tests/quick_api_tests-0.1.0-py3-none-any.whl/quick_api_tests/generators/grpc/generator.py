from pathlib import Path
import grpc
from jinja2 import (
    Environment,
    FileSystemLoader,
)
from quick_api_tests.generators.grpc.extractor import GrpcServiceExtractor
from quick_api_tests.generators.grpc.proto_recover import ProtoRecover
from quick_api_tests.generators.http.filters import (
    to_snake_case,
    to_camel_case,
)
from quick_api_tests.generators.http.utils import (
    run_command,
    create_and_write_file,
)
from quick_api_tests.logger.log import LOGGER


class GRPCGenerator:
    BASE_PATH = Path(".") / "clients" / "grpc" / "internal"

    def __init__(self, channel: grpc.Channel, service_name: str) -> None:
        self._extractor = GrpcServiceExtractor(channel=channel)
        self._service_name = service_name
        self.templates_dir = str(Path(__file__).parent / "templates")
        self.env = Environment(
            loader=FileSystemLoader(self.templates_dir), autoescape=True
        )
        self.env.filters["to_snake_case"] = to_snake_case
        self.env.filters["to_camel_case"] = to_camel_case
        self.proto_files = []

    def generate(self):
        self._recover_protos()
        self._generate_base_stubs()
        self._gen_clients()

    def _gen_clients(self):
        for stub in self._extractor.stub_names:
            handlers = self._extractor.handlers_by_stub_name(stub)
            imports = self._get_imports_path(stub)
            rendered_code = self.env.get_template("client.jinja2").render(
                imports=imports,
                handlers=handlers,
                stub_name=stub,
            )
            file_name = f"{to_snake_case(stub)}_pb.py"
            file_path = self.BASE_PATH.parent / "stubs" / to_snake_case(self._service_name) / file_name
            create_and_write_file(file_path=file_path, text=rendered_code)
            create_and_write_file(
                file_path=file_path.parent / "__init__.py", text="# coding: utf-8"
            )
            run_command(f'black {file_path}')

    def _get_imports_path(self, stub: str) -> list[str]:
        for proto in self.proto_files:
            proto_file_search_string = "".join(proto.name.split(".")[0].split("_")).lower()
            if proto_file_search_string in stub.lower():
                proto = str(proto)
                stub_bp_grpc = proto.replace(".proto", '_pb2_grpc').replace("/", ".")
                models_pb = proto.replace(".proto", '_pb2').replace("/", ".")
                stub_import = f'from {stub_bp_grpc} import {stub} as _{stub}'
                models_import = f'from {models_pb} import *'
                return [stub_import, models_import]

        return []

    def _generate_base_stubs(self):
        proto_files = self.BASE_PATH.rglob("*.proto")
        base_command = [
            "python",
            "-m",
            "grpc.tools.protoc",
            "-I .",
            "--proto_path=./clients/grpc/internal",
            "--python_out=.",
            "--grpc_python_out=.",
            "--mypy_out=.",
        ]
        for proto_file in proto_files:
            LOGGER.info(f"Processing {proto_file}")
            command = " ".join(base_command + [str(proto_file)])
            exit_code, stderr = run_command(command)
            if exit_code != 0:
                LOGGER.error(f"Error processing {proto_file}: {stderr}")
                continue

    def _recover_protos(self):
        for proto_descriptor in self._extractor.proto_file_descriptors.values():
            LOGGER.info(f"Processing recover proto: {proto_descriptor.name}")
            try:
                self.proto_files.append(ProtoRecover(proto_descriptor).get_proto(output_dir=self.BASE_PATH))
            except TypeError as e:
                LOGGER.error(f"Error processing: {proto_descriptor.name}: {e}")

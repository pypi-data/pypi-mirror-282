from typing import Optional
import grpc
import click
import toml

from quick_api_tests.generators.grpc.generator import GRPCGenerator
from quick_api_tests.generators.http.logic_generator import HTTPLogicGenerator
from quick_api_tests.generators.http.parser import OpenAPISpec
from quick_api_tests.generators.http.rest_codegen import HTTPGenerator


@click.group()
def cli() -> None:
    ...


@click.command("generate")
@click.option(
    "-t",
    "--type",
    "gentype",
    required=False,
    type=str,
    default=None,
    help="Concrete type of generation: grpc, http, etc.",
)
def generate_command(gentype: Optional[str] = None) -> None:
    with open('quick.toml') as config_file:
        config = toml.load(config_file)

        if gentype == 'grpc':
            for grpc_service in config['grpc']:
                channel = grpc.insecure_channel(grpc_service['channel'])
                codegen = GRPCGenerator(
                    channel=channel,
                    service_name=grpc_service['service_name'],
                )
                codegen.generate()
        elif gentype == 'http':
            for http_service in config['http']:
                openapi_spec = OpenAPISpec(openapi_spec=http_service['swagger'], service_name=http_service['service_name'])
                codegen = HTTPGenerator(
                    openapi_spec=openapi_spec
                )
                codegen.generate()
                logic = HTTPLogicGenerator(openapi_spec=openapi_spec)
                logic.generate()


cli.add_command(generate_command)

if __name__ == "__main__":
    cli()

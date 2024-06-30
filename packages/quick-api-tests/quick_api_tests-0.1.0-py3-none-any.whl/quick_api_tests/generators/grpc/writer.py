from pathlib import Path


class FileWriter:
    BASE_PATH = Path(".") / "clients" / "grpc" / "internal"

    def __init__(self, proto_name: str, proto_content: str = None):
        parts = proto_name.rsplit(".", 1)
        directory = parts[0].replace(".", "/")
        new_path = directory if len(parts) == 1 else f"{directory}.{parts[1]}"
        proto_name = self.BASE_PATH / new_path
        proto_name.parent.mkdir(parents=True, exist_ok=True)
        with open(proto_name, "w") as f:
            f.write(proto_content)

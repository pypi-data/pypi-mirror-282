from ..utils import get_key_multiline_values, jump_to_nonempty
from . import (
    DatasetCalculatedParameters,
    DatasetInputParameters,
    Process,
    Products,
    TechnosphereEdges,
)


def dummy(*arg, **kwargs):
    pass


BLOCK_MAPPING = {
    "Products": Products,
    "Reference assembly": TechnosphereEdges,
    "Disposal scenarios": dummy,
    "Waste scenarios": dummy,
    "Input parameters": DatasetInputParameters,
    "Calculated parameters": DatasetCalculatedParameters,
    "Materials/assemblies": TechnosphereEdges,
    "Waste or disposal scenario": dummy,
    "Processes": TechnosphereEdges,
    "Dissassemblies": dummy,
    "Reuses": dummy,
    "Additional life cycles": TechnosphereEdges,
}


class ProductStage(Process):
    def __init__(self, block: list[list], header: dict):
        self.parsed = {"metadata": {}}
        self.blocks = {}
        self.header = header

        block = jump_to_nonempty(block)

        # Start with metadata. This is stored as:
        # Key
        # Value
        # On separate lines (value can span more than one line).
        # Also, sometimes the value is missing (blank line), so we can't use
        # `get_key_multiline_value`.
        self.index = 0
        while block[self.index][1][0] not in BLOCK_MAPPING:
            k, v = self.pull_metadata_pair(block, header)
            if v:
                self.parsed["metadata"][k] = v

        for block_type, block_data in get_key_multiline_values(
            block[self.index :], stop_terms=BLOCK_MAPPING
        ):
            kwargs = {
                "header": header,
                "block": block_data,
                "category": block_type,
            }
            if not block_data:
                continue
            self.blocks[block_type] = BLOCK_MAPPING[block_type](**kwargs)

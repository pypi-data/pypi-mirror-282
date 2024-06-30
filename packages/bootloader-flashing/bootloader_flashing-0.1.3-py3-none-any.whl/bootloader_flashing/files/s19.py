import binascii
import re
from functools import cached_property
from pathlib import Path


class S19:
    class Record:
        def __init__(self, raw: str) -> None:
            self.raw = raw.strip()

        @cached_property
        def type(self) -> str:
            return self.raw[slice(0, 2)]

        @cached_property
        def length(self) -> str:
            return self.raw[slice(2, 4)]

        @cached_property
        def address(self) -> str:
            match self.type:
                case "S0":  # should be 0x0000
                    return self.raw[slice(4, 8)]
                case "S1":
                    return self.raw[slice(4, 8)]
                case "S2":
                    return self.raw[slice(4, 10)]
                case "S3":
                    return self.raw[slice(4, 12)]
                case "S5":  # not sure
                    return self.raw[slice(4, 8)]
                case "S7":
                    return self.raw[slice(4, 12)]
                case "S8":
                    return self.raw[slice(4, 10)]
                case "S9":
                    return self.raw[slice(4, 8)]
                case _:
                    raise NotImplementedError()

        @cached_property
        def data(self) -> str:
            match self.type:
                case "S0":
                    return self.raw[slice(8, -2)]
                case "S1":
                    return self.raw[slice(8, -2)]
                case "S2":
                    return self.raw[slice(10, -2)]
                case "S3":
                    return self.raw[slice(12, -2)]
                case "S5":
                    return self.raw[slice(8, -2)]
                case "S7":
                    return self.raw[slice(12, -2)]
                case "S8":
                    return self.raw[slice(10, -2)]
                case "S9":
                    return self.raw[slice(8, -2)]
                case _:
                    raise NotImplementedError()

        @cached_property
        def checksum(self) -> int:
            return (sum(int(i, 16) for i in re.findall(r"\w{2}", self.length + self.address + self.data)) & 0xFF) ^ 0xFF

        @cached_property
        def actual_checksum(self) -> str:
            return self.raw[-2:]

        @cached_property
        def valid(self) -> bool:
            return self.checksum == int(self.actual_checksum, 16)

        @cached_property
        def mname(self) -> str:
            # TODO:
            raise NotImplementedError

        @cached_property
        def ver(self) -> str:
            # TODO:
            raise NotImplementedError

        @cached_property
        def rev(self) -> str:
            # TODO:
            raise NotImplementedError

        @cached_property
        def comment(self) -> str:
            # TODO:
            raise NotImplementedError

    def __init__(self, file: str | Path):
        self.file = Path(file)

    @cached_property
    def name(self) -> str:
        return self.file.name

    @cached_property
    def records(self) -> list[Record]:
        return [self.Record(line) for line in self.file.read_text().splitlines()]

    @cached_property
    def address(self) -> int:
        for r in self.records:
            if r.type != "S0":
                return int(r.address, 16)

    @cached_property
    def data(self) -> str:
        return "".join(r.data for r in self.records if r.type != "S0")  # S0的数据段放的是标题

    @cached_property
    def length(self) -> int:
        return len(bytes.fromhex(self.data))

    @cached_property
    def checksum(self) -> bytes:
        return (binascii.crc32(bytes.fromhex(self.data)) & 0xFFFFFFFF).to_bytes(length=4)

    def __str__(self):
        return (
            f"<{self.__class__.__name__} name={self.name}, "
            f"checksum=0x{int(self.checksum.hex(), 16):08X}, "
            f"address=0x{self.address:08X}, "
            f"length=0x{self.length:08X}>"
        )

    __repr__ = __str__

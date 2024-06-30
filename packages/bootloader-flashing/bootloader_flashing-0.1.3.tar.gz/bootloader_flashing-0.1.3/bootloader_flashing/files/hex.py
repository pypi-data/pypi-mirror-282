import binascii
import enum
import re
from functools import cached_property
from pathlib import Path


class Hex:
    class Record:
        class TypeEnum(enum.Enum):
            DATA = "00"  # 数据记录
            EOF = "01"  # 文件结束记录
            EXT_SEGMENT_ADDR = "02"  # 扩展段地址记录
            EXT_LIN_ADDR = "04"  # 扩展线性地址记录

        def __init__(self, raw: str) -> None:
            self.raw = raw.strip()

        @cached_property
        def type(self) -> str:
            return self.raw[slice(7, 9)]

        @cached_property
        def length(self) -> str:
            return self.raw[slice(1, 3)]

        @cached_property
        def address(self) -> str:
            return self.raw[slice(3, 7)]

        @cached_property
        def data(self) -> str:
            return self.raw[slice(9, -2)]

        @cached_property
        def checksum(self) -> int:
            return (sum(int(i, 16) for i in re.findall(r"\w{2}", self.length + self.address + self.data)) & 0xFF) ^ 0xFF

        @cached_property
        def actual_checksum(self) -> str:
            return self.raw[-2:]

        @cached_property
        def valid(self) -> bool:
            return self.checksum == int(self.actual_checksum, 16)

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
        s: str = ""
        for r in self.records:
            if r.type == self.Record.TypeEnum.EXT_LIN_ADDR.value:
                s += r.data
            elif r.type == self.Record.TypeEnum.DATA.value:
                s += r.address
                return int(s, 16)

    @cached_property
    def data(self) -> str:
        return "".join(r.data for r in self.records if r.type == self.Record.TypeEnum.DATA.value)

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

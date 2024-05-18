from .HexidecimalToDecimal import HexadecimalToDecimal

# range format: '000000-FFFFFF'
def AddressIsInRange(address: str, range: str):
    print(f"Checking if {address} is in range {range}")
    if address is None or range is None:
        return False
    address = HexadecimalToDecimal(address)
    start, end = range.split('-')
    start = HexadecimalToDecimal(start)
    end = HexadecimalToDecimal(end)
    return start <= address <= end

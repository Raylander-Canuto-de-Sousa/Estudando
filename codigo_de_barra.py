from barcode import EAN13
from barcode.writer import ImageWriter


codigo_barra= EAN13("123456789102",writer = ImageWriter())

codigo_barra.save("Inutilismo")
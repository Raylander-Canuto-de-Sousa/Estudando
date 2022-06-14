from barcode import EAN13
from barcode.writer import ImageWriter


codigos_produtos = {
        "Feijao":"987432106123",
        "Arroz":"665738901111",
        "Macarrao":"665887111111",
        "Azeite":"998562111116"}

for produto in codigos_produtos:
    #print(produtos)
    #print(codigos_produtos[produto])
    codigo = (codigos_produtos[produto])
    codigo_barra = EAN13(codigo,writer = ImageWriter())
    codigo_barra.save(f"codigo_barra_{produto}")
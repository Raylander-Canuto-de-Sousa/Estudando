import qrcode

links_produtos = {
        "produtos1":"123456",
        "produtos2":"123457",
        "produtos3":"123548",
        "produtos4":"123459",
        }
for produto in links_produtos:
    #print(produto)
    #print(links_produtos[produto])
    link = links_produtos[produto]
    image_qrcode = qrcode.make(link)
    image_qrcode.save(f"qrcode_{produto}.jpg")
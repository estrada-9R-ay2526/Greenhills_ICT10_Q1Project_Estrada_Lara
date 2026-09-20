from pyscript import document


def generate_sku(e):

    category = document.getElementById("category")
    product = document.getElementById("product")
    quantity = document.getElementById("quantity")

    category_code = category.value

    product_code = product.value.replace(" ", "").upper()[:3]

    stock_code = quantity.value.zfill(3)

    sku = category_code + "-" + product_code + "-" + stock_code

    document.getElementById("result").innerText = "Generated SKU: " + sku
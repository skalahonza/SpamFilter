from filter import MyFilter

test = MyFilter()
test.train('data\\1')  # Tento adresář bude obsahovat soubor !truth.txt
test.test('data\\2')  # V tomto adresáři metoda vytvoří soubor !prediction.txt
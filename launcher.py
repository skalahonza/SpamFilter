from filter import MyFilter
import datetime

test = MyFilter()
print("training")
test.train('data\\1')  # Tento adresář bude obsahovat soubor !truth.txt
print("testing")
start = datetime.datetime.now()
test.test('data\\2')  # V tomto adresáři metoda vytvoří soubor !prediction.txt
print("Time spend: ", datetime.datetime.now() - start)
print("done")
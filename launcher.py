from filter import MyFilter
from quality import compute_quality_for_corpus
import datetime

INPUT = 'data\\1'
OUTPUT = 'data\\2'
start = datetime.datetime.now()
test = MyFilter()
print("training")
test.train(INPUT)  # Tento adresář bude obsahovat soubor !truth.txt
print("Done! Time spend training: ", datetime.datetime.now() - start)
print("testing")
start = datetime.datetime.now()
test.test(OUTPUT)  # V tomto adresáři metoda vytvoří soubor !prediction.txt
print("Done! Time spend testing: ", datetime.datetime.now() - start)
print("Filtr quality:")
print(compute_quality_for_corpus(OUTPUT))
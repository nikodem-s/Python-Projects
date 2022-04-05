import pprint

from Company import Company

Company = Company()

Company.read_database()
pprint.pprint(Company.lista)
Company.fire_workers()
pprint.pprint(Company.lista)

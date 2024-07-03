import backup
from kardfm import kardfm

dfm = kardfm("test")

dfm.createdoc("data",doctype="txt")
dfm.data = "Hello world!"
dfm.savedoc()

dfm.createbackup("data","full","F:\\")
dfm.deletedoc("data")

dfm.loadbackup("F:\\", "data",1)
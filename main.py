import Bytebin


bb = Bytebin.Bytebin()

paste = bb.create("Hello World!")

print(paste.url)
print(paste.key)

lookup = bb.lookup(paste.key)

print(lookup.url)
print(lookup.key)
print(lookup.content)

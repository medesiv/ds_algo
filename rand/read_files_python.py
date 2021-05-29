#To write a lazy function, just use yield:

def read_in_chunks(file_object, chunk_size=1024):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

def process_data(peice):
    print(peice)


with open('really_big_file.dat') as f:
    for piece in read_in_chunks(f):
        process_data(piece)
#Another option would be to use iter and a helper function:

f = open('really_big_file.dat')
def read1k():
    return f.read(1024)

for piece in iter(read1k, ''):
    process_data(piece)
#If the file is line-based, the file object is already a lazy generator of lines:

for line in open('really_big_file.dat'):
    process_data(line)


with open('foo') as f:
    while True:
        lines = f.readlines(8192)
        if not lines:
            break
        for line in lines:
            pass


with open('foo') as f:
    while True:
        line = f.readline()
        if not line:
            break
        pass

filepath = 'Iliad.txt'
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       print("Line {}: {}".format(cnt, line.strip()))
       line = fp.readline()
       cnt += 1

"""
for filename in os.listdir(input_dir):
    with open(filename, 'rb') as f:
        if filename.endswith(".gz"):
            f = gzip.open(fileobj=f)
        words = (line.split(delimiter) for line in f)
        ... my logic ...  

"""


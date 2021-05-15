

def get_data(files):
    files = open(files)
    lines = files.readlines()
    files.close()
    return [line.strip() for line in lines]


def write_data(file_name, score):
    f = open(file_name, "w")
    f.write(score)
    f.close()
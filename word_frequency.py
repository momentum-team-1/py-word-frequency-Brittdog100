STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    lines = []
    with open(file) as f:
        for line in f:
            lines.append(line)
    freq = {}
    for line in lines:
        ftd = line.replace('.', '').replace(',', '').replace('!', '').replace('?', '').lower()
        for w in ftd.split():
            word = w.strip()
            if word in STOP_WORDS or word == '':
                continue
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1
    for word in sorted(freq, key=freq.get, reverse=True):
        print(word,'|',"*" * freq[word])
    pass


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)

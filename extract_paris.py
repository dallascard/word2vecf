import codecs
from optparse import OptionParser


"""
Read in text and convert it to word-context pairs
"""

def main():
    usage = "%prog input.txt output.txt"
    parser = OptionParser(usage=usage)
    #parser.add_option('--keyword', dest='key', default=None,
    #                  help='Keyword argument: default=%default')
    #parser.add_option('--boolarg', action="store_true", dest="boolarg", default=False,
    #                  help='Keyword argument: default=%default')

    (options, args) = parser.parse_args()
    infile = args[0]
    outfile = args[1]

    with codecs.open(infile, 'r', encoding='utf-8') as f:
        text = f.read()

    text = text.lower()

    lines = []
    one_side_window_size = 2
    words = text.split()
    for i, word in enumerate(words):
        context_start = max(0, i - one_side_window_size)
        context_end = min(len(words)-1, i + one_side_window_size)
        for j in range(context_start, context_end+1):
            if j != i:
                lines.append(word + ' ' + words[j])

    with codecs.open(outfile, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line + '\n')


if __name__ == '__main__':
    main()

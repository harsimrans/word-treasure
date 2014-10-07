import sys
sys.path.append("./wordnik/")

from wordnik import *

apiURL = 'http://api.wordnik.com/v4'
apiKey = '06433ce87b8d5300a221707756305436a90698af8fb780485' # my own key, get yours
client = swagger.ApiClient(apiKey, apiURL)

wordApi = WordApi.WordApi(client)
wordsApi = WordsApi.WordsApi(client)

def display_random_words(limit=5):
    randoms = wordsApi.getRandomWords();
    for i in range(min(len(randoms), limit)):
        print "* " + randoms[i].word;

def display_definitions(word, length=5):
    definitions = wordApi.getDefinitions(word)
    for i in range(min(length, len(definitions))):
        print '* ' + definitions[i].text + '\n'

def display_examples(word):
    examples = wordApi.getExamples(word)
    if not examples:
        print "examples not found"
        return
    for example in examples.examples:
        print "* " + example.text + '\n'

def display_top_examples(word):
    example = wordApi.getTopExample(word)
    if not example:
        print "No example found"
        return
    print "\nExample: "
    print  example.text + '\n'

def display_related_words(word):
    related = wordApi.getRelatedWords(word)
    for wds in related:
        #print wds.words
        for wd in wds.words:
            print "* " + wd

def display_defitions_of_file_words(path):
    f = open(path, 'r')
    words = []
    for line in f:
        words.append(line)
    for word in words:
        word = word.strip('\n')
        print "\n----------------------------------------"
        print "word: ", word
        print "----------------------------------------"
        display_definitions(word, 2)



def display_help():
    '''help: definitions, random words, related words '''
    print "--------------------------------------------------------------------"
    print "Usage: python word_treasure.py [--options] args "
    print " options:                                       "
    print "  [-r or --random] count: display the random words    "
    print "  [-d or --defi] word : displays the definition of words"
    print "  [-e or --exp] word : displays the examples of word"
    print "  [-t or --tope] word : displays the top example of word"
    print "  [-s or --relate] word : displays the related words"
    print "  [-f or --file] file : displays the definitions of word from file"
    print "  [-h or --help] displays the guide"
    print "--------------------------------------------------------------------"

def main(argv):
    length = len(argv)
    if length != 3:
        display_help()
        exit(10)
    if argv[1] == '-r' or argv[1] == '--random':
        display_random_words(int(argv[2]))
    elif argv[1] == '-d' or argv[1] == '--defi':
        display_definitions(argv[2])
    elif argv[1] == '-e' or argv[1] == '--exp':
        display_examples(argv[2])
    elif argv[1] == '-t' or argv[1] == '--tope':
        display_top_examples(argv[2])
    elif argv[1] == '-s' or argv[1] == '--relate':
        display_related_words(argv[2])
    elif argv[1] == '-h' or argv[1] == '--help':
        display_help()
    elif argv[1] == '-f' or argv[1] == '--file':
        display_defitions_of_file_words(argv[2])
    else:
        display_help()


if __name__ == '__main__':
    main(sys.argv)

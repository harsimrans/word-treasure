#!/usr/bin/env python2
#
# word_treasure.py - find meaning and example uses online.
#
# Copyright (c) 2015 Harsimran Singh <me@harsimransingh.in>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

import sys
from argparse import ArgumentParser

#sys.path.append("./wordnik/")

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
    return True

def display_definitions(word, length=5):
    definitions = wordApi.getDefinitions(word)
    if not definitions:
        print "Probably not a valid word"
        return None
    print "Definitions: \n"
    for i in range(min(length, len(definitions))):
        print '* ' + definitions[i].text + '\n'
    return True

def display_examples(word, limit=5):
    examples = wordApi.getExamples(word)
    if not examples:
        print "examples not found"
        return None
    print "Examples: \n"
    for i in range(min(len(examples.examples), limit)):
        print "* " + examples.examples[i].text + '\n'
    return True

def display_top_examples(word):
    definition = wordApi.getDefinitions(word)
    if definition == None: # probably a non-existant word
        return None
    example = wordApi.getTopExample(word)
    if not example:
        print "No example found"
        return None
    print "\nExample: "
    print  example.text + '\n'
    return True

def display_related_words(word):
    related = wordApi.getRelatedWords(word)
    if related == None:
        print "No related words found"
        return None
    print "Related Words: \n"
    for wds in related:
        #print wds.words
        for wd in wds.words:
            print "* " + wd
        print ""
    return True

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
    return True

def display_compact(word):

    # print top two definitions
    if display_definitions(word, 2) == None:
        return  None # wasn't a valid word

    # then display top 3 examples to explain
    display_examples(word, 3)
    return True

def read_from_file(filename):
    f = open(filename, 'r')
    for word in f:
        print "*****************************"
        print "Word: " + str(word),
        print "*****************************"
        word = word.strip("\n")
        display_compact(word)
        raw_input("Press enter to continue ...")
        print "\033[2A"
    return True

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
    print "  [-c or --compact] count: display the word's definition and example"
    print "  [-h or --help] displays the guide"
    print "--------------------------------------------------------------------"
    return True

def main():
    parser = ArgumentParser()

    #adding options to parser
    group = parser.add_mutually_exclusive_group()

    group.add_argument("-r", "--random", action="store_true", dest="random", help="displays random words")
    group.add_argument("-d", "--defi", action="store_true", dest="definition", help="displays definition of the word", default="True")
    group.add_argument("-e", "--examples", action="store_true", dest="examples", help="displays examples")
    group.add_argument("-t", "--topexample", action="store_true", dest="topexample", help="displays top examples")
    group.add_argument("-s", "--similarwords", action="store_true", dest="similarwords", help="displays similar words")
    group.add_argument("-c", "--compact", action="store_true", dest="compact", help="displays all things about word in compact form")
    group.add_argument("-f", "--file", action="store_true", dest="file", help="displays words in compact form from file")

    parser.add_argument("word",  help="Word / count which ever is applicable")

    args, other_args = parser.parse_known_args()
    # print args, args.word
    word = args.word
    if word == '':
        parser.print_usage()
        exit(1)
    if args.random:
        display_random_words(word)
    elif args.examples:
        display_examples(word)
    elif args.topexample:
        display_top_examples(word)
    elif args.similarwords:
        display_related_words(word)
    elif args.compact:
        display_compact(word)
    elif args.file:
        read_from_file(word)
    # should be last, value true by default
    elif args.definition:
        display_definitions(word)
    else:
        display_help()

if __name__ == '__main__':
    main()

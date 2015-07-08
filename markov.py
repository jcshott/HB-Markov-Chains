import sys 
import random


def make_chains(corpus, n):
    """Takes input text as string; returns dictionary of markov chains."""
    # print corpus
    ngram_dict = {}
    # Create a list of words in order by splitting on spaces
    input_words = corpus.split()

    # Iterate over word list and create tuple keys for dictionary
    for index in xrange(len(input_words) - n):
        ngram = ()
        for index_n in xrange(n):
            ngram = ngram + (input_words[index + index_n],)
        # print ngram
        # For each tuple, check if the tuple is already a key in the dict
        # If it is a key, add to its value. If it is not a key, make it key, with new list
        if ngram in ngram_dict:
            ngram_dict[ngram].append(input_words[index + n]) 
        else:
            ngram_dict[ngram] = []
            ngram_dict[ngram].append(input_words[index + n])
    # print ngram_dict
    return ngram_dict


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""
    # Grab random key from markov chain dict to start off the generated text
    key_list = chains.keys()
  #  start_index = random.randint(0, (len(key_list) - 1))
    start_key = random.choice(key_list)
    
    # print "start_key:", start_key
    while not start_key[0][0].isupper(): 
        start_key = random.choice(key_list)
    key = start_key
    random_list_for_string = []

    char_count = 0
    for n in range(len(key)):
        random_list_for_string.append(key[n])
        char_count += len(key[n]) + 1
    # Until a ngram is not present in the dict, generate random next word from the values associated
    # with that ngram
    next_word = " "
    # print "next word", next_word
    while key in chains and char_count <= 140:
        value_list = chains[key]
       # random_index = random.randint(0, (len(value_list) - 1))
        next_word = random.choice(value_list)

        random_list_for_string.append(next_word)
        char_count += len(next_word) + 1
        temp_key = ()
        for n in range(1, len(key)):
            temp_key += (key[n],)
        # print "next word", next_word
        key = temp_key + (next_word,)
        #do something
    # print random_list_for_string
    final_list_for_string = []
    for search_i in xrange(len(random_list_for_string) - 1, 0, -1):
        if random_list_for_string[search_i][-1] == "." or random_list_for_string[search_i][-1] == "!" or random_list_for_string[search_i][-1] == "?":
            final_list_for_string = random_list_for_string[:search_i + 1]
    return " ".join(final_list_for_string)


# Change this to read input_text from a file, deciding which file should
# be used by examining the `sys.argv` arguments (if neccessary, see the
# Python docs for sys.argv)

text_of_all_files = ""
for i in range(1, len(sys.argv)):
    input_text = sys.argv[i]
    print input_text
    file_handle = open(input_text)
    text_of_all_files = text_of_all_files + " " + file_handle.read()


# input_text_1 = sys.argv[1]
# input_text_2 = sys.argv[2]

# file_handle_1 = open(input_text_1)
# file_handle_2 = open(input_text_2)

# Get a Markov chain
chain_dict = make_chains(text_of_all_files, 2)

# Produce random text
random_text = make_text(chain_dict)

print random_text

import sys 
import random


def make_chains(corpus):
    """Takes input text as string; returns dictionary of markov chains."""
    # print corpus
    bigram_dict = {}
    # Create a list of words in order by splitting on spaces
    input_words = corpus.split()

    # Iterate over word list and create tuple keys for dictionary
    for index in xrange(len(input_words) - 2):
        bigram = (input_words[index], input_words[index + 1])

        # For each tuple, check if the tuple is already a key in the dict
        # If it is a key, add to its value. If it is not a key, make it key, with new list
        if bigram in bigram_dict:
            bigram_dict[bigram].append(input_words[index+2]) 
        else:
            bigram_dict[bigram] = []
            bigram_dict[bigram].append(input_words[index+2])
   # print bigram_dict
    return bigram_dict


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
    random_list_for_string = [key[0], key[1]]
    # Until a bigram is not present in the dict, generate random next word from the values associated
    # with that bigram
    next_word = " "
    # print "next word", next_word
    while key in chains:
        value_list = chains[key]
       # random_index = random.randint(0, (len(value_list) - 1))
        next_word = random.choice(value_list)

        random_list_for_string.append(next_word)
        key = (key[1], next_word)
        # print "next word", next_word

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
chain_dict = make_chains(text_of_all_files)

# Produce random text
random_text = make_text(chain_dict)

print random_text

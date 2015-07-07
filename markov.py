import sys 
import random


def make_chains(corpus):
    """Takes input text as string; returns dictionary of markov chains."""

    bigram_dict = {}
    # Create a list of words in order by splitting on spaces
    input_words = corpus.replace("\n", " ").split(" ")

    # Iterate over word list and create tuple keys for dictionary
    for index in range(len(input_words) - 3):
        bigram = (input_words[index], input_words[index + 1])

        #bigram_dict.get(bigram, []).append(input_words[index+2].rstrip())

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
    start_index = random.randint(0, (len(key_list) - 1))
    start_key = key_list[start_index]
    key = start_key
    random_list_for_string = [key[0], key[1]]
    # Until a bigram is not present in the dict, generate random next word from the values associated
    # with that bigram
    while key in chains:
        value_list = chains[key]
        random_index = random.randint(0, (len(value_list) - 1))
        next_word = value_list[random_index]

        random_list_for_string.append(next_word)
        key = (key[1], next_word)

        #do something

    return " ".join(random_list_for_string)


# Change this to read input_text from a file, deciding which file should
# be used by examining the `sys.argv` arguments (if neccessary, see the
# Python docs for sys.argv)

input_text = sys.argv[1]

file_handle = open(input_text)

# Get a Markov chain
chain_dict = make_chains(file_handle.read())

# Produce random text
random_text = make_text(chain_dict)

print random_text

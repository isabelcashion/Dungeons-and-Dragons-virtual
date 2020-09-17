def words_with_length(greater_than, less_than, count_repeated_letters=True,
                      wordlist='./words.txt'):
    """
    Returns a list of common english words of a certain length

    Input:
        greater_than           -- has more letters than this number
        less_than              -- has less letters than this number
        count_repeated_letters -- if True, then repeated letters are 
                                  included in the length (ie the true
                                  length of the word is returned)
                                  if False, the length is just the 
                                  total number of different letters in 
                                  the word
        wordlist               -- The text file where all the words are
    Output:
        word_list    -- a list of words than meet the specification
                        all words are returned in upper case
    """
    # read all the words in first
    with open(wordlist) as wl:
        all_words=wl.readlines()
    
    # Filter out words with the right length
    all_words = [w[:-1].upper() for w in all_words\
                     if length_is_between(w[:-1], greater_than, less_than, 
                                          count_repeated_letters)]
    return all_words

def length_is_between(word, greater_than, less_than, count_repeated_letters):
    if count_repeated_letters:
        length = len(word)
    else:
        length = len(set(word))
    
    return (greater_than < length < less_than)
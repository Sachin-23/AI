import nltk
import sys
import os
import string
import math

FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    file_contents = dict() 
    for path, dirs, files in os.walk(directory):
        for file in files:
            fd = open(os.path.join(path, file), "r")
            file_contents[file] = fd.read()
            fd.close()
    return file_contents


def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    strings = []
    stopwords = nltk.corpus.stopwords.words("english")
    for token in nltk.word_tokenize(document):
        if not (token in string.punctuation or token in stopwords):
            strings.append(token.lower())
    return strings


def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    idfs = dict()
    for doc in documents:
        for word in documents[doc]:
            doc_con = 0
            for document in documents:
                if word in documents[document]:
                    doc_con += 1
            idfs[word] = math.log(len(documents) / doc_con)
    return idfs


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    tf_idfs = {file:0 for file in files}
    for word in query:
        for file in files:
            tf = files[file].count(word)
            tf_idfs[file] += tf * idfs[word] 
    tf_idfs = sorted(tf_idfs, key=lambda x: tf_idfs[x], reverse=True)
    return tf_idfs[0:n]


def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    sen_idfs = dict()
    for word in query:
        for sentence in sentences:
            if word in sentences[sentence]:
                if sentence in sen_idfs:
                    sen_idfs[sentence] += idfs[word]
                else:
                    sen_idfs[sentence] = idfs[word]

    answers = sorted(sen_idfs, key=lambda x: sen_idfs[x], reverse=True)

    for answer in answers[0:n+2]:
        print(answer, sen_idfs[answer])

    if sen_idfs[answers[0]] == sen_idfs[answers[1]]:
        # If two sentences have same idfs.
        query_density = dict()
        # Find higher "query term density" for n + 1 sentences.
        for sentence in answers[0:n+1]:
            count = 0
            for word in query:
                if word in sentences[sentence]:
                    count += 1
            query_density[sentence] = count / len(sentences[sentence])

        answers = sorted(query_density, key=lambda x: query_density[x], reverse=True)

    return answers[0:n]

if __name__ == "__main__":
    main()

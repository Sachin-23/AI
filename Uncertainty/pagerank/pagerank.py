import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    # All links found in that page.
    links = corpus[page]

    # All the page in corpus.
    all_pages = set(list(corpus.keys()) + [i for j in corpus for i in corpus[j]])

    probability_distribution = {}

    # If the page contains any link.
    if links:
        links_probability = damping_factor / len(links)
        additional_probability = (1 - damping_factor) / len(all_pages)
        for each_page in all_pages:
            if each_page in links:
                probability_distribution[each_page] = links_probability + additional_probability
            else:
                probability_distribution[each_page] = additional_probability
    else:
        probability = 1 / len(all_pages)
        for each_page in all_pages:
            probability_distribution[each_page] = probability

    return probability_distribution


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    all_pages = set(list(corpus.keys()) + [i for j in corpus for i in corpus[j]])

    PageRank = {page: 0 for page in all_pages}

    random_page = random.choice(list(all_pages))

    pd = transition_model(corpus, random_page, damping_factor)  
   
    for i in range(n - 1):
        weights = [pd[link] for link in pd]
        pages = list(pd.keys())
        random_page = random.choices(pages, weights, k=1)[0]
        PageRank[random_page] += 1
        pd = transition_model(corpus, random_page, damping_factor)  
    
    for page in PageRank:
        PageRank[page] /= n

    return PageRank


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    all_pages = set(list(corpus.keys()) + [i for j in corpus for i in corpus[j]])

    PageRank = {page: 1/len(all_pages) for page in all_pages}

    i = True
    while i:
        i = False
        for page in all_pages:
            first_half = (1 - damping_factor) / len(all_pages)

            second_half = 0
            for pg in corpus:
                if page in corpus[pg]:
                    second_half += (PageRank[pg] / len(corpus[pg]))
                elif not corpus[pg]:
                    second_half += 1 / len(all_pages)

            full = first_half + damping_factor * second_half
            if abs(PageRank[page] - full) > 0.001:
                i = True
                PageRank[page] = full 

    return PageRank


if __name__ == "__main__":
    main()

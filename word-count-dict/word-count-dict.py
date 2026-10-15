def word_count_dict(sentences: list) -> dict:
    """
    Returns a dictionary of token counts.
    """

    freq = {}

    for i in  range(len(sentences)):
        for j in range(len(sentences[i])):
            if sentences[i][j] in freq:
                freq[sentences[i][j]] = freq[sentences[i][j]] + 1;
            else:
                freq[sentences[i][j]] = 1;

    return freq;
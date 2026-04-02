[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/cDnlIYNC)

# P1: Data Detective

## Summary

This project analyzes a text file, counts word frequencies, shows the top N words, and reports one extra insight. The program processes the text step by step, making it easy to understand and test each part of the workflow.

## Dataset

* File: `data/sample.txt` (Romeo and Juliet by William Shakespeare, Project Gutenberg #70521)
* Why I chose it: I chose *Romeo and Juliet* because it is a well-known public-domain text with rich language and varied vocabulary, which makes it ideal for analyzing word frequencies and patterns.

## How to run

```bash
pytest -q
python -m src.project
```

## Approach

* Load text from a file
* Normalize the text (lowercase, remove punctuation)
* Tokenize into words
* Count word frequencies using a dictionary
* Show the top N most frequent words
* Report one extra insight (average word length)

## Complexity

### `count_words`

* Time: O(n)
* Space: O(k)
* Why: The function loops through all words once (n words), and stores unique words (k) in a dictionary.

### `top_n_words`

* Time: O(k log k)
* Space: O(k)
* Why: The dictionary items are sorted based on frequency, which takes O(k log k), where k is the number of unique words.

## Edge-case checklist

* [x] empty file — returns empty results safely
* [x] punctuation-heavy input — punctuation is removed during normalization
* [x] repeated words — counted correctly using dictionary
* [x] uppercase/lowercase differences — normalized to lowercase
* [x] `n <= 0` — returns an empty list

## Assistance & sources

* AI used? (Y/N): Yes
* What it helped with: Structuring the project, writing functions, and generating test cases.
* Other sources: Project Gutenberg (Romeo and Juliet text)

## Design note (150–250 words)

I chose *Romeo and Juliet* by William Shakespeare as my dataset because it is a public-domain text with a wide variety of vocabulary and writing styles. This makes it suitable for analyzing word frequencies and understanding how often certain words appear in classical literature.

For the design, I focused on breaking the program into small, clear functions such as loading text, normalizing it, tokenizing, and counting words. This modular approach made it easier to test each part individually and ensured that the code is readable and maintainable. Using Python dictionaries for counting words was straightforward and efficient.

One of the easier parts was implementing the word counting logic, while handling edge cases like empty input and punctuation required more careful thought. Normalizing the text properly was important to ensure consistent results.

If I were to improve this project, I would add more advanced insights such as tracking common phrases (bigrams) or visualizing the results. This would make the tool more powerful while still building on the same core structure.

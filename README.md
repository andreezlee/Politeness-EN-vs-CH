# Politeness-EN-vs-CH
Creating classifiers to resolve misunderstandings between native English speakers (predominantly American) and Chinese ESL speakers.

## So far:

In examining features of person (1st vs 2nd vs 3rd), there are no distinctions in frequency for any labels for native speakers and ESL speakers.

In regards to passive voice, it appears native speakers are much more likely to see passive voice as polite compared to Chinese ESL speakers.

## Labeling Schema Testing

Within ```Parsing.ipynb```, there are 5 labeling schemes implemented:

- Binary scheme: just 0 or 1 depending on impolite or polite, respectively.
- Weak Neutral scheme: adding in Neutral label that applies for a wide range of values.
- Strong Neutral scheme: Neutral label applies over more narrow range of values.
- Intermediate scheme: extending labeling with Very Polite and Very Impolite.
- Partitions scheme: scheme based on relative frequency rather than exact values.

## Classifier Implementation

In accordance to features hypothesized in the PDF, we implement a series of Random Forest classifiers to measure model accuracy by ablating on these features, starting with a naive model and logically working our way through the combinations.

### TODO: Codify results for easier comparison, add more metrics like Recall/Precision/F1
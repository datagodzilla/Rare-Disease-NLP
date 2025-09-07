# Rare-Disease-NLP

This project generates a corpus of 7699 rare disease abstracts. Follow the Notebooks in the order below to see the workflow.

## Key notebooks
``gather_pubs_per_disease.ipynb``: Queries the [EBI RESTful API](https://www.ebi.ac.uk/ebisearch/documentation/rest-api) for 500 disease names and synonyms and retrieves abstracts until at least 50 abstracts returned or results exhausted and saves results in whole_abstract_set.csv. Although ~25,000 abstracts were expected, 7699 unique abstracts were returned on 488 diseases due to limited research on rare diseases.

``csv2txtfolder.ipynb``: Converts the saved abstracts into a folder of text files which comprises the corpus. The corpus has too many files to save in GitHub so rerun this notebook to generate.
Data files
GARD.csv: List of rare disease names and synonyms from the NIH Genetic and Rare Disease Information Center
whole_abstract_set.csv: Contains 7699 unique abstracts (9284 total) that were returned from the EBI API call.


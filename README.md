# olympics-in-numbers

This is data from the 2024 Paris Olympics scraped from the [official website](https://olympics.com/en/paris-2024/). The data was retrieved on August 12, 2024, one day after the closing ceremony.

The cleaned and structured data is available in the `data/` directory. The schema is pretty self explanatory, but broadly, there are four main entities: `countries`, `athletes`, `disciplines` (e.g., tennis), and `events` (e.g., women's singles). Following best practices, each entity is assigned an `id`, which is referenced throughout the dataset. You can join tables on these ids to get all relevant information. 

`utils.py` also contains some helper functions to fetch population and GDP data from Wikipedia.

I have manually tallied the data against the official website, so I'm pretty confident of the data quality. but feel free to open issues or PRs if you find an error.

I hope this dataset can encourage more fine-grained analysis and understanding, beyond the usual medal tally.

# Basic Statistics

- Countries: 206 (of which 92 won medals)
- Disciplines: 45
  - Events: 329
- Athletes: 11110
  - Largest contingents: USA (690), France (600), Australia (475)
  - Smallest contingents: Belize, Somalia, Liechtenstein, Nauru (all one)
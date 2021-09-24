# msa-2021-dsproj-mabilton

This repository contains all of the work I produced for [Phase 2 of the Microsoft Student Accelerator Data Science Programme](https://github.com/NZMSA/2021-Phase-2-Data-Science). Here's a brief overview of what's stored here:

- The `[1] Train BERT Model` folder contains the IPython notebook I used to finetune one of Hugging Face's transformer models for the purposes of the [Kaggle readability competition](https://www.kaggle.com/c/commonlitreadabilityprize), as well as the notebook I used to actually submit my Kaggle predictions.
- The `[2] Scrape Gutenberg` folder contains an IPython notebook which scrapes the entire texts of the Top 100 most popular books on the [Project Gutenberg website](https://www.gutenberg.org/). The 'readability' of each of these texts is then predicted using the transformer model which was previously trained in `[1] Train BERT Model`.
- The `[3] Deploy Model` folder contains an IPython notebook to deploy the finetuned transformer model onto Azure, as well as a Flask web app which calls the endpoint of this Azure-deployed model; instructions are provided on how to deploy this Flask web app to Heroku.
- As the name suggests, the `[4] Power BI Dashboard` folder just contains a very simple Power BI dashboard to visualise some of the data I was working with in this project.


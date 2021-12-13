# Analyze Twitter Data for Sentiment Analysis

**Flask web app for Twitter data analysis of Taco Bell food chain tweets**

<!-- ### References -->
## Code Documents

## data/

* **W2V.pkl** : The Word2Vec model, saved in full, for access in the `wordcloud` function.
* `sent_df` and `tokens` JSON files save the work done in the **preproc.ipynb** notebook, for easier access to the processed data.
* `tweets.db` : The `sqlite` database that stored the accumulating tweets run by the `getTweets.py` script.

## twitapp/

* This is the main **Flask** app directory.
* The `db.py` script defines the `SQLite` database.
* `mkclouds.py` is a script that generates the `wordcloud` images from the similar words as found by the `word2Vec` model.
* `word_vectors.kv` is the stored `KeyedVectors` from the **Word2Vec** model.
* HTML models are in the **templates** directory.

## Root level

* `Procfile` is a simple script to allow deployment to Heroku.
* `getTweets.py` is the Python script used to cull tweets via the **Twitter API v 2.x**.
* The `preproc` Jupyter notebook is a place for experimentation and general pre-processing of data with **Pandas**. The **Word2Vec** modeling and **WordCloud** functions were developed here.
* The `requirements.txt` is for deployment, and lists the installed packages in the `pip` virtual environment.
* `tweetTasks.ipynb` is the initial work on developing the `getTweets` script and other code development for processing the data.
* `twitDBTest.py` was written to test whether the ongoing crontab job was successful, and how many tweets were appended to the database.


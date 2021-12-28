# Function script to generate the WordCloud

def makeCloud(term_choice):
    from os import path
    from PIL import Image
    import numpy as np
    from matplotlib.figure import Figure
    # import matplotlib.pyplot as plt
    # import os

    from wordcloud import WordCloud, ImageColorGenerator
    from gensim.models import KeyedVectors

    # Read the whole text.
    IMG_DIR = 'twitapp/static/images/'

    # read the mask image
    taco_mask = np.array(Image.open(path.join(IMG_DIR, 'taco_bell_8.png')))

    # Load stored word2Vec vectors
    reload_word_vecs = KeyedVectors.load('word_vectors.kv')

    # Define choice set
    # choices = ['love', 'hate', 'good', 'disgusting', 'awful', 'best', 'awesome', 'dinner', 'lunch', 'late', 'really', 'gordita', 'chalupa', 'drunk', 'pizza']
    search_item = term_choice # Choice selection

    # Run the model to obtain the word vectors for similarities
    sims = [item[0] for item in reload_word_vecs.most_similar([search_item], topn=300)]

    # Draw the w WordCloud image, with the masked image
    wc = WordCloud(background_color="black", max_words=300, mask=taco_mask)
                    # contour_width=10, contour_color='grey')


    # generate word cloud
    simString = " ".join(sims)
    wc.generate(simString)

    # Useful function for deriving a greyscale image; uncomment to use, put grey_color_func in color_func parameter in imshow function.
    # def grey_color_func(word, font_size, position, orientation, random_state=None,
    #                     **kwargs):
    #     return "hsl(0, 0%%, %d%%)" % np.random.randint(90, 100)

    # Use WordCloud's built-in function to generate colormap from the mask image.
    taco_colors = ImageColorGenerator(taco_mask)

    # store to file
    # wc.to_file(path.join(IMG_DIR, "taco_hash.png"))


    # Size, style, and show
    fig = Figure(figsize=(12, 18))
    ax = fig.subplots()
    ax.imshow(wc.recolor(color_func=taco_colors), interpolation='bilinear')
    ax.axis('off')
    return fig
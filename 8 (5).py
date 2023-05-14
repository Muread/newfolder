def get_word_reviews_count(df):
    word_reviews = {}
    for row in df.dropna(subset=['review']).itertuples():
        recipe_id, review = row.recipe_id, row.review
        words = review.split(' ')
        for word in words:
            if word not in word_reviews:
                word_reviews[word] = []
            word_reviews[word].append(recipe_id)
    
    word_reviews_count = {}
    for row in df.dropna(subset=['review']).itertuples():
        review = row.review
        words = review.split(' ')
        for word in words:
            word_reviews_count[word] = len(word_reviews[word])
    
    return word_reviews_count
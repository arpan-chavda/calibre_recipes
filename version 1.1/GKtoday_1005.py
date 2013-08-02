class BasicUserRecipe1374243904(AutomaticNewsRecipe):
    title          = u'GKtoday'
    oldest_article = 7
    max_articles_per_feed = 100
    auto_cleanup = True

	description = u'GKToday.in web site ebook created using rss feeds.'

    # Author of this recipe.
    __author__ = 'arpan-chavda'

    # Specify English as the language of the RSS feeds (ISO-639 code).
    language = 'en_GB'

    # Set tags.
    tags = 'quiz, current-affairs'

    # Set publisher and publication type.
    publisher = 'GKToday.in'
    publication_type = 'blog'

    # Disable stylesheets from site.
    no_stylesheets = True

    encoding = None
    remove_empty_feeds = True
    conversion_options = { 'smarten_punctuation' : True , 'search_replace': '[["Show Answer", ""], ["Download article as PDF", ""]]'}
    feeds          = [(u'Home', u'http://feeds.feedburner.com/GeneralKnowledgeToday')]
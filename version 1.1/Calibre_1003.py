class AdvancedUserRecipe1365325396(BasicNewsRecipe):
    title          = u'Calibre'
    oldest_article = 30
    max_articles_per_feed = 3
    description = u'thecalibre.in web site ebook created using rss feeds.'

    # Author of this recipe.
    __author__ = 'arpan-chavda'

    # Specify English as the language of the RSS feeds (ISO-639 code).
    language = 'en_GB'

    # Set tags.
    tags = 'current-affairs'

    # Set publisher and publication type.
    publisher = 'theCalibre.in'
    publication_type = 'blog'

    # Disable stylesheets from site.
    no_stylesheets = True

    encoding = None
    remove_empty_feeds = True
    conversion_options = { 'smarten_punctuation' : True }

    auto_cleanup = True
    auto_cleanup_keep = '//img[@itemprop="image"]'
    feeds          = [(u'Calibre- 1', u'http://thecalibre.in/feed')]

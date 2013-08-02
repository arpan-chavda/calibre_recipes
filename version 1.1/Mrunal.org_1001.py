class AdvancedUserRecipe1365325396(BasicNewsRecipe):
    title          = u'Mrunal.org'
    oldest_article = 7
    max_articles_per_feed = 10000
    auto_cleanup = True
    description = u'Mrunal blog ebook created using rss feeds.'
    masthead_url = 'https://fbcdn-sphotos-d-a.akamaihd.net/hphotos-ak-frc1/376962_238261119628582_1219921430_n.jpg'
    # Author of this recipe.
    __author__ = 'arpan-chavda'

    # Specify English as the language of the RSS feeds (ISO-639 code).
    language = 'en_GB'

    # Set tags.
    tags = 'blog'

    # Set publisher and publication type.
    publisher = 'Mrunal Patel'
    publication_type = 'Blog'

    # Disable stylesheets from site.
    no_stylesheets = True

    encoding = None
    remove_empty_feeds = True
    conversion_options = { 'smarten_punctuation' : True }

    feeds          = [(u'Current Feeds', u'http://mrunal.org/feed')]

    def print_version(self, url):
        return url+'/print'

from IPython.display import HTML
import htmlmin

def inject(page_url: str, page_identifier: str, site_shortname: str):
    """
    Args:
        page_url (str): your page's canonical URL
        page_identifier (str): your page's unique identifier
        site_shortname (str): your site's disqus shortname

    Returns:
        None

    Example:
        >>> jupyter_disqus.inject(
                page_url= https://costahuang.me",
                page_identifier = "SC2AI/",
                site_shortname = "costahuang"
            )
    """
    disqus_code = """
    <div id="disqus_thread"></div>
    <script>

    /**
    *  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
    *  LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables*/

    var disqus_config = function () {
    this.page.url = '%s';  // Replace PAGE_URL with your page's canonical URL variable
    this.page.identifier = '%s'; // Replace PAGE_IDENTIFIER with your page's unique identifier variable
    };
    (function() { // DON'T EDIT BELOW THIS LINE
    var d = document, s = d.createElement('script');
    s.src = 'https://%s.disqus.com/embed.js';
    s.setAttribute('data-timestamp', +new Date());
    (d.head || d.body).appendChild(s);
    })();
    </script>
    <noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
        <script id="dsq-count-scr" src="//%s.disqus.com/count.js" async></script>
    </body>
    """ % (page_url, page_identifier, site_shortname, site_shortname)
    HTML(htmlmin.minify(disqus_code))
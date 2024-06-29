import mechanicalsoup
import re
import urllib.parse
import sys
def go(keyword=None):
   if len(sys.argv)>1:
      keyword=sys.argv[1]
   if keyword is not None:
    browser = mechanicalsoup.StatefulBrowser()
    url = f"https://cn.bing.com/videos/search?q={keyword}&FORM=HDRSC3"
    browser.open(url)
    page = browser.get_current_page()
    elements = page.find_all(class_='mc_vtvc_con_rc')
    results = []
    for element in elements:
        title_match = re.search(r'"vt":"([^"]+)"', str(element))
        url_match = re.search(r'"purl":"([^"]+)"', str(element))
        if title_match and url_match:
            title = title_match.group(1)
            url = url_match.group(1)
            results.append((title, url))
    return results

def image(keyword=None):
   if len(sys.argv)>1:
      keyword=sys.argv[1]
   if keyword is not None:
    browser = mechanicalsoup.StatefulBrowser()
    url = 'https://cn.bing.com/images/search?q=' + urllib.parse.quote(keyword)
    response = browser.open(url)
    page_content = browser.get_current_page()
    iusc_tags = page_content.find_all('a', class_='iusc')
    
    results = []
    for tag in iusc_tags:
        murl = re.search(r'"murl":"([^"]+)"', str(tag))
        t = re.search(r'"t":"([^"]+)"', str(tag))
        if murl and t:
            results.append({
                "title": t.group(1),
                "url": murl.group(1)
            })
    
    return results
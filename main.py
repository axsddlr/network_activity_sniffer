import json

from playwright.sync_api import sync_playwright


def test_json(response, results):
    try:
        results.append(
            {
                "url": response.url,
                "data": response.json(),
            }
        )
    except:
        pass


def run(playwright):
    results = []
    chromium = playwright.chromium
    browser = chromium.launch(headless=True)
    page = browser.new_page()
    page.on('response', lambda response: test_json(response, results))
    page.goto('https://www.nba.com/stats/players/')
    browser.close()
    return results


with sync_playwright() as playwright:
    data = run(playwright)
    with open('data.json', 'w') as f:
        f.write(json.dumps(data))

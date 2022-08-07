from test_init import Complex


def test_button():
    browser = Complex("http://www.python.org")
    button = browser.getElement("//a[@class='donate-button']")
    assert button.text == "Donate", "Donation button text is not Donate"
    button.click()
    title = browser.getElement("//h1[@class='entry-title']")
    assert title.text == "Donation for the PSF", "Donation title text is not valid"
    assert title.is_displayed(), "Donation title not visible"
    pass

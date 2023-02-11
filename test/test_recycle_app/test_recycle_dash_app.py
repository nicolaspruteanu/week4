from dash.testing.application_runners import import_app
from selenium.webdriver.common.keys import Keys


# test case id format is an abbreviation in the pattern of mmffddd where m stands for module,
# f for file, and d for three digits which convey the number of your test case.
def test_rec001_h1_text_equals(dash_duo):
    """
    GIVEN the app is running
    WHEN the home page is available
    THEN the H1 heading element should include the text 'Waste and recycling' (not case sensitive)
    """
    app = import_app(app_file="recycle_app.recycle_dash_app")
    dash_duo.start_server(app)
    dash_duo.wait_for_element("h1", timeout=4)
    h1_text = dash_duo.find_element("h1").text
    assert h1_text.casefold() == "Waste and recycling".casefold()


def test_rec002_areadropdowncontainslondon(dash_duo):
    """
    GIVEN the recycle Dash app is running
    WHEN the home page has loaded
    THEN 'London' should appear in the area dropdown
    """
    app = import_app(app_file="recycle_app.recycle_dash_app")
    dash_duo.start_server(app)
    dash_duo.wait_for_element("h1", timeout=4)
    dash_duo.driver.implicitly_wait(5)
    assert (
        "London" in dash_duo.find_element("#area-select").text
    ), "'London' should appear in the area dropdown"


def test_rec003_areadropdownchangesstats(dash_duo):
    """
    GIVEN the recycle Dash app is running
    WHEN the area dropdown is changed to Hackney
    THEN the card title for the stats panel is also changed to Hackney.

    Note: using select_dcc_dropdown(elem_or_selector, value=None, index=None) didn't implement the selected value
    """
    app = import_app(app_file="recycle_app.recycle_dash_app")
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#area-select", timeout=4)
    select_input = dash_duo.find_element("#area-select input")
    select_input.send_keys("Hackney")
    select_input.send_keys(Keys.RETURN)
    dash_duo.driver.implicitly_wait(5)
    assert (
        "HACKNEY" in dash_duo.find_element("#card-name").text
    ), "'Hackney' should appear in the card name"

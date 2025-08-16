from playwright.sync_api import Playwright


def test_get_game_of_thrones_house_name(playwright: Playwright):
    headers = {
        "Accept": "application/json"
    }
    api_request_context = playwright.request.new_context(
        base_url="https://anapioficeandfire.com", extra_http_headers=headers
    )
    response = api_request_context.get("/api/houses/362")
    assert response.ok
    json_response = response.json()
    assert json_response["name"] == "House Stark of Winterfell"

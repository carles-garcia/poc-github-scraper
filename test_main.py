import sys
from unittest.mock import patch

from main import get_pattern, main, parse, scrap


def mock_get_response_lines(*args, **kwargs):
    return [
        "asdf",
        '      <a class="v-align-middle" data-hydro-click="{&quot;event_type&quot;:&quot;search_result.click&quot;,&quot;payload&quot;:{&quot;page_number&quot;:1,&quot;per_page&quot;:10,&quot;query&quot;:&quot;openstack nova css&quot;,&quot;result_position&quot;:1,&quot;click_id&quot;:55005225,&quot;result&quot;:{&quot;id&quot;:55005225,&quot;global_relay_id&quot;:&quot;MDEwOlJlcG9zaXRvcnk1NTAwNTIyNQ==&quot;,&quot;model_name&quot;:&quot;Repository&quot;,&quot;url&quot;:&quot;https://github.com/atuldjadhav/DropBox-Cloud-Storage&quot;},&quot;originating_url&quot;:&quot;https://github.com/search?q=openstack+nova+css&amp;type=repositories&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="bd698c0c017a37879a629022488ea97db29fc55faebdfb068a2f80252c8623f1" href="/atuldjadhav/DropBox-Cloud-Storage">atuldjadhav/DropBox-Cloud-Storage</a>',
    ]


def test_scrap():
    input = {
        "keywords": ["openstack", "nova", "css"],
        "proxies": ["194.126.37.94:8080", "13.78.125.167:8080"],
        "type": "Repositories",
    }
    expected_output = [{"url": "https://github.com/atuldjadhav/DropBox-Cloud-Storage"}]

    with patch("main.get_response_lines", new=mock_get_response_lines):
        result = scrap(input)
    assert result == expected_output


def test_get_pattern():
    assert get_pattern("repositories")
    assert get_pattern("issues")
    assert get_pattern("wikis")


def test_parse():
    args = parse(["-i", "input.json"])
    assert args.input_file == "input.json"


def test_main():
    with patch("main.scrap", return_value="output") as mock_scrap:
        sys.argv = ["main", "-i", "repositories.json"]
        main()
        mock_scrap.assert_called_once()

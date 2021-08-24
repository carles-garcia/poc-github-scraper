import argparse
import json
import random
import re
import sys
from typing import Dict, List

import requests


def get_response_lines(url: str, request_proxies: Dict) -> List[str]:
    response = requests.get(url, proxies=request_proxies)
    text = response.text.split("\n")
    return text


def get_pattern(query_type: str):
    if query_type == "repositories":
        pattern = "(https?://github\.com/\w+/[\w-]+)"
    elif query_type == "issues":
        pattern = "(https?://github\.com/\w+/[\w-]+/issues/\d+)"
    else:
        pattern = "(https?://github\.com//\w+/[\w-]+/wiki/[\w-]+)"
    return pattern


def scrap(input_json: Dict) -> List[Dict]:
    query: str = "+".join(input_json["keywords"])
    query_type: str = input_json["type"].lower()
    proxies: List = input_json["proxies"]
    if proxies:
        proxy = random.choice(proxies)
        request_proxies = {"http": "http://" + proxy}
    else:
        request_proxies = {}
    url = f"http://github.com/search?q={query}&type={query_type}"

    text = get_response_lines(url, request_proxies)
    result_lines = [line for line in text if "search_result.click" in line]

    result_urls: List[Dict] = []
    pattern = get_pattern(query_type)
    for line in result_lines:
        match = re.search(pattern, line)
        if match is not None:
            url = match.group(0)
            result_urls.append({"url": url})

    return result_urls


def get_input_json(input_file):
    with open(input_file) as json_file:
        input_json = json.load(json_file)
    return input_json


def parse(args):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i", "--input-file", type=str, help="input file", required=True
    )
    return parser.parse_args(args)


def main() -> None:
    args = parse(sys.argv[1:])
    input_json = get_input_json(args.input_file)
    result_urls = scrap(input_json)
    print(json.dumps(result_urls))


if __name__ == "__main__":
    main()

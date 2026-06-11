from datetime import datetime
from pathlib import Path

import requests


def fetch_sample_post():
    """Fetch sample data from a public API using the requests package."""
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1",
        timeout=10,
    )
    response.raise_for_status()
    return response.json()


def generate_log(data):
    if not isinstance(data, list):
        raise ValueError("Log data must be provided as a list.")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")
    return filename


def build_log_entries():
    """Create log entries from API data, with a local fallback for portability."""
    try:
        post = fetch_sample_post()
        return [
            "Fetched sample post from JSONPlaceholder",
            f"Post ID: {post.get('id', 'Unknown')}",
            f"Title: {post.get('title', 'No title found')}",
        ]
    except requests.RequestException as error:
        return [
            "Sample API fetch failed",
            f"Reason: {error}",
            "Generated fallback automation log",
        ]


def main():
    filename = generate_log(build_log_entries())
    output_path = Path(filename).resolve()
    print(f"Output saved at {output_path}")


if __name__ == "__main__":
    main()

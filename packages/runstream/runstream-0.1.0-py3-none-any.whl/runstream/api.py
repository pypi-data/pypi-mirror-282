import logging
import os

import requests

from runstream.model import Run, serialize_run

RUNSTREAM_API_KEY = os.getenv("RUNSTREAM_API_KEY")
RUNSTREAM_URL = os.getenv("RUNSTREAM_URL", "https://runstream.dev")
LOGGER = logging.getLogger(__name__)


def post_run(run: Run):
    run_json = serialize_run(run)

    # todo:
    # - requests.Session()
    # - retry logic
    # - async thread pool with queuing
    response = requests.post(
        f"{RUNSTREAM_URL}/api/runs",
        headers={
            "Content-Type": "application/json",
            "X-API-KEY": RUNSTREAM_API_KEY,
        },
        json=run_json,
    )

    if response.status_code != 200:
        LOGGER.error(f"Failed to post run: {response.content}")

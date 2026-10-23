"""Checks the webhook verifier against the shared vectors: python3 tests/test_webhooks.py [vectors.json]

Also collected by pytest (``test_shared_vectors``)."""

import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))
from referalli import webhooks  # noqa: E402

DEFAULT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "vectors.json")


def failures(path):
    cases = json.load(open(path))["cases"]
    return cases, [c["name"] for c in cases if webhooks.verify(c["body"], c["headers"], c["secrets"], now=c["now"]) != c["valid"]]


def test_shared_vectors():
    _, failed = failures(DEFAULT)
    assert failed == []


if __name__ == "__main__":
    cases, failed = failures(sys.argv[1] if len(sys.argv) > 1 else DEFAULT)
    for name in failed:
        print(f"FAIL {name}")
    print(f"{len(cases) - len(failed)}/{len(cases)} passed")
    sys.exit(1 if failed else 0)

"""Unit tests for slashless Location-leak detection (Aug–Sep 2026 outage)."""

from host_all import location_leaks_from_headers


def test_relative_host_prefix_leaks():
    hdrs = "HTTP/1.1 308 Permanent Redirect\r\nLocation: /tampatileroofrepair.com/services/\r\n"
    assert location_leaks_from_headers(hdrs, "tampatileroofrepair.com") == (
        "LOC-LEAK /tampatileroofrepair.com/services/"
    )


def test_clean_relative_ok():
    hdrs = "HTTP/1.1 308 Permanent Redirect\r\nLocation: /services/\r\n"
    assert location_leaks_from_headers(hdrs, "tampatileroofrepair.com") is None


def test_absolute_host_leak():
    hdrs = (
        "HTTP/1.1 308\r\n"
        "Location: https://tampatileroofrepair.com/tampatileroofrepair.com/services/\r\n"
    )
    assert "LOC-LEAK" in location_leaks_from_headers(hdrs, "tampatileroofrepair.com")


def test_no_location_ok():
    hdrs = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n"
    assert location_leaks_from_headers(hdrs, "example.com") is None


def test_exact_host_path_leaks():
    hdrs = "HTTP/1.1 308\r\nLocation: /example.com\r\n"
    assert location_leaks_from_headers(hdrs, "example.com") == "LOC-LEAK /example.com"


if __name__ == "__main__":
    test_relative_host_prefix_leaks()
    test_clean_relative_ok()
    test_absolute_host_leak()
    test_no_location_ok()
    test_exact_host_path_leaks()
    print("all green")

from ca_slack_block_kit import Divider


def test_divider_render() -> None:
    divider = Divider()
    expected_output = {"type": "divider"}
    assert divider.render() == expected_output

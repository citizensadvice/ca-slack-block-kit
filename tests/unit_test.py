from ca_slack_block_kit import Divider, Emoji


def test_divider_render() -> None:
    divider = Divider()
    expected_output = {"type": "divider"}
    assert divider.render() == expected_output


def test_emoji_constants() -> None:
    assert Emoji.THUMBS_UP == ":thumbsup:"
    assert Emoji.THUMBS_DOWN == ":thumbsdown:"
    assert Emoji.PARTY_POPPER == ":tada:"
    assert Emoji.WARNING == ":warning:"
    assert Emoji.CHECK_MARK == ":white_check_mark:"
    assert Emoji.CROSS_MARK == ":x:"
    assert Emoji.INFO == ":information_source:"
    assert Emoji.ROCKET == ":rocket:"
    assert Emoji.EYES == ":eyes:"
    assert Emoji.FIRE == ":fire:"
    assert Emoji.STAR == ":star:"

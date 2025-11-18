from os import environ

from dotenv import load_dotenv
from slack_sdk import WebClient

from ca_slack_block_kit import (
    CodeBlock,
    Divider,
    Emoji,
    Header,
    MarkdownSection,
    MarkdownSectionFields,
    render_blocks,
)

load_dotenv()
client = WebClient(environ["SLACK_TOKEN"])
TEST_CNANNEL_ID = "C07AGEKN0CB"
TEST_MESSAGE_TITLE = "CA Stack Block Kit Integration Test"
TEST_MARKDOWN_TEXT = f"""
*This is a test markdown section*

- Bullet point 1 {Emoji.THUMBS_UP}
- Bullet point 2 {Emoji.HEART}
- Bullet point 3 {Emoji.ROCKET}

`Inline code`
""".strip()
TEST_MARKDOWN_FIELDS = [
    "*Field 1*: Value 1 " + Emoji.STAR,
    "*Field 2*: Value 2 " + Emoji.HEART,
    "*Field 3*: Value 3 " + Emoji.CLAP,
    "*Field 4*: Value 4 " + Emoji.BUG,
]
TEST_CODE_SNIPPET = """
# This is a code snippet
def hello_world():
    print("Hello, world!")
""".strip()


def test_message() -> None:
    blocks = []

    blocks.append(Header(text=TEST_MESSAGE_TITLE))
    blocks.append(Divider())
    blocks.append(MarkdownSection(text=TEST_MARKDOWN_TEXT))
    blocks.append(Divider())
    blocks.append(MarkdownSectionFields(fields=TEST_MARKDOWN_FIELDS))
    blocks.append(Divider())
    blocks.append(CodeBlock(code=TEST_CODE_SNIPPET))

    response = client.chat_postMessage(
        channel=TEST_CNANNEL_ID,
        text="Hello from integration test!",
        blocks=render_blocks(blocks),
    )

    assert response["ok"] is True

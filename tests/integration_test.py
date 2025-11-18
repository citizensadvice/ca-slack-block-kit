from slack_sdk import WebClient
from dotenv import load_dotenv
from os import environ
from ca_slack_block_kit import (
    Block,
    Divider,
    Header,
    MarkdownSection,
    render_blocks,
    MarkdownSectionFields,
    CodeBlock,
)

load_dotenv()
client = WebClient(environ["SLACK_TOKEN"])
TEST_CNANNEL_ID = "C07AGEKN0CB"
TEST_MESSAGE_TITLE = "CA Stack Block Kit Integration Test"
TEST_MARKDOWN_TEXT = """
*This is a test markdown section*

- Bullet point 1 :smile:
- Bullet point 2 :tada:
- Bullet point 3 :rocket:

`Inline code`
""".strip()
TEST_MARKDOWN_FIELDS = [
    "*Field 1*: Value 1 :star:",
    "*Field 2*: Value 2 :heart:",
    "*Field 3*: Value 3 :fire:",
    "*Field 4*: Value 4 :thumbsup:",
]
TEST_CODE_SNIPPET = """
# This is a code snippet
def hello_world():
    print("Hello, world!")
""".strip()


def test_message():
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

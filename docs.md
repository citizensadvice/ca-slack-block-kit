# Table of Contents

* [ca\_slack\_block\_kit](#ca_slack_block_kit)
  * [render\_blocks](#ca_slack_block_kit.render_blocks)
  * [Block](#ca_slack_block_kit.Block)
  * [Divider](#ca_slack_block_kit.Divider)
  * [Header](#ca_slack_block_kit.Header)
  * [MarkdownSection](#ca_slack_block_kit.MarkdownSection)
  * [MarkdownSectionFields](#ca_slack_block_kit.MarkdownSectionFields)
  * [CodeBlock](#ca_slack_block_kit.CodeBlock)

<a id="ca_slack_block_kit"></a>

# ca\_slack\_block\_kit

Slack message blocks for notifications and alerts.

This module defines various Slack message block types used to construct messages
sent to Slack channels using the Blocks format. Each block type is represented
by a class that implements the Block interface.

By constructing a list of these blocks, we can then render them into the format
required by the Slack API.

<a id="ca_slack_block_kit.render_blocks"></a>

#### render\_blocks

```python
def render_blocks(blocks: list["Block"]) -> list[dict]
```

Render a list of Block objects into a list of dictionaries compatible with the Slack SDK client chat_postMessage function.

**Arguments**:

- `blocks` _list[Block]_ - List of Block objects to render.
  

**Returns**:

- `list[dict]` - List of dictionaries representing the Slack message blocks.

<a id="ca_slack_block_kit.Block"></a>

## Block Objects

```python
class Block(ABC)
```

Base class for Slack message blocks.

All block types should inherit from this class and implement the render method.

<a id="ca_slack_block_kit.Divider"></a>

## Divider Objects

```python
class Divider(Block)
```

Divider block.

<a id="ca_slack_block_kit.Header"></a>

## Header Objects

```python
@dataclass
class Header(Block)
```

Header block. Plain text with emoji support enabled.

**Arguments**:

- `text` - The header text.

<a id="ca_slack_block_kit.MarkdownSection"></a>

## MarkdownSection Objects

```python
@dataclass
class MarkdownSection(Block)
```

Markdown section block with a single piece of text.

**Arguments**:

- `text` - The markdown formatted text for the section.

<a id="ca_slack_block_kit.MarkdownSectionFields"></a>

## MarkdownSectionFields Objects

```python
@dataclass
class MarkdownSectionFields(Block)
```

Markdown section block with multiple fields.

**Arguments**:

- `fields` - A list of markdown formatted text strings for the fields.

<a id="ca_slack_block_kit.CodeBlock"></a>

## CodeBlock Objects

```python
@dataclass
class CodeBlock(Block)
```

Code block section.

**Arguments**:

- `code` - The code string to display in the block.


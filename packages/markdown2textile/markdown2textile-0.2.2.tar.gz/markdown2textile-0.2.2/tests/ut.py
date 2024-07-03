from markdown2textile.cli import convert_markdown_to_textile, convert_textile_to_markdown


def test_convert_markdown_to_textile():
    markdown = "**bold text**"
    expected_textile = "*bold text*"
    expected_textile = expected_textile.replace("\r", "").replace("\n", "")
    tested = convert_markdown_to_textile(markdown).replace("\r", "").replace("\n", "")
    assert tested == expected_textile


def test_convert_markdown_to_textile_empty_input():
    markdown = """\
# My Text

This is a pen.
My name is Pen.

[Link to panflute](http://scorreia.com/software/panflute/index.html)

https://elixir-lang.org

## Your Text

Run the bellow code with `--option`:

```python
print("Hello, world")
```

---

> 2019/06/23

> 2019/06/23
> 2019-06-23

> 2019/06/23
>
> 2019-06-23

* **Bold** and __Bold__
- *Italic* and _Italic_
"""
    expected_textile = """\
h1(#my-text). My Text

This is a pen.
My name is Pen.

"Link to panflute":http://scorreia.com/software/panflute/index.html

https://elixir-lang.org

h2(#your-text). Your Text

Run the bellow code with @--option@:

<pre><code class="python">
print("Hello, world")
</code></pre>

---

> 2019/06/23

> 2019/06/23
> 2019&#45;06&#45;23

> 2019/06/23
>
> 2019&#45;06&#45;23

* *Bold* and *Bold*
* _Italic_ and _Italic_
"""
    expected_textile = expected_textile.replace("\r", "").replace("\n", "")
    tested = convert_markdown_to_textile(markdown).replace("\r", "").replace("\n", "")
    assert tested == expected_textile


def test_convert_textile_to_markdown():
    textile = """
<pre><code class="bash">
echo abcdefg
</code></pre>
"""
    expected_markdown = """
``` bash
echo abcdefg
```
"""
    expected_markdown = expected_markdown.replace("\r", "").replace("\n", "")
    tested = convert_textile_to_markdown(textile).replace("\r", "").replace("\n", "")
    assert tested == expected_markdown
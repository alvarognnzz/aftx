# aftx

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

alvarognnzz's formatted text. Simple and minimalist formatted text system inspired by Markdown and LaTeX.

<p align="center">
  <img src="https://github.com/alvgonzx/aftx/assets/77798268/ec0f4303-bac5-4b61-ba4e-99208489eac0https://github.com/alvgonzx/aftx/assets/77798268/ec0f4303-bac5-4b61-ba4e-99208489eac0" />
</p>

## Formatted text system

This formatted text system is used to create simple text documents with a readable and appealing format. It uses a syntax similar to Markdown that makes the creation of text documents easier.

## Syntax

The syntax aims to be very simple and similar to Markdown.

### Title

```
# This is a title
```

### Subtitle

```
## This is a subtitle
```

### List

```
- This
- Is
- A
- List
```

## Roadmap

- [ ] Make possible to create new pages
- [ ] Add support to more types of subtitles (h1-h6)
- [ ] Integrate images
- [ ] Include ordered lists
- [ ] Create a configurable font system (using google fonts)

## Installation

Before installing, make sure you install [wkhtmltopdf](https://wkhtmltopdf.org/downloads.html) and add it to your system path.

### Git clone

```
git clone https://github.com/alvgonzx/aftx.git
```

### Install dependencies

```
pip install -r requirements.txt
```

### Run the compiler
```
python compiler.py examples/lorem.aftx
```

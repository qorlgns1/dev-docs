---
title: "text-transform - Typography - Tailwind CSS"
description: "Use the uppercase utility to uppercase the text of an element:"
---

Source URL: https://tailwindcss.com/docs/text-transform

# text-transform - Typography - Tailwind CSS

| Class         | Styles                        |
| ------------- | ----------------------------- |
| `uppercase`   | `text-transform: uppercase;`  |
| `lowercase`   | `text-transform: lowercase;`  |
| `capitalize`  | `text-transform: capitalize;` |
| `normal-case` | `text-transform: none;`       |

## Examples

- Uppercasing text

Use the `uppercase` utility to uppercase the text of an element:

The quick brown fox jumps over the lazy dog.

```
    <p class="uppercase">The quick brown fox ...</p>
```

- Lowercasing text

Use the `lowercase` utility to lowercase the text of an element:

The quick brown fox jumps over the lazy dog.

```
    <p class="lowercase">The quick brown fox ...</p>
```

- Capitalizing text

Use the `capitalize` utility to capitalize text of an element:

The quick brown fox jumps over the lazy dog.

```
    <p class="capitalize">The quick brown fox ...</p>
```

- Resetting text casing

Use the `normal-case` utility to preserve the original text casing of an element—typically used to reset capitalization at different breakpoints:

The quick brown fox jumps over the lazy dog.

```
    <p class="normal-case">The quick brown fox ...</p>
```

- Responsive design

Prefix a `text-transform` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
    <p class="capitalize md:uppercase ...">  Lorem ipsum dolor sit amet...</p>
```

Learn more about using variants in the [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states).

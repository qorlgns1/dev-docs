---
title: "scroll-behavior - Interactivity - Tailwind CSS"
description: "Use the scroll-smooth utility to enable smooth scrolling within an element:"
---

Source URL: https://tailwindcss.com/docs/scroll-behavior

# scroll-behavior - Interactivity - Tailwind CSS

| Class           | Styles                     |
| --------------- | -------------------------- |
| `scroll-auto`   | `scroll-behavior: auto;`   |
| `scroll-smooth` | `scroll-behavior: smooth;` |

## Examples

- Using smooth scrolling

Use the `scroll-smooth` utility to enable smooth scrolling within an element:

```
    <html class="scroll-smooth">  <!-- ... --></html>
```

Setting the `scroll-behavior` only affects scroll events that are triggered by the browser.

- Using normal scrolling

Use the `scroll-auto` utility to revert to the default browser behavior for scrolling:

```
    <html class="scroll-smooth md:scroll-auto">  <!-- ... --></html>
```

---
title: "isolation - Layout - Tailwind CSS"
description: "Use the isolate and isolation-auto utilities to control whether an element should explicitly create a new stacking context:"
---

Source URL: https://tailwindcss.com/docs/isolation

# isolation - Layout - Tailwind CSS

| Class            | Styles                |
| ---------------- | --------------------- |
| `isolate`        | `isolation: isolate;` |
| `isolation-auto` | `isolation: auto;`    |

## Examples

- Basic example

Use the `isolate` and `isolation-auto` utilities to control whether an element should explicitly create a new stacking context:

```
    <div class="isolate ...">  <!-- ... --></div>
```

- Responsive design

Prefix an `isolation` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
    <div class="isolate md:isolation-auto ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states).

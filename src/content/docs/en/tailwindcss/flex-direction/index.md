---
title: "flex-direction - Flexbox & Grid - Tailwind CSS"
description: "Use flex-row to position flex items horizontally in the same direction as text:"
---

Source URL: https://tailwindcss.com/docs/flex-direction

# flex-direction - Flexbox & Grid - Tailwind CSS

| Class              | Styles                            |
| ------------------ | --------------------------------- |
| `flex-row`         | `flex-direction: row;`            |
| `flex-row-reverse` | `flex-direction: row-reverse;`    |
| `flex-col`         | `flex-direction: column;`         |
| `flex-col-reverse` | `flex-direction: column-reverse;` |

## Examples

- Row

Use `flex-row` to position flex items horizontally in the same direction as text:

01

02

03

```
    <div class="flex flex-row ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

- Row reversed

Use `flex-row-reverse` to position flex items horizontally in the opposite direction:

01

02

03

```
    <div class="flex flex-row-reverse ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

- Column

Use `flex-col` to position flex items vertically:

01

02

03

```
    <div class="flex flex-col ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

- Column reversed

Use `flex-col-reverse` to position flex items vertically in the opposite direction:

01

02

03

```
    <div class="flex flex-col-reverse ...">  <div>01</div>  <div>02</div>  <div>03</div></div>
```

- Responsive design

Prefix a `flex-direction` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
    <div class="flex flex-col md:flex-row ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states).

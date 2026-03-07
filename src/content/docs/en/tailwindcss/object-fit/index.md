---
title: "object-fit - Layout - Tailwind CSS"
description: "Use the object-cover utility to resize an element's content to cover its container:"
---

Source URL: https://tailwindcss.com/docs/object-fit

# object-fit - Layout - Tailwind CSS

| Class               | Styles                    |
| ------------------- | ------------------------- |
| `object-contain`    | `object-fit: contain;`    |
| `object-cover`      | `object-fit: cover;`      |
| `object-fill`       | `object-fit: fill;`       |
| `object-none`       | `object-fit: none;`       |
| `object-scale-down` | `object-fit: scale-down;` |

## Examples

- Resizing to cover

Use the `object-cover` utility to resize an element's content to cover its container:

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
    <img class="h-48 w-96 object-cover ..." src="/img/mountains.jpg" />
```

- Containing within

Use the `object-contain` utility to resize an element's content to stay contained within its container:

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
    <img class="h-48 w-96 object-contain ..." src="/img/mountains.jpg" />
```

- Stretching to fit

Use the `object-fill` utility to stretch an element's content to fit its container:

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
    <img class="h-48 w-96 object-fill ..." src="/img/mountains.jpg" />
```

- Scaling down

Use the `object-scale-down` utility to display an element's content at its original size but scale it down to fit its container if necessary:

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=128&h=160&q=80)

```
    <img class="h-48 w-96 object-scale-down ..." src="/img/mountains.jpg" />
```

- Using the original size

Use the `object-none` utility to display an element's content at its original size ignoring the container size:

![](https://images.unsplash.com/photo-1554629947-334ff61d85dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&h=1000&q=90)

```
    <img class="h-48 w-96 object-none ..." src="/img/mountains.jpg" />
```

- Responsive design

Prefix an `object-fit` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
    <img class="object-contain md:object-cover" src="/img/mountains.jpg" />
```

Learn more about using variants in the [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states).

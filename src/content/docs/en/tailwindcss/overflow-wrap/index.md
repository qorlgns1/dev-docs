---
title: "overflow-wrap - Typography - Tailwind CSS"
description: "Use the wrap-break-word utility to allow line breaks between letters in a word if needed:"
---

Source URL: https://tailwindcss.com/docs/overflow-wrap

# overflow-wrap - Typography - Tailwind CSS

| Class             | Styles                       |
| ----------------- | ---------------------------- |
| `wrap-break-word` | `overflow-wrap: break-word;` |
| `wrap-anywhere`   | `overflow-wrap: anywhere;`   |
| `wrap-normal`     | `overflow-wrap: normal;`     |

## Examples

- Wrapping mid-word

Use the `wrap-break-word` utility to allow line breaks between letters in a word if needed:

The longest word in any of the major English language dictionaries is pneumonoultramicroscopicsilicovolcanoconiosis, a word that refers to a lung disease contracted from the inhalation of very fine silica particles, specifically from a volcano; medically, it is the same as silicosis.

```
    <p class="wrap-break-word">The longest word in any of the major...</p>
```

- Wrapping anywhere

The `wrap-anywhere` utility behaves similarly to `wrap-break-word`, except that the browser factors in mid-word line breaks when calculating the intrinsic size of the element:

wrap-break-word

![](https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80)

Jay Riemenschneider

jason.riemenschneider@vandelayindustries.com

wrap-anywhere

![](https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80)

Jay Riemenschneider

jason.riemenschneider@vandelayindustries.com

```
    <div class="flex max-w-sm">  <img class="size-16 rounded-full" src="/img/profile.jpg" />  <div class="wrap-break-word">    <p class="font-medium">Jay Riemenschneider</p>    <p>jason.riemenschneider@vandelayindustries.com</p>  </div></div><div class="flex max-w-sm">  <img class="size-16 rounded-full" src="/img/profile.jpg" />  <div class="wrap-anywhere">    <p class="font-medium">Jay Riemenschneider</p>    <p>jason.riemenschneider@vandelayindustries.com</p>  </div></div>
```

This is useful for wrapping text inside of `flex` containers, where you would usually need to set `min-width: 0` on the child element to allow it to shrink below its content size.

- Wrapping normally

Use the `wrap-normal` utility to only allow line breaks at natural wrapping points, like spaces, hyphens, and punctuation:

The longest word in any of the major English language dictionaries is pneumonoultramicroscopicsilicovolcanoconiosis, a word that refers to a lung disease contracted from the inhalation of very fine silica particles, specifically from a volcano; medically, it is the same as silicosis.

```
    <p class="wrap-normal">The longest word in any of the major...</p>
```

- Responsive design

Prefix an `overflow-wrap` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
    <p class="wrap-normal md:wrap-break-word ...">  Lorem ipsum dolor sit amet...</p>
```

Learn more about using variants in the [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states).

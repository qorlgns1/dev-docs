---
title: "scroll-margin - Interactivity - Tailwind CSS"
description: "Use the scroll-mt-<number>, scroll-mr-<number>, scroll-mb-<number>, and scroll-ml-<number> utilities like scroll-ml-4 and scroll-mt-6 to set the scrol..."
---

Source URL: https://tailwindcss.com/docs/scroll-margin

# scroll-margin - Interactivity - Tailwind CSS

| Class                            | Styles                                                          |
| -------------------------------- | --------------------------------------------------------------- |
| `scroll-m-<number>`              | `scroll-margin: calc(var(--spacing) * <number>);`               |
| `-scroll-m-<number>`             | `scroll-margin: calc(var(--spacing) * -<number>);`              |
| `scroll-m-(<custom-property>)`   | `scroll-margin: var(<custom-property>);`                        |
| `scroll-m-[<value>]`             | `scroll-margin: <value>;`                                       |
| `scroll-mx-<number>`             | `scroll-margin-inline: calc(var(--spacing) * <number>);`        |
| `-scroll-mx-<number>`            | `scroll-margin-inline: calc(var(--spacing) * -<number>);`       |
| `scroll-mx-(<custom-property>)`  | `scroll-margin-inline: var(<custom-property>);`                 |
| `scroll-mx-[<value>]`            | `scroll-margin-inline: <value>;`                                |
| `scroll-my-<number>`             | `scroll-margin-block: calc(var(--spacing) * <number>);`         |
| `-scroll-my-<number>`            | `scroll-margin-block: calc(var(--spacing) * -<number>);`        |
| `scroll-my-(<custom-property>)`  | `scroll-margin-block: var(<custom-property>);`                  |
| `scroll-my-[<value>]`            | `scroll-margin-block: <value>;`                                 |
| `scroll-ms-<number>`             | `scroll-margin-inline-start: calc(var(--spacing) * <number>);`  |
| `-scroll-ms-<number>`            | `scroll-margin-inline-start: calc(var(--spacing) * -<number>);` |
| `scroll-ms-(<custom-property>)`  | `scroll-margin-inline-start: var(<custom-property>);`           |
| `scroll-ms-[<value>]`            | `scroll-margin-inline-start: <value>;`                          |
| `scroll-me-<number>`             | `scroll-margin-inline-end: calc(var(--spacing) * <number>);`    |
| `-scroll-me-<number>`            | `scroll-margin-inline-end: calc(var(--spacing) * -<number>);`   |
| `scroll-me-(<custom-property>)`  | `scroll-margin-inline-end: var(<custom-property>);`             |
| `scroll-me-[<value>]`            | `scroll-margin-inline-end: <value>;`                            |
| `scroll-mbs-<number>`            | `scroll-margin-block-start: calc(var(--spacing) * <number>);`   |
| `-scroll-mbs-<number>`           | `scroll-margin-block-start: calc(var(--spacing) * -<number>);`  |
| `scroll-mbs-(<custom-property>)` | `scroll-margin-block-start: var(<custom-property>);`            |
| `scroll-mbs-[<value>]`           | `scroll-margin-block-start: <value>;`                           |
| `scroll-mbe-<number>`            | `scroll-margin-block-end: calc(var(--spacing) * <number>);`     |
| `-scroll-mbe-<number>`           | `scroll-margin-block-end: calc(var(--spacing) * -<number>);`    |
| `scroll-mbe-(<custom-property>)` | `scroll-margin-block-end: var(<custom-property>);`              |
| `scroll-mbe-[<value>]`           | `scroll-margin-block-end: <value>;`                             |
| `scroll-mt-<number>`             | `scroll-margin-top: calc(var(--spacing) * <number>);`           |
| `-scroll-mt-<number>`            | `scroll-margin-top: calc(var(--spacing) * -<number>);`          |
| `scroll-mt-(<custom-property>)`  | `scroll-margin-top: var(<custom-property>);`                    |
| `scroll-mt-[<value>]`            | `scroll-margin-top: <value>;`                                   |
| `scroll-mr-<number>`             | `scroll-margin-right: calc(var(--spacing) * <number>);`         |
| `-scroll-mr-<number>`            | `scroll-margin-right: calc(var(--spacing) * -<number>);`        |
| `scroll-mr-(<custom-property>)`  | `scroll-margin-right: var(<custom-property>);`                  |
| `scroll-mr-[<value>]`            | `scroll-margin-right: <value>;`                                 |
| `scroll-mb-<number>`             | `scroll-margin-bottom: calc(var(--spacing) * <number>);`        |
| `-scroll-mb-<number>`            | `scroll-margin-bottom: calc(var(--spacing) * -<number>);`       |
| `scroll-mb-(<custom-property>)`  | `scroll-margin-bottom: var(<custom-property>);`                 |
| `scroll-mb-[<value>]`            | `scroll-margin-bottom: <value>;`                                |
| `scroll-ml-<number>`             | `scroll-margin-left: calc(var(--spacing) * <number>);`          |
| `-scroll-ml-<number>`            | `scroll-margin-left: calc(var(--spacing) * -<number>);`         |
| `scroll-ml-(<custom-property>)`  | `scroll-margin-left: var(<custom-property>);`                   |
| `scroll-ml-[<value>]`            | `scroll-margin-left: <value>;`                                  |

Show more

## Examples

- Basic example

Use the `scroll-mt-<number>`, `scroll-mr-<number>`, `scroll-mb-<number>`, and `scroll-ml-<number>` utilities like `scroll-ml-4` and `scroll-mt-6` to set the scroll offset around items within a snap container:

Scroll in the grid of images to see the expected behavior

![](https://images.unsplash.com/photo-1604999565976-8913ad2ddb7c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=320&h=160&q=80)

![](https://images.unsplash.com/photo-1540206351-d6465b3ac5c1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=320&h=160&q=80)

![](https://images.unsplash.com/photo-1622890806166-111d7f6c7c97?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=320&h=160&q=80)

![](https://images.unsplash.com/photo-1590523277543-a94d2e4eb00b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=320&h=160&q=80)

![](https://images.unsplash.com/photo-1575424909138-46b05e5919ec?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=320&h=160&q=80)

```
    <div class="snap-x ...">  <div class="snap-start scroll-ml-6 ...">    <img src="/img/vacation-01.jpg"/>  </div>  <div class="snap-start scroll-ml-6 ...">    <img src="/img/vacation-02.jpg"/>  </div>  <div class="snap-start scroll-ml-6 ...">    <img src="/img/vacation-03.jpg"/>  </div>  <div class="snap-start scroll-ml-6 ...">    <img src="/img/vacation-04.jpg"/>  </div>  <div class="snap-start scroll-ml-6 ...">    <img src="/img/vacation-05.jpg"/>  </div></div>
```

- Using negative values

To use a negative scroll margin value, prefix the class name with a dash to convert it to a negative value:

```
    <div class="snap-start -scroll-ml-6 ...">  <!-- ... --></div>
```

- Using logical properties

Use the `scroll-ms-<number>` and `scroll-me-<number>` utilities to set the `scroll-margin-inline-start` and `scroll-margin-inline-end` [logical properties](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Logical_Properties/Basic_concepts), which map to either the left or right side based on the text direction:

Scroll in the grid of images to see the expected behavior

Left-to-right

![](https://images.unsplash.com/photo-1604999565976-8913ad2ddb7c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=320&h=160&q=80)

![](https://images.unsplash.com/photo-1540206351-d6465b3ac5c1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=320&h=160&q=80)

![](https://images.unsplash.com/photo-1622890806166-111d7f6c7c97?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=320&h=160&q=80)

![](https://images.unsplash.com/photo-1590523277543-a94d2e4eb00b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=320&h=160&q=80)

![](https://images.unsplash.com/photo-1575424909138-46b05e5919ec?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=320&h=160&q=80)

Right-to-left

![](https://images.unsplash.com/photo-1604999565976-8913ad2ddb7c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=320&h=160&q=80)

![](https://images.unsplash.com/photo-1540206351-d6465b3ac5c1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=320&h=160&q=80)

![](https://images.unsplash.com/photo-1622890806166-111d7f6c7c97?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=320&h=160&q=80)

![](https://images.unsplash.com/photo-1590523277543-a94d2e4eb00b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=320&h=160&q=80)

![](https://images.unsplash.com/photo-1575424909138-46b05e5919ec?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=320&h=160&q=80)

```
    <div dir="ltr">  <div class="snap-x ...">    <div class="snap-start scroll-ms-6 ...">      <img src="/img/vacation-01.jpg"/>    </div>    <!-- ... -->  </div></div><div dir="rtl">  <div class="snap-x ...">    <div class="snap-start scroll-ms-6 ...">      <img src="/img/vacation-01.jpg"/>    </div>    <!-- ... -->  </div></div>
```

For more control, you can also use the [LTR and RTL modifiers](https://tailwindcss.com/docs/hover-focus-and-other-states#rtl-support) to conditionally apply specific styles depending on the current text direction.

Use the `scroll-mbs-<number>` and `scroll-mbe-<number>` utilities to set the `scroll-margin-block-start` and `scroll-margin-block-end` logical properties, which map to either the top or bottom side based on the writing mode:

```
    <div class="snap-y ...">  <div class="snap-start scroll-mbs-6 ...">    <!-- ... -->  </div></div>
```

- Using a custom value

Use utilities like `scroll-ml-[<value>]` and `scroll-me-[<value>]` to set the scroll margin based on a completely custom value:

```
    <div class="scroll-ml-[24rem] ...">  <!-- ... --></div>
```

For CSS variables, you can also use the `scroll-ml-(<custom-property>)` syntax:

```
    <div class="scroll-ml-(--my-scroll-margin) ...">  <!-- ... --></div>
```

This is just a shorthand for `scroll-ml-[var(<custom-property>)]` that adds the `var()` function for you automatically.

- Responsive design

Prefix a `scroll-margin` utility with a breakpoint variant like `md:` to only apply the utility at medium screen sizes and above:

```
    <div class="scroll-m-8 md:scroll-m-0 ...">  <!-- ... --></div>
```

Learn more about using variants in the [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states).

## Customizing your theme

The `scroll-m-<number>`,`scroll-mx-<number>`,`scroll-my-<number>`,`scroll-ms-<number>`,`scroll-me-<number>`,`scroll-mbs-<number>`,`scroll-mbe-<number>`,`scroll-mt-<number>`,`scroll-mr-<number>`,`scroll-mb-<number>`, and `scroll-ml-<number>` utilities are driven by the `--spacing` theme variable, which can be customized in your own theme:

```
    @theme {  --spacing: 1px; }
```

Learn more about customizing the spacing scale in the [theme variable documentation](https://tailwindcss.com/docs/theme).

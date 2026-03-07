---
title: "border-radius - 테두리 - Tailwind CSS"
description: "rounded-sm 및 rounded-md 같은 유틸리티를 사용해 요소에 서로 다른 border radius 크기를 적용하세요:"
---

# border-radius - 테두리 - Tailwind CSS

| 클래스                           | 스타일                                                                                                                                 |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `rounded-xs`                     | `border-radius: var(--radius-xs); /* 0.125rem (2px) */`                                                                                |
| `rounded-sm`                     | `border-radius: var(--radius-sm); /* 0.25rem (4px) */`                                                                                 |
| `rounded-md`                     | `border-radius: var(--radius-md); /* 0.375rem (6px) */`                                                                                |
| `rounded-lg`                     | `border-radius: var(--radius-lg); /* 0.5rem (8px) */`                                                                                  |
| `rounded-xl`                     | `border-radius: var(--radius-xl); /* 0.75rem (12px) */`                                                                                |
| `rounded-2xl`                    | `border-radius: var(--radius-2xl); /* 1rem (16px) */`                                                                                  |
| `rounded-3xl`                    | `border-radius: var(--radius-3xl); /* 1.5rem (24px) */`                                                                                |
| `rounded-4xl`                    | `border-radius: var(--radius-4xl); /* 2rem (32px) */`                                                                                  |
| `rounded-none`                   | `border-radius: 0;`                                                                                                                    |
| `rounded-full`                   | `border-radius: calc(infinity * 1px);`                                                                                                 |
| `rounded-(<custom-property>)`    | `border-radius: var(<custom-property>);`                                                                                               |
| `rounded-[<value>]`              | `border-radius: <value>;`                                                                                                              |
| `rounded-s-xs`                   | `border-start-start-radius: var(--radius-xs); /* 0.125rem (2px) */ border-end-start-radius: var(--radius-xs); /* 0.125rem (2px) */`    |
| `rounded-s-sm`                   | `border-start-start-radius: var(--radius-sm); /* 0.25rem (4px) */ border-end-start-radius: var(--radius-sm); /* 0.25rem (4px) */`      |
| `rounded-s-md`                   | `border-start-start-radius: var(--radius-md); /* 0.375rem (6px) */ border-end-start-radius: var(--radius-md); /* 0.375rem (6px) */`    |
| `rounded-s-lg`                   | `border-start-start-radius: var(--radius-lg); /* 0.5rem (8px) */ border-end-start-radius: var(--radius-lg); /* 0.5rem (8px) */`        |
| `rounded-s-xl`                   | `border-start-start-radius: var(--radius-xl); /* 0.75rem (12px) */ border-end-start-radius: var(--radius-xl); /* 0.75rem (12px) */`    |
| `rounded-s-2xl`                  | `border-start-start-radius: var(--radius-2xl); /* 1rem (16px) */ border-end-start-radius: var(--radius-2xl); /* 1rem (16px) */`        |
| `rounded-s-3xl`                  | `border-start-start-radius: var(--radius-3xl); /* 1.5rem (24px) */ border-end-start-radius: var(--radius-3xl); /* 1.5rem (24px) */`    |
| `rounded-s-4xl`                  | `border-start-start-radius: var(--radius-4xl); /* 2rem (32px) */ border-end-start-radius: var(--radius-4xl); /* 2rem (32px) */`        |
| `rounded-s-none`                 | `border-start-start-radius: 0; border-end-start-radius: 0;`                                                                            |
| `rounded-s-full`                 | `border-start-start-radius: calc(infinity * 1px); border-end-start-radius: calc(infinity * 1px);`                                      |
| `rounded-s-(<custom-property>)`  | `border-start-start-radius: var(<custom-property>); border-end-start-radius: var(<custom-property>);`                                  |
| `rounded-s-[<value>]`            | `border-start-start-radius: <value>; border-end-start-radius: <value>;`                                                                |
| `rounded-e-xs`                   | `border-start-end-radius: var(--radius-xs); /* 0.125rem (2px) */ border-end-end-radius: var(--radius-xs); /* 0.125rem (2px) */`        |
| `rounded-e-sm`                   | `border-start-end-radius: var(--radius-sm); /* 0.25rem (4px) */ border-end-end-radius: var(--radius-sm); /* 0.25rem (4px) */`          |
| `rounded-e-md`                   | `border-start-end-radius: var(--radius-md); /* 0.375rem (6px) */ border-end-end-radius: var(--radius-md); /* 0.375rem (6px) */`        |
| `rounded-e-lg`                   | `border-start-end-radius: var(--radius-lg); /* 0.5rem (8px) */ border-end-end-radius: var(--radius-lg); /* 0.5rem (8px) */`            |
| `rounded-e-xl`                   | `border-start-end-radius: var(--radius-xl); /* 0.75rem (12px) */ border-end-end-radius: var(--radius-xl); /* 0.75rem (12px) */`        |
| `rounded-e-2xl`                  | `border-start-end-radius: var(--radius-2xl); /* 1rem (16px) */ border-end-end-radius: var(--radius-2xl); /* 1rem (16px) */`            |
| `rounded-e-3xl`                  | `border-start-end-radius: var(--radius-3xl); /* 1.5rem (24px) */ border-end-end-radius: var(--radius-3xl); /* 1.5rem (24px) */`        |
| `rounded-e-4xl`                  | `border-start-end-radius: var(--radius-4xl); /* 2rem (32px) */ border-end-end-radius: var(--radius-4xl); /* 2rem (32px) */`            |
| `rounded-e-none`                 | `border-start-end-radius: 0; border-end-end-radius: 0;`                                                                                |
| `rounded-e-full`                 | `border-start-end-radius: calc(infinity * 1px); border-end-end-radius: calc(infinity * 1px);`                                          |
| `rounded-e-(<custom-property>)`  | `border-start-end-radius: var(<custom-property>); border-end-end-radius: var(<custom-property>);`                                      |
| `rounded-e-[<value>]`            | `border-start-end-radius: <value>; border-end-end-radius: <value>;`                                                                    |
| `rounded-t-xs`                   | `border-top-left-radius: var(--radius-xs); /* 0.125rem (2px) */ border-top-right-radius: var(--radius-xs); /* 0.125rem (2px) */`       |
| `rounded-t-sm`                   | `border-top-left-radius: var(--radius-sm); /* 0.25rem (4px) */ border-top-right-radius: var(--radius-sm); /* 0.25rem (4px) */`         |
| `rounded-t-md`                   | `border-top-left-radius: var(--radius-md); /* 0.375rem (6px) */ border-top-right-radius: var(--radius-md); /* 0.375rem (6px) */`       |
| `rounded-t-lg`                   | `border-top-left-radius: var(--radius-lg); /* 0.5rem (8px) */ border-top-right-radius: var(--radius-lg); /* 0.5rem (8px) */`           |
| `rounded-t-xl`                   | `border-top-left-radius: var(--radius-xl); /* 0.75rem (12px) */ border-top-right-radius: var(--radius-xl); /* 0.75rem (12px) */`       |
| `rounded-t-2xl`                  | `border-top-left-radius: var(--radius-2xl); /* 1rem (16px) */ border-top-right-radius: var(--radius-2xl); /* 1rem (16px) */`           |
| `rounded-t-3xl`                  | `border-top-left-radius: var(--radius-3xl); /* 1.5rem (24px) */ border-top-right-radius: var(--radius-3xl); /* 1.5rem (24px) */`       |
| `rounded-t-4xl`                  | `border-top-left-radius: var(--radius-4xl); /* 2rem (32px) */ border-top-right-radius: var(--radius-4xl); /* 2rem (32px) */`           |
| `rounded-t-none`                 | `border-top-left-radius: 0; border-top-right-radius: 0;`                                                                               |
| `rounded-t-full`                 | `border-top-left-radius: calc(infinity * 1px); border-top-right-radius: calc(infinity * 1px);`                                         |
| `rounded-t-(<custom-property>)`  | `border-top-left-radius: var(<custom-property>); border-top-right-radius: var(<custom-property>);`                                     |
| `rounded-t-[<value>]`            | `border-top-left-radius: <value>; border-top-right-radius: <value>;`                                                                   |
| `rounded-r-xs`                   | `border-top-right-radius: var(--radius-xs); /* 0.125rem (2px) */ border-bottom-right-radius: var(--radius-xs); /* 0.125rem (2px) */`   |
| `rounded-r-sm`                   | `border-top-right-radius: var(--radius-sm); /* 0.25rem (4px) */ border-bottom-right-radius: var(--radius-sm); /* 0.25rem (4px) */`     |
| `rounded-r-md`                   | `border-top-right-radius: var(--radius-md); /* 0.375rem (6px) */ border-bottom-right-radius: var(--radius-md); /* 0.375rem (6px) */`   |
| `rounded-r-lg`                   | `border-top-right-radius: var(--radius-lg); /* 0.5rem (8px) */ border-bottom-right-radius: var(--radius-lg); /* 0.5rem (8px) */`       |
| `rounded-r-xl`                   | `border-top-right-radius: var(--radius-xl); /* 0.75rem (12px) */ border-bottom-right-radius: var(--radius-xl); /* 0.75rem (12px) */`   |
| `rounded-r-2xl`                  | `border-top-right-radius: var(--radius-2xl); /* 1rem (16px) */ border-bottom-right-radius: var(--radius-2xl); /* 1rem (16px) */`       |
| `rounded-r-3xl`                  | `border-top-right-radius: var(--radius-3xl); /* 1.5rem (24px) */ border-bottom-right-radius: var(--radius-3xl); /* 1.5rem (24px) */`   |
| `rounded-r-4xl`                  | `border-top-right-radius: var(--radius-4xl); /* 2rem (32px) */ border-bottom-right-radius: var(--radius-4xl); /* 2rem (32px) */`       |
| `rounded-r-none`                 | `border-top-right-radius: 0; border-bottom-right-radius: 0;`                                                                           |
| `rounded-r-full`                 | `border-top-right-radius: calc(infinity * 1px); border-bottom-right-radius: calc(infinity * 1px);`                                     |
| `rounded-r-(<custom-property>)`  | `border-top-right-radius: var(<custom-property>); border-bottom-right-radius: var(<custom-property>);`                                 |
| `rounded-r-[<value>]`            | `border-top-right-radius: <value>; border-bottom-right-radius: <value>;`                                                               |
| `rounded-b-xs`                   | `border-bottom-right-radius: var(--radius-xs); /* 0.125rem (2px) */ border-bottom-left-radius: var(--radius-xs); /* 0.125rem (2px) */` |
| `rounded-b-sm`                   | `border-bottom-right-radius: var(--radius-sm); /* 0.25rem (4px) */ border-bottom-left-radius: var(--radius-sm); /* 0.25rem (4px) */`   |
| `rounded-b-md`                   | `border-bottom-right-radius: var(--radius-md); /* 0.375rem (6px) */ border-bottom-left-radius: var(--radius-md); /* 0.375rem (6px) */` |
| `rounded-b-lg`                   | `border-bottom-right-radius: var(--radius-lg); /* 0.5rem (8px) */ border-bottom-left-radius: var(--radius-lg); /* 0.5rem (8px) */`     |
| `rounded-b-xl`                   | `border-bottom-right-radius: var(--radius-xl); /* 0.75rem (12px) */ border-bottom-left-radius: var(--radius-xl); /* 0.75rem (12px) */` |
| `rounded-b-2xl`                  | `border-bottom-right-radius: var(--radius-2xl); /* 1rem (16px) */ border-bottom-left-radius: var(--radius-2xl); /* 1rem (16px) */`     |
| `rounded-b-3xl`                  | `border-bottom-right-radius: var(--radius-3xl); /* 1.5rem (24px) */ border-bottom-left-radius: var(--radius-3xl); /* 1.5rem (24px) */` |
| `rounded-b-4xl`                  | `border-bottom-right-radius: var(--radius-4xl); /* 2rem (32px) */ border-bottom-left-radius: var(--radius-4xl); /* 2rem (32px) */`     |
| `rounded-b-none`                 | `border-bottom-right-radius: 0; border-bottom-left-radius: 0;`                                                                         |
| `rounded-b-full`                 | `border-bottom-right-radius: calc(infinity * 1px); border-bottom-left-radius: calc(infinity * 1px);`                                   |
| `rounded-b-(<custom-property>)`  | `border-bottom-right-radius: var(<custom-property>); border-bottom-left-radius: var(<custom-property>);`                               |
| `rounded-b-[<value>]`            | `border-bottom-right-radius: <value>; border-bottom-left-radius: <value>;`                                                             |
| `rounded-l-xs`                   | `border-top-left-radius: var(--radius-xs); /* 0.125rem (2px) */ border-bottom-left-radius: var(--radius-xs); /* 0.125rem (2px) */`     |
| `rounded-l-sm`                   | `border-top-left-radius: var(--radius-sm); /* 0.25rem (4px) */ border-bottom-left-radius: var(--radius-sm); /* 0.25rem (4px) */`       |
| `rounded-l-md`                   | `border-top-left-radius: var(--radius-md); /* 0.375rem (6px) */ border-bottom-left-radius: var(--radius-md); /* 0.375rem (6px) */`     |
| `rounded-l-lg`                   | `border-top-left-radius: var(--radius-lg); /* 0.5rem (8px) */ border-bottom-left-radius: var(--radius-lg); /* 0.5rem (8px) */`         |
| `rounded-l-xl`                   | `border-top-left-radius: var(--radius-xl); /* 0.75rem (12px) */ border-bottom-left-radius: var(--radius-xl); /* 0.75rem (12px) */`     |
| `rounded-l-2xl`                  | `border-top-left-radius: var(--radius-2xl); /* 1rem (16px) */ border-bottom-left-radius: var(--radius-2xl); /* 1rem (16px) */`         |
| `rounded-l-3xl`                  | `border-top-left-radius: var(--radius-3xl); /* 1.5rem (24px) */ border-bottom-left-radius: var(--radius-3xl); /* 1.5rem (24px) */`     |
| `rounded-l-4xl`                  | `border-top-left-radius: var(--radius-4xl); /* 2rem (32px) */ border-bottom-left-radius: var(--radius-4xl); /* 2rem (32px) */`         |
| `rounded-l-none`                 | `border-top-left-radius: 0; border-bottom-left-radius: 0;`                                                                             |
| `rounded-l-full`                 | `border-top-left-radius: calc(infinity * 1px); border-bottom-left-radius: calc(infinity * 1px);`                                       |
| `rounded-l-(<custom-property>)`  | `border-top-left-radius: var(<custom-property>); border-bottom-left-radius: var(<custom-property>);`                                   |
| `rounded-l-[<value>]`            | `border-top-left-radius: <value>; border-bottom-left-radius: <value>;`                                                                 |
| `rounded-ss-xs`                  | `border-start-start-radius: var(--radius-xs); /* 0.125rem (2px) */`                                                                    |
| `rounded-ss-sm`                  | `border-start-start-radius: var(--radius-sm); /* 0.25rem (4px) */`                                                                     |
| `rounded-ss-md`                  | `border-start-start-radius: var(--radius-md); /* 0.375rem (6px) */`                                                                    |
| `rounded-ss-lg`                  | `border-start-start-radius: var(--radius-lg); /* 0.5rem (8px) */`                                                                      |
| `rounded-ss-xl`                  | `border-start-start-radius: var(--radius-xl); /* 0.75rem (12px) */`                                                                    |
| `rounded-ss-2xl`                 | `border-start-start-radius: var(--radius-2xl); /* 1rem (16px) */`                                                                      |
| `rounded-ss-3xl`                 | `border-start-start-radius: var(--radius-3xl); /* 1.5rem (24px) */`                                                                    |
| `rounded-ss-4xl`                 | `border-start-start-radius: var(--radius-4xl); /* 2rem (32px) */`                                                                      |
| `rounded-ss-none`                | `border-start-start-radius: 0;`                                                                                                        |
| `rounded-ss-full`                | `border-start-start-radius: calc(infinity * 1px);`                                                                                     |
| `rounded-ss-(<custom-property>)` | `border-start-start-radius: var(<custom-property>);`                                                                                   |
| `rounded-ss-[<value>]`           | `border-start-start-radius: <value>;`                                                                                                  |
| `rounded-se-xs`                  | `border-start-end-radius: var(--radius-xs); /* 0.125rem (2px) */`                                                                      |
| `rounded-se-sm`                  | `border-start-end-radius: var(--radius-sm); /* 0.25rem (4px) */`                                                                       |
| `rounded-se-md`                  | `border-start-end-radius: var(--radius-md); /* 0.375rem (6px) */`                                                                      |
| `rounded-se-lg`                  | `border-start-end-radius: var(--radius-lg); /* 0.5rem (8px) */`                                                                        |
| `rounded-se-xl`                  | `border-start-end-radius: var(--radius-xl); /* 0.75rem (12px) */`                                                                      |
| `rounded-se-2xl`                 | `border-start-end-radius: var(--radius-2xl); /* 1rem (16px) */`                                                                        |
| `rounded-se-3xl`                 | `border-start-end-radius: var(--radius-3xl); /* 1.5rem (24px) */`                                                                      |

`rounded-se-4xl`| `border-start-end-radius: var(--radius-4xl); /* 2rem (32px) */`
`rounded-se-none`| `border-start-end-radius: 0;`
`rounded-se-full`| `border-start-end-radius: calc(infinity * 1px);`
`rounded-se-(<custom-property>)`| `border-start-end-radius: var(<custom-property>);`
`rounded-se-[<value>]`| `border-start-end-radius: <value>;`
`rounded-ee-xs`| `border-end-end-radius: var(--radius-xs); /* 0.125rem (2px) */`
`rounded-ee-sm`| `border-end-end-radius: var(--radius-sm); /* 0.25rem (4px) */`
`rounded-ee-md`| `border-end-end-radius: var(--radius-md); /* 0.375rem (6px) */`
`rounded-ee-lg`| `border-end-end-radius: var(--radius-lg); /* 0.5rem (8px) */`
`rounded-ee-xl`| `border-end-end-radius: var(--radius-xl); /* 0.75rem (12px) */`
`rounded-ee-2xl`| `border-end-end-radius: var(--radius-2xl); /* 1rem (16px) */`
`rounded-ee-3xl`| `border-end-end-radius: var(--radius-3xl); /* 1.5rem (24px) */`
`rounded-ee-4xl`| `border-end-end-radius: var(--radius-4xl); /* 2rem (32px) */`
`rounded-ee-none`| `border-end-end-radius: 0;`
`rounded-ee-full`| `border-end-end-radius: calc(infinity * 1px);`
`rounded-ee-(<custom-property>)`| `border-end-end-radius: var(<custom-property>);`
`rounded-ee-[<value>]`| `border-end-end-radius: <value>;`
`rounded-es-xs`| `border-end-start-radius: var(--radius-xs); /* 0.125rem (2px) */`
`rounded-es-sm`| `border-end-start-radius: var(--radius-sm); /* 0.25rem (4px) */`
`rounded-es-md`| `border-end-start-radius: var(--radius-md); /* 0.375rem (6px) */`
`rounded-es-lg`| `border-end-start-radius: var(--radius-lg); /* 0.5rem (8px) */`
`rounded-es-xl`| `border-end-start-radius: var(--radius-xl); /* 0.75rem (12px) */`
`rounded-es-2xl`| `border-end-start-radius: var(--radius-2xl); /* 1rem (16px) */`
`rounded-es-3xl`| `border-end-start-radius: var(--radius-3xl); /* 1.5rem (24px) */`
`rounded-es-4xl`| `border-end-start-radius: var(--radius-4xl); /* 2rem (32px) */`
`rounded-es-none`| `border-end-start-radius: 0;`
`rounded-es-full`| `border-end-start-radius: calc(infinity * 1px);`
`rounded-es-(<custom-property>)`| `border-end-start-radius: var(<custom-property>);`
`rounded-es-[<value>]`| `border-end-start-radius: <value>;`
`rounded-tl-xs`| `border-top-left-radius: var(--radius-xs); /* 0.125rem (2px) */`
`rounded-tl-sm`| `border-top-left-radius: var(--radius-sm); /* 0.25rem (4px) */`
`rounded-tl-md`| `border-top-left-radius: var(--radius-md); /* 0.375rem (6px) */`
`rounded-tl-lg`| `border-top-left-radius: var(--radius-lg); /* 0.5rem (8px) */`
`rounded-tl-xl`| `border-top-left-radius: var(--radius-xl); /* 0.75rem (12px) */`
`rounded-tl-2xl`| `border-top-left-radius: var(--radius-2xl); /* 1rem (16px) */`
`rounded-tl-3xl`| `border-top-left-radius: var(--radius-3xl); /* 1.5rem (24px) */`
`rounded-tl-4xl`| `border-top-left-radius: var(--radius-4xl); /* 2rem (32px) */`
`rounded-tl-none`| `border-top-left-radius: 0;`
`rounded-tl-full`| `border-top-left-radius: calc(infinity * 1px);`
`rounded-tl-(<custom-property>)`| `border-top-left-radius: var(<custom-property>);`
`rounded-tl-[<value>]`| `border-top-left-radius: <value>;`
`rounded-tr-xs`| `border-top-right-radius: var(--radius-xs); /* 0.125rem (2px) */`
`rounded-tr-sm`| `border-top-right-radius: var(--radius-sm); /* 0.25rem (4px) */`
`rounded-tr-md`| `border-top-right-radius: var(--radius-md); /* 0.375rem (6px) */`
`rounded-tr-lg`| `border-top-right-radius: var(--radius-lg); /* 0.5rem (8px) */`
`rounded-tr-xl`| `border-top-right-radius: var(--radius-xl); /* 0.75rem (12px) */`
`rounded-tr-2xl`| `border-top-right-radius: var(--radius-2xl); /* 1rem (16px) */`
`rounded-tr-3xl`| `border-top-right-radius: var(--radius-3xl); /* 1.5rem (24px) */`
`rounded-tr-4xl`| `border-top-right-radius: var(--radius-4xl); /* 2rem (32px) */`
`rounded-tr-none`| `border-top-right-radius: 0;`
`rounded-tr-full`| `border-top-right-radius: calc(infinity * 1px);`
`rounded-tr-(<custom-property>)`| `border-top-right-radius: var(<custom-property>);`
`rounded-tr-[<value>]`| `border-top-right-radius: <value>;`
`rounded-br-xs`| `border-bottom-right-radius: var(--radius-xs); /* 0.125rem (2px) */`
`rounded-br-sm`| `border-bottom-right-radius: var(--radius-sm); /* 0.25rem (4px) */`
`rounded-br-md`| `border-bottom-right-radius: var(--radius-md); /* 0.375rem (6px) */`
`rounded-br-lg`| `border-bottom-right-radius: var(--radius-lg); /* 0.5rem (8px) */`
`rounded-br-xl`| `border-bottom-right-radius: var(--radius-xl); /* 0.75rem (12px) */`
`rounded-br-2xl`| `border-bottom-right-radius: var(--radius-2xl); /* 1rem (16px) */`
`rounded-br-3xl`| `border-bottom-right-radius: var(--radius-3xl); /* 1.5rem (24px) */`
`rounded-br-4xl`| `border-bottom-right-radius: var(--radius-4xl); /* 2rem (32px) */`
`rounded-br-none`| `border-bottom-right-radius: 0;`
`rounded-br-full`| `border-bottom-right-radius: calc(infinity * 1px);`
`rounded-br-(<custom-property>)`| `border-bottom-right-radius: var(<custom-property>);`
`rounded-br-[<value>]`| `border-bottom-right-radius: <value>;`
`rounded-bl-xs`| `border-bottom-left-radius: var(--radius-xs); /* 0.125rem (2px) */`
`rounded-bl-sm`| `border-bottom-left-radius: var(--radius-sm); /* 0.25rem (4px) */`
`rounded-bl-md`| `border-bottom-left-radius: var(--radius-md); /* 0.375rem (6px) */`
`rounded-bl-lg`| `border-bottom-left-radius: var(--radius-lg); /* 0.5rem (8px) */`
`rounded-bl-xl`| `border-bottom-left-radius: var(--radius-xl); /* 0.75rem (12px) */`
`rounded-bl-2xl`| `border-bottom-left-radius: var(--radius-2xl); /* 1rem (16px) */`
`rounded-bl-3xl`| `border-bottom-left-radius: var(--radius-3xl); /* 1.5rem (24px) */`
`rounded-bl-4xl`| `border-bottom-left-radius: var(--radius-4xl); /* 2rem (32px) */`
`rounded-bl-none`| `border-bottom-left-radius: 0;`
`rounded-bl-full`| `border-bottom-left-radius: calc(infinity * 1px);`
`rounded-bl-(<custom-property>)`| `border-bottom-left-radius: var(<custom-property>);`
`rounded-bl-[<value>]`| `border-bottom-left-radius: <value>;`

더 보기

## 예제

- 기본 예제

`rounded-sm` 및 `rounded-md` 같은 유틸리티를 사용해 요소에 서로 다른 border radius 크기를 적용하세요:

rounded-sm

rounded-md

rounded-lg

rounded-xl

```
    <div class="rounded-sm ..."></div><div class="rounded-md ..."></div><div class="rounded-lg ..."></div><div class="rounded-xl ..."></div>
```

- 각 면을 개별적으로 둥글게 만들기

`rounded-t-md` 및 `rounded-r-lg` 같은 유틸리티를 사용해 요소의 한 면만 둥글게 만들 수 있습니다:

rounded-t-lg

rounded-r-lg

rounded-b-lg

rounded-l-lg

```
    <div class="rounded-t-lg ..."></div><div class="rounded-r-lg ..."></div><div class="rounded-b-lg ..."></div><div class="rounded-l-lg ..."></div>
```

- 각 모서리를 개별적으로 둥글게 만들기

`rounded-tr-md` 및 `rounded-tl-lg` 같은 유틸리티를 사용해 요소의 한 모서리만 둥글게 만들 수 있습니다:

rounded-tl-lg

rounded-tr-lg

rounded-br-lg

rounded-bl-lg

```
    <div class="rounded-tl-lg ..."></div><div class="rounded-tr-lg ..."></div><div class="rounded-br-lg ..."></div><div class="rounded-bl-lg ..."></div>
```

- 논리 속성 사용하기

`rounded-s-md` 및 `rounded-se-xl` 같은 유틸리티를 사용해 [논리 속성](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Logical_Properties/Basic_concepts)으로 border radius를 설정할 수 있으며, 이는 텍스트 방향에 따라 적절한 모서리에 매핑됩니다:

왼쪽에서 오른쪽

오른쪽에서 왼쪽

```
    <div dir="ltr">  <div class="rounded-s-lg ..."></div></div><div dir="rtl">  <div class="rounded-s-lg ..."></div></div>
```

다음은 사용 가능한 모든 border radius 논리 속성 유틸리티와, LTR 및 RTL 모드에서의 물리 속성 대응값입니다.

| 클래스         | 왼쪽에서 오른쪽 | 오른쪽에서 왼쪽 |
| -------------- | --------------- | --------------- |
| `rounded-s-*`  | `rounded-l-*`   | `rounded-r-*`   |
| `rounded-e-*`  | `rounded-r-*`   | `rounded-l-*`   |
| `rounded-ss-*` | `rounded-tl-*`  | `rounded-tr-*`  |
| `rounded-se-*` | `rounded-tr-*`  | `rounded-tl-*`  |
| `rounded-es-*` | `rounded-bl-*`  | `rounded-br-*`  |
| `rounded-ee-*` | `rounded-br-*`  | `rounded-bl-*`  |

더 세밀하게 제어하려면 [LTR 및 RTL modifiers](https://tailwindcss.com/docs/hover-focus-and-other-states#rtl-support)를 사용해 현재 텍스트 방향에 따라 특정 스타일을 조건부로 적용할 수도 있습니다.

- 알약형 버튼 만들기

`rounded-full` 유틸리티를 사용해 알약형 버튼을 만들 수 있습니다:

rounded-full

변경 사항 저장

```
    <button class="rounded-full ...">Save Changes</button>
```

- border radius 제거하기

`rounded-none` 유틸리티를 사용해 요소에 이미 적용된 border radius를 제거합니다:

rounded-none

변경 사항 저장

```
    <button class="rounded-none ...">Save Changes</button>
```

- 사용자 정의 값 사용하기

`rounded-[<value>]` 구문을 사용해 완전히 사용자 정의한 값으로 border radius를 설정할 수 있습니다:

```
    <div class="rounded-[2vw] ...">  <!-- ... --></div>
```

CSS 변수의 경우 `rounded-(<custom-property>)` 구문도 사용할 수 있습니다:

```
    <div class="rounded-(--my-radius) ...">  <!-- ... --></div>
```

이는 `var()` 함수를 자동으로 추가해 주는 `rounded-[var(<custom-property>)]`의 단축 표기입니다.

- 반응형 디자인

`border-radius` 유틸리티 앞에 `md:` 같은 브레이크포인트 변형을 붙이면 중간 크기 이상의 화면에서만 해당 유틸리티가 적용됩니다:

```
    <div class="rounded md:rounded-lg ...">  <!-- ... --></div>
```

변형 사용법은 [variants documentation](https://tailwindcss.com/docs/hover-focus-and-other-states)에서 자세히 알아보세요.

## 테마 커스터마이징

프로젝트에서 border radius 유틸리티를 커스터마이징하려면 `--radius-*` 테마 변수를 사용하세요:

```
    @theme {  --radius-5xl: 3rem; }
```

이제 마크업에서 `rounded-5xl` 유틸리티를 사용할 수 있습니다:

```
    <div class="rounded-5xl">  <!-- ... --></div>
```

테마 커스터마이징에 대한 자세한 내용은 [theme documentation](https://tailwindcss.com/docs/theme#customizing-your-theme)에서 확인하세요.

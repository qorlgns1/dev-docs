---
title: 'List formatting'
description: 'When working with lists of items, you can format them as conjunctions or disjunctions.'
---

Source URL: https://next-intl.dev/docs/usage/lists

# List formatting

When working with lists of items, you can format them as conjunctions or disjunctions.

Formatting aspects, like the used separators, differ per locale:

  * “HTML, CSS, and JavaScript” in `en-US`
  * “HTML, CSS und JavaScript” in `de-DE`

List formatting can be applied with the `useFormatter` hook:
```
    import {useFormatter} from 'next-intl';

    function Component() {
      const format = useFormatter();
      const items = ['HTML', 'CSS', 'JavaScript'];

      // Renders "HTML, CSS, and JavaScript"
      format.list(items, {type: 'conjunction'});

      // Renders "HTML, CSS, or JavaScript"
      format.list(items, {type: 'disjunction'});
    }
```

See the MDN docs about [`ListFormat`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/ListFormat) to learn more about the options that you can provide to the `list` function or try the [interactive explorer](https://www.intl-explorer.com/ListFormat) for `Intl.ListFormat`.

Note that lists can currently only be formatted via `useFormatter`, there’s no equivalent inline syntax for messages at this point.

To reuse list formats for multiple components, you can configure [global formats](https://next-intl.dev/docs/usage/configuration#formats).

[](https://next-intl.dev/docs/usage/lists#messages-array)How can I render an array of messages?

See the [arrays of messages guide](https://next-intl.dev/docs/usage/translations#arrays-of-messages).

## Formatting of React elements[](https://next-intl.dev/docs/usage/lists#react-elements)

Apart from string values, you can also pass arrays of React elements to the formatting function:
```
    import {useFormatter} from 'next-intl';

    function Component() {
      const format = useFormatter();

      const users = [
        {id: 1, name: 'Alice'},
        {id: 2, name: 'Bob'},
        {id: 3, name: 'Charlie'}
      ];

      const items = users.map((user) => (
        <a key={user.id} href={`/user/${user.id}`}>
          {user.name}
        </a>
      ));

      return <p>{format.list(items)}</p>;
    }
```

**Result:**
```
    <p>
      <a href="/user/1">Alice</a>, <a href="/user/2">Bob</a>, and
      <a href="/user/3">Charlie</a>
    </p>
```

Note that `format.list` will return an `Iterable<ReactElement>` in this case.


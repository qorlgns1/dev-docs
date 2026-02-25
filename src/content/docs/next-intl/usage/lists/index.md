---
title: '목록 포맷팅'
description: '항목 목록을 다룰 때, 목록을 접속형(conjunction) 또는 선택형(disjunction)으로 포맷할 수 있습니다.'
---

출처 URL: https://next-intl.dev/docs/usage/lists

# 목록 포맷팅

항목 목록을 다룰 때, 목록을 접속형(conjunction) 또는 선택형(disjunction)으로 포맷할 수 있습니다.

사용되는 구분자 같은 포맷팅 요소는 로캘마다 다릅니다:

  * “HTML, CSS, and JavaScript” in `en-US`
  * “HTML, CSS und JavaScript” in `de-DE`

목록 포맷팅은 `useFormatter` 훅으로 적용할 수 있습니다:
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

`list` 함수에 전달할 수 있는 옵션을 더 알아보려면 [`ListFormat`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/ListFormat)에 대한 MDN 문서를 참고하거나, `Intl.ListFormat`의 [interactive explorer](https://www.intl-explorer.com/ListFormat)를 사용해 보세요.

현재 목록은 `useFormatter`를 통해서만 포맷할 수 있으며, 지금 시점에서는 메시지용 동등한 인라인 문법이 없습니다.

여러 컴포넌트에서 목록 포맷을 재사용하려면 [global formats](https://next-intl.dev/docs/usage/configuration#formats)를 설정할 수 있습니다.

[](https://next-intl.dev/docs/usage/lists#messages-array)메시지 배열을 어떻게 렌더링하나요?

[메시지 배열 가이드](https://next-intl.dev/docs/usage/translations#arrays-of-messages)를 참고하세요.

## React 요소 포맷팅[](https://next-intl.dev/docs/usage/lists#react-elements)

문자열 값뿐만 아니라, 포맷팅 함수에 React 요소 배열도 전달할 수 있습니다:
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

**결과:**
```
    <p>
      <a href="/user/1">Alice</a>, <a href="/user/2">Bob</a>, and
      <a href="/user/3">Charlie</a>
    </p>
```

이 경우 `format.list`는 `Iterable<ReactElement>`를 반환합니다.


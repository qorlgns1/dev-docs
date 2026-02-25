---
title: '번역 렌더링'
description: '원본 URL: https://next-intl.dev/docs/usage/translations'
---

원본 URL: https://next-intl.dev/docs/usage/translations

# 번역 렌더링

영상으로 보는 편이 좋으신가요?

[첫 번역](https://learn.next-intl.dev/chapters/03-translations/01-setup)

## 용어[](https://next-intl.dev/docs/usage/translations#terminology)

  * **Locale** : 사용자 언어와 서식 기본 설정을 담고 있는 식별자를 설명할 때 사용하는 용어입니다. 언어 외에도 locale에는 선택적인 지역 정보(예: `en-US`)가 포함될 수 있습니다.
  * **Messages** : locale별로 그룹화된 key/번역 쌍의 모음입니다(예: `en-US.json`).

## 메시지 구조화[](https://next-intl.dev/docs/usage/translations#structuring-messages)

메시지는 일반적으로 JSON 파일에 정의합니다:

en.json
```
    {
      "About": {
        "title": "About us"
      }
    }
```

React 컴포넌트 내부에서는 `useTranslations` 훅으로 메시지를 렌더링할 수 있습니다:

About.tsx
```
    import {useTranslations} from 'next-intl';

    function About() {
      const t = useTranslations('About');
      return <h1>{t('title')}</h1>;
    }
```

컴포넌트에서 사용 가능한 모든 메시지를 가져오려면 namespace 경로를 생략하면 됩니다:
```
    const t = useTranslations();

    t('About.title');
```

**더 알아보기:**

[키 구성](https://learn.next-intl.dev/chapters/03-translations/03-keys)

[메시지 재사용](https://learn.next-intl.dev/chapters/03-translations/04-message-reuse)

[에디터 도구](https://learn.next-intl.dev/chapters/03-translations/05-tooling)

💡

번역가는 [Crowdin](https://crowdin.com/teams/engineering) 같은 로컬라이제이션 관리 솔루션을 사용해 메시지를 협업할 수 있습니다.

[](https://next-intl.dev/docs/usage/translations#messages-nested-structure)메시지에 더 많은 구조를 적용하려면 어떻게 하나요?

원한다면 메시지를 중첩 객체로 구조화할 수 있습니다.

en.json
```
    {
      "auth": {
        "SignUp": {
          "title": "Sign up",
          "form": {
            "placeholder": "Please enter your name",
            "submit": "Submit"
          }
        }
      }
    }
```

SignUp.tsx
```
    import {useTranslations} from 'next-intl';

    function SignUp() {
      // Provide the lowest common denominator that contains
      // all messages this component needs to consume.
      const t = useTranslations('auth.SignUp');

      return (
        <>
          <h1>{t('title')}</h1>
          <form>
            <input
              // The remaining hierarchy can be resolved by
              // using `.` to access nested messages.
              placeholder={t('form.placeholder')}
            />
            <button type="submit">{t('form.submit')}</button>
          </form>
        </>
      );
    }
```

[](https://next-intl.dev/docs/usage/translations#messages-outside-components)컴포넌트 밖에서 번역을 사용하려면 어떻게 하나요?

`next-intl`은 React 컴포넌트 내부에서 번역을 소비하도록 설계된 `useTranslations` API를 중심으로 구성되어 있습니다. 이것이 제약처럼 보일 수 있지만, 의도된 설계이며 놓치기 쉬운 잠재적 문제를 피하는 검증된 패턴 사용을 장려하기 위한 것입니다.

다만 예외가 하나 있습니다: [Using `next-intl` with Server Actions, Metadata and Route Handlers](https://next-intl.dev/docs/environments/actions-metadata-route-handlers).

이 주제를 더 깊이 보고 싶다면, 이 설계 결정의 배경을 다루는 블로그 글을 참고하세요: [How (not) to use translations outside of React components](https://next-intl.dev/blog/translations-outside-of-react-components).

[](https://next-intl.dev/docs/usage/translations#messages-other-styles)메시지 구조를 다른 스타일로 사용할 수 있나요?

중첩을 표현하는 데 사용되므로 namespace key에는 ”.” 문자를 포함할 수 없습니다. 다른 문자는 모두 사용할 수 있습니다.

메시지 key에 ”.”를 사용하는 평면 구조에서 마이그레이션하는 경우, 다음과 같이 메시지를 중첩 구조로 변환할 수 있습니다:
```
    import {set} from 'lodash';

    const input = {
      'one.one': '1.1',
      'one.two': '1.2',
      'two.one.one': '2.1.1'
    };

    const output = Object.entries(input).reduce(
      (acc, [key, value]) => set(acc, key, value),
      {}
    );
```

**출력:**
```
    {
      "one": {
        "one": "1.1",
        "two": "1.2"
      },
      "two": {
        "one": {
          "one": "2.1.1"
        }
      }
    }
```

이렇게 하면 반복되는 상위 key의 중복을 제거하면서 계층 구조를 유지할 수 있습니다. 일회성 스크립트에서 실행하거나, 메시지를 `next-intl`에 전달하기 전에 실행하면 됩니다.

이전에 사람이 읽기 쉬운 문장을 key로 사용했다면, 이론적으로 메시지를 `next-intl`에 전달하기 전에 `.` 문자를 다른 문자(예: `_`)로 매핑할 수 있습니다. 하지만 일반적으로는 key로 ID를 사용하는 것이 권장됩니다. 사람이 읽기 쉬운 key를 사용하려는 주된 이유가 에디터 가독성이라면, [VSCode integration](https://next-intl.dev/docs/workflows/vscode-integration)을 통해 에디터에서 사람이 읽기 쉬운 라벨을 계속 볼 수 있습니다.

## ICU 메시지[](https://next-intl.dev/docs/usage/translations#icu-messages)

`next-intl`은 [ICU message syntax](https://unicode-org.github.io/icu/userguide/format_parse/messages/)를 사용하며, 이를 통해 언어별 뉘앙스를 표현하고 메시지 내부의 상태 처리를 앱 코드와 분리할 수 있습니다.

[ICU 메시지](https://learn.next-intl.dev/chapters/03-translations/06-icu-messages)

### 정적 메시지[](https://next-intl.dev/docs/usage/translations#static-messages)

정적 메시지는 있는 그대로 사용됩니다:

en.json
```
    "message": "Hello world!"
```
```
    t('message'); // "Hello world!"
```

### 인자 보간[](https://next-intl.dev/docs/usage/translations#arguments)

동적 값은 중괄호를 사용해 메시지에 삽입할 수 있습니다:

en.json
```
    "message": "Hello {name}!"
```
```
    t('message', {name: 'Jane'}); // "Hello Jane!"
```

[](https://next-intl.dev/docs/usage/translations#interpolation-supported-characters)값 이름에는 어떤 문자를 사용할 수 있나요?

값 이름은 영숫자여야 하며 밑줄을 포함할 수 있습니다. 대시를 포함한 다른 문자는 지원되지 않습니다.

### 기수 복수화[](https://next-intl.dev/docs/usage/translations#cardinal-pluralization)

주어진 아이템 개수의 복수형을 표현하려면 `plural` 인자를 사용할 수 있습니다:

en.json
```
    "message": "You have {count, plural, =0 {no followers yet} =1 {one follower} other {# followers}}."
```
```
    t('message', {count: 3580}); // "You have 3,580 followers."
```

`#` 마커를 사용하면 값이 [숫자 형식으로 포맷](https://next-intl.dev/docs/usage/numbers)된다는 점에 유의하세요.

[](https://next-intl.dev/docs/usage/translations#cardinal-plural-forms)어떤 복수형이 지원되나요?

언어마다 복수형 규칙이 다르며, 메시지도 이러한 규칙을 반영해야 합니다.

예를 들어 영어에는 두 가지 형태가 있습니다. 단수용(예: “1 _follower_ ”)과 그 외 모든 경우용(예: “0 _followers_ ”, “2 _followers_ ”)입니다. 반면 중국어는 한 가지 형태만 있고, 아랍어는 여섯 가지 형태가 있습니다.

또 다른 고려 사항은 사용성 측면입니다. 일반적으로 추가 케이스를 고려하면 도움이 되며, 가장 흔한 예는 0에 대한 특수 케이스입니다(예: “0 followers” 대신 “No followers yet”).

특정 숫자에 매칭하기 위해 언제나 `=value` 문법(예: `=0`)을 사용할 수 있지만, 언어의 문법 규칙에 따라 다음 태그를 사용할 수 있습니다:

  * `zero`: 0개 항목 문법이 있는 언어용(예: 라트비아어, 웨일스어).
  * `one`: 단수 항목 문법이 있는 언어용(예: 영어, 독일어).
  * `two`: 2개 항목 문법이 있는 언어용(예: 아랍어, 웨일스어).
  * `few`: 소수 항목에 대한 별도 문법이 있는 언어용(예: 아랍어, 크로아티아어).
  * `many`: 다수 항목에 대한 별도 문법이 있는 언어용(예: 아랍어, 크로아티아어).
  * `other`: 값이 다른 복수 카테고리에 매칭되지 않을 때 사용.

`next-intl`은 [`Intl.PluralRules`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules)를 사용해 주어진 숫자에 맞는 태그를 판별합니다. `few`와 `many`가 적용되는 정확한 범위는 locale에 따라 달라집니다(Unicode CLDR의 [language plural rules](https://www.unicode.org/cldr/charts/43/supplemental/language_plural_rules.html) 표 참고).

### 서수 복수화[](https://next-intl.dev/docs/usage/translations#ordinal-pluralization)

항목의 순서에 기반해 복수형을 적용하려면 `selectordinal` 인자를 사용할 수 있습니다:

en.json
```
    "message": "It's your {year, selectordinal, one {#st} two {#nd} few {#rd} other {#th}} birthday!"
```

[](https://next-intl.dev/docs/usage/translations#ordinal-plural-forms)어떤 복수형이 지원되나요?

언어에 따라 서로 다른 서수 복수형이 지원됩니다.

예를 들어 영어에는 네 가지 형태가 있습니다: “th”, “st”, “nd”, “rd”(예: 1st, 2nd, 3rd, 4th … 11th, 12th, 13th … 21st, 22nd, 23rd, 24th 등). 반면 중국어와 아랍어는 모두 서수에 한 가지 형태만 사용합니다.

`next-intl`은 [`Intl.PluralRules`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules)를 사용해 주어진 숫자에 맞는 _tag_ 를 판별합니다.

**지원되는 태그는 다음과 같습니다:**

  * `zero`: 0개 항목 문법이 있는 언어용(예: 라트비아어, 웨일스어).
  * `one`: 단수 항목 문법이 있는 언어용(예: 영어, 독일어).
  * `two`: 2개 항목 문법이 있는 언어용(예: 아랍어, 웨일스어).
  * `few`: 소수 항목에 대한 별도 문법이 있는 언어용(예: 아랍어, 폴란드어, 크로아티아어).
  * `many`: 다수 항목에 대한 별도 문법이 있는 언어용(예: 아랍어, 폴란드어, 크로아티아어).
  * `other`: 값이 다른 복수 카테고리에 매칭되지 않을 때 사용.

`few`와 `many`가 적용되는 정확한 범위는 locale에 따라 달라집니다(Unicode CLDR의 [language plural rules](https://www.unicode.org/cldr/charts/43/supplemental/language_plural_rules.html) 표 참고).

특정 숫자에 매칭하기 위해 `next-intl`은 특별한 `=value` 문법(예: `=3`)도 추가로 지원하며, 이 문법이 항상 우선 적용됩니다.

### enum 기반 값 선택[](https://next-intl.dev/docs/usage/translations#selecting-enum-based-values)

식별자를 사람이 읽기 쉬운 라벨로 매핑하려면 JavaScript의 `switch` 문과 유사하게 동작하는 `select` 인자를 사용할 수 있습니다:

en.json
```
    "message": "{gender, select, female {She is} male {He is} other {They are}} online."
```
```
    t('message', {gender: 'female'}); // "She is online."
```

**참고** : `other` 케이스는 필수이며, 특정 값과 일치하는 항목이 없을 때 사용됩니다.

[](https://next-intl.dev/docs/usage/translations#select-values-supported-characters)select 값에는 어떤 문자를 사용할 수 있나요?

값은 영숫자여야 하며 밑줄을 포함할 수 있습니다. 대시를 포함한 다른 문자는 지원되지 않습니다.

따라서 예를 들어 locale을 사람이 읽기 쉬운 문자열에 매핑할 때는 먼저 대시를 밑줄로 매핑해야 합니다:

en.json
```
    "label": "{locale, select, en_GB {British English} en_US {American English} other {Unknown}}"
```
```
    const locale = 'en-GB';
    t('message', {locale: locale.replaceAll('-', '_')});
```

### 이스케이프[](https://next-intl.dev/docs/usage/translations#escaping)

중괄호는 [인자 보간](https://next-intl.dev/docs/usage/translations#arguments)에 사용되므로, 메시지에서 실제 기호로 사용하려면 작은따옴표(`'`)로 감쌀 수 있습니다:

en.json
```
    "message": "Escape curly braces with single quotes (e.g. '{name}')"
```
```
    t('message'); // "Escape curly braces with single quotes (e.g. {name})"
```

## 리치 텍스트[](https://next-intl.dev/docs/usage/translations#rich-text)

커스텀 태그를 사용해 리치 텍스트를 포맷하고, `t.rich`를 통해 이를 React 컴포넌트에 매핑할 수 있습니다:

en.json
```
    {
      "message": "Please refer to <guidelines>the guidelines</guidelines>."
    }
```
```
    // Returns `<>Please refer to <a href="/guidelines">the guidelines</a>.</>`
    t.rich('message', {
      guidelines: (chunks) => <a href="/guidelines">{chunks}</a>
    });
```

태그는 임의로 중첩할 수 있습니다(예: `This is <important><very>very</very> important</important>`).

[](https://next-intl.dev/docs/usage/translations#rich-text-reuse-tags)앱 전반에서 태그를 재사용하려면 어떻게 하나요?

앱 전반에서 공유하려는 리치 텍스트용 공통 태그는 공유 모듈에 정의하고, `t.rich` 사용이 필요한 곳에서 import할 수 있습니다.

편리한 패턴은 render prop을 통해 공통 태그를 제공하는 컴포넌트를 사용하는 것입니다:
```
    import {useTranslations} from 'next-intl';
    import RichText from '@/components/RichText';

    function AboutPage() {
      const t = useTranslations('AboutPage');
      return <RichText>{(tags) => t.rich('description', tags)}</RichText>;
    }
```

이 경우 `RichText` 컴포넌트는 스타일이 적용된 태그와 텍스트의 일반 레이아웃을 함께 제공할 수 있습니다:

components/RichText.tsx
```
    import {ReactNode} from 'react';

    // These tags are available
    type Tag = 'p' | 'b' | 'i';

    type Props = {
      children(tags: Record<Tag, (chunks: ReactNode) => ReactNode>): ReactNode
    };

    export default function RichText({children}: Props) {
      return (
          {children({
            p: (chunks: ReactNode) => <p>{chunks}</p>,
            b: (chunks: ReactNode) => <b className="font-semibold">{chunks}</b>,
            i: (chunks: ReactNode) => <i className="italic">{chunks}</i>
          })}
      );
    }
```

공유 태그와 컴포넌트의 값을 함께 조합해야 한다면 spread operator를 사용해 적절히 병합할 수 있습니다:
```
    function UserPage({username}) {
      const t = useTranslations('UserPage');
      return (
      );
    }
```

[](https://next-intl.dev/docs/usage/translations#rich-text-self-closing)chunks 없이 “self-closing” 태그를 사용하려면 어떻게 하나요?

메시지에서는 자식으로 chunks가 없는 태그를 사용할 수 있지만, 문법상 ICU parser에는 닫는 태그가 필요합니다:

en.json
```
    {
      "message": "Hello,<br></br>how are you?"
    }
```
```
    t.rich('message', {
      br: () => <br />
    });
```

[](https://next-intl.dev/docs/usage/translations#rich-text-attributes)태그에 attributes를 전달하려면 어떻게 하나요?

attributes는 메시지 내부가 아니라 호출 위치(call site)에서만 설정할 수 있습니다:

en.json
```
    {
      "message": "Go to <profile>my profile</profile>"
    }
```
```
    t.rich('message', {
      profile: (chunks) => <Link href="/profile">{chunks}</Link>
    });
```

메시지의 일부로 attributes 값을 반드시 구성해야 하는 경우, 별도 메시지에서 값을 가져와 다른 메시지에 attribute로 전달할 수 있습니다:

en.json
```
    {
      "message": "See this <partner>partner website</partner>.",
      "partnerHref": "https://partner.example.com"
    }
```
```
    t.rich('message', {
      partner: (chunks) => <a href={t('partnerHref')}>{chunks}</a>
    });
```

경로명을 현지화하는 용도라면 [`pathnames`](https://next-intl.dev/docs/routing/configuration#pathnames) 사용을 고려하세요.

## HTML 마크업[](https://next-intl.dev/docs/usage/translations#html-markup)

리치 텍스트를 렌더링할 때는 보통 [리치 텍스트 포맷팅](https://next-intl.dev/docs/usage/translations#rich-text)을 사용하는 것이 좋습니다. 다만 raw HTML markup을 출력해야 하는 사용 사례가 있다면 `t.markup` 함수를 사용할 수 있습니다:

en.json
```
    {
      "markup": "This is <important>important</important>"
    }
```
```
    // Returns 'This is <b>important</b>'
    t.markup('markup', {
      important: (chunks) => `<b>${chunks}</b>`
    });
```

`t.rich`와 달리, 제공하는 markup 함수는 `chunks`를 `string`으로 받고, 감싼 결과를 역시 `string`으로 반환합니다.

## 원시 메시지[](https://next-intl.dev/docs/usage/translations#raw-messages)

메시지는 항상 파싱되므로, 예를 들어 리치 텍스트 서식을 위해서는 필요한 태그를 제공해야 합니다. 메시지에 원시 HTML이 저장되어 있는 경우처럼 파싱을 피하고 싶다면, 이 사용 사례를 위한 별도의 API가 있습니다:

en.json
```
    {
      "content": "<h1>Headline</h1><p>This is raw HTML</p>"
    }
```
```
```

⚠️

**중요** : 교차 사이트 스크립팅 공격을 방지하려면 [`dangerouslySetInnerHTML`](https://react.dev/reference/react-dom/components/common#dangerously-setting-the-inner-html)에 전달하는 콘텐츠를 항상 sanitize해야 합니다.

원시 메시지의 값은 유효한 모든 JSON 값이 될 수 있습니다: 문자열, 불리언, 객체, 배열.

## 선택적 메시지[](https://next-intl.dev/docs/usage/translations#t-has)

특정 로캘에서만 제공되는 메시지가 있다면, 현재 로캘에서 메시지를 사용할 수 있는지 확인하기 위해 `t.has` 함수를 사용할 수 있습니다:
```
    const t = useTranslations('About');

    t.has('title'); // true
    t.has('unknown'); // false
```

이와는 별개로, 특정 로캘의 메시지가 불완전한 경우 기본 로캘 등의 [대체 메시지](https://next-intl.dev/docs/usage/configuration#messages)를 제공할 수도 있습니다.

## 메시지 배열[](https://next-intl.dev/docs/usage/translations#arrays-of-messages)

메시지 목록을 렌더링해야 한다면, 권장되는 방식은 React 컴포넌트 내에서 메시지 키를 배열에 매핑하는 것입니다:

en.json
```
    {
      "CompanyStats": {
        "yearsOfService": {
          "title": "Years of service",
          "value": "34"
        },
        "happyClients": {
          "title": "Happy clients",
          "value": "1.000+"
        },
        "partners": {
          "title": "Products",
          "value": "5.000+"
        }
      }
    }
```

CompanyStats.tsx
```
    import {useTranslations} from 'next-intl';

    function CompanyStats() {
      const t = useTranslations('CompanyStats');
      const items = [
        {
          title: t('yearsOfService.title'),
          value: t('yearsOfService.value')
        },
        {
          title: t('happyClients.title'),
          value: t('happyClients.value')
        },
        {
          title: t('partners.title'),
          value: t('partners.value')
        }
      ];

      return (
        <ul>
          {items.map((item, index) => (
            <li key={index}>
              <h2>{item.title}</h2>
              <p>{item.value}</p>
            </li>
          ))}
        </ul>
      );
    }
```

이 접근 방식은 ICU 기능을 사용할 수 있게 하면서, 메시지의 정적 [검증](https://next-intl.dev/docs/workflows/messages)도 가능하게 해줍니다.

[](https://next-intl.dev/docs/usage/translations#arrays-varying-amount)로캘에 따라 항목 수가 달라지면 어떻게 하나요?

네임스페이스의 모든 키를 동적으로 순회하려면 [`useMessages`](https://next-intl.dev/docs/usage/configuration#messages) 훅을 사용해 특정 네임스페이스의 모든 메시지를 가져오고, 거기서 키를 추출할 수 있습니다:

CompanyStats.tsx
```
    import {useTranslations, useMessages} from 'next-intl';

    function CompanyStats() {
      const t = useTranslations('CompanyStats');

      const messages = useMessages();
      const keys = Object.keys(messages.CompanyStats);

      return (
        <ul>
          {keys.map((key) => (
            <li key={key}>
              <h2>{t(`${key}.title`)}</h2>
              <p>{t(`${key}.value`)}</p>
            </li>
          ))}
        </ul>
      );
    }
```

## 오른쪽에서 왼쪽으로 쓰는 언어[](https://next-intl.dev/docs/usage/translations#right-to-left-languages)

아랍어, 히브리어, 페르시아어 같은 언어는 [오른쪽에서 왼쪽으로 쓰는 문자 체계](https://en.wikipedia.org/wiki/Right-to-left_script)(보통 RTL로 약칭)를 사용합니다. 이러한 언어에서는 페이지의 오른쪽에서 쓰기를 시작해 왼쪽으로 이어집니다.

**예시:**
```
    النص في اللغة العربية _مثلا_ يُقرأ من اليمين لليسار
```

번역된 메시지를 제공하는 것 외에도, 올바른 RTL 현지화를 위해서는 다음이 필요합니다:

  1. 필요한 위치에 [`dir` attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/dir) 제공
  2. 예: [CSS logical properties](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_logical_properties_and_values)를 사용한 레이아웃 미러링
  3. 예: 아이콘 커스터마이징을 통한 요소 미러링

**더 알아보기:**

[Right-to-left layouts](https://learn.next-intl.dev/chapters/09-design-localization/02-right-to-left)


---
title: "css.include"
description: "CSS를 처리할지 여부를 설정합니다. 제외되면 CSS 파일은 이후 처리를 우회하기 위해 빈 문자열로 대체됩니다. CSS Modules는 런타임에 영향을 주지 않도록 프록시를 반환합니다."
---

출처 URL: https://vitest.dev/config/css

# css

- **타입**: `boolean | { include?, exclude?, modules? }`

CSS를 처리할지 여부를 설정합니다. 제외되면 CSS 파일은 이후 처리를 우회하기 위해 빈 문자열로 대체됩니다. CSS Modules는 런타임에 영향을 주지 않도록 프록시를 반환합니다.

::: warning
이 옵션은 [browser tests](https://vitest.dev/guide/browser/)에는 적용되지 않습니다.
:::

## css.include

- **타입**: `RegExp | RegExp[]`
- **기본값**: `[]`

실제 CSS를 반환하며 Vite 파이프라인에서 처리되어야 하는 파일을 위한 RegExp 패턴입니다.

:::tip
모든 CSS 파일을 처리하려면 `/.+/`를 사용하세요.
:::

## css.exclude

- **타입**: `RegExp | RegExp[]`
- **기본값**: `[]`

빈 CSS 파일을 반환할 파일을 위한 RegExp 패턴입니다.

## css.modules

- **타입**: `{ classNameStrategy? }`
- **기본값**: `{}`

### css.modules.classNameStrategy

- **타입**: `'stable' | 'scoped' | 'non-scoped'`
- **기본값**: `'stable'`

CSS 파일을 처리하기로 했다면, CSS modules 내부의 클래스 이름을 스코프 처리할지 설정할 수 있습니다. 다음 옵션 중 하나를 선택할 수 있습니다.

- `stable`: 클래스 이름은 `_${name}_${hashedFilename}` 형식으로 생성됩니다. 즉 CSS 내용이 변경되어도 생성된 클래스는 동일하게 유지되지만, 파일 이름이 변경되거나 파일이 다른 폴더로 이동하면 변경됩니다. 이 설정은 snapshot 기능을 사용할 때 유용합니다.
- `scoped`: 클래스 이름은 일반적인 방식으로 생성되며, `css.modules.generateScopedName` 메서드가 있고 CSS 처리가 활성화되어 있다면 이를 따릅니다. 기본적으로 파일 이름은 `_${name}_${hash}` 형식으로 생성되며, hash에는 파일 이름과 파일 내용이 포함됩니다.
- `non-scoped`: 클래스 이름이 해시되지 않습니다.

::: warning
기본적으로 Vitest는 프록시를 내보내며 CSS Modules 처리를 우회합니다. 클래스의 CSS 속성에 의존한다면 `include` 옵션을 사용해 CSS 처리를 활성화해야 합니다.
:::

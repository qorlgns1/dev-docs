---
title: 'CSS 태그 없음'
description: '> 수동 스타일시트 태그 추가를 방지하세요.'
---

# CSS 태그 없음 | Next.js

Source URL: https://nextjs.org/docs/messages/no-css-tags

[Docs](https://nextjs.org/docs)[Errors](https://nextjs.org/docs)No CSS Tags

# CSS 태그 없음

> 수동 스타일시트 태그 추가를 방지하세요.

## 왜 이 오류가 발생했나요[](https://nextjs.org/docs/messages/no-css-tags#why-this-error-occurred)

외부 스타일시트를 연결하기 위해 `link` 요소를 사용했습니다. 이는 웹페이지의 CSS 리소스 로딩에 부정적인 영향을 줄 수 있습니다.

## 해결 방법[](https://nextjs.org/docs/messages/no-css-tags#possible-ways-to-fix-it)

Next.js의 기본 제공 CSS 지원을 활용해 스타일을 포함하는 여러 방법이 있습니다. 예를 들어 `pages/_app.js`에서 가져오는 루트 스타일시트 안에 `@import`를 사용할 수 있습니다:

styles.css
```
    /* Root stylesheet */
    @import 'extra.css';

    body {
      /* ... */
    }
```

또 다른 방법은 CSS 모듈을 사용해 특정 컴포넌트에만 범위가 지정된 CSS 파일을 가져오는 것입니다.

pages/index.js
```
    import styles from './extra.module.css'

    export class Home {
      render() {
        return (
          <div>
            <button type="button" className={styles.active}>
              Open
            </button>
          </div>
        )
      }
    }
```

애플리케이션에 CSS를 포함하는 모든 방법을 알아보려면 [Built-In CSS Support](https://nextjs.org/docs/app/getting-started/css) 문서를 참고하세요.

보내기
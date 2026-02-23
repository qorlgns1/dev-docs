---
title: 'url은 더 이상 사용되지 않습니다'
description: '이 기능이 사라지는 이유는 모든 것을 매우 예측 가능하고 명시적으로 만들고자 하기 때문입니다. 어디선가 갑자기 나타나는 마법 같은 url 속성은 이러한 목표에 도움이 되지 않습니다.'
---

# `url`은 더 이상 사용되지 않습니다 | Next.js

Source URL: https://nextjs.org/docs/messages/url-deprecated

[문서](https://nextjs.org/docs)[오류](https://nextjs.org/docs)`url` is deprecated

# `url`은 더 이상 사용되지 않습니다

## 이 오류가 발생한 이유[](https://nextjs.org/docs/messages/url-deprecated#why-this-error-occurred)

6.x 이전 버전에서는 `url` 속성이 모든 `Page` 컴포넌트( `pages` 디렉터리 안의 모든 페이지)에 마법처럼 주입되었습니다.

이 기능이 사라지는 이유는 모든 것을 매우 예측 가능하고 명시적으로 만들고자 하기 때문입니다. 어디선가 갑자기 나타나는 마법 같은 url 속성은 이러한 목표에 도움이 되지 않습니다.

> **참고**: ⚠️ 일부 경우에는 코드 어디에서도 `url`을 참조하지 않아도 React Dev Tools를 사용하면 이 경고가 발생할 수 있습니다. 확장을 일시적으로 비활성화하고 경고가 지속되는지 확인하세요.

## 가능한 해결 방법[](https://nextjs.org/docs/messages/url-deprecated#possible-ways-to-fix-it)

Next 5부터는 Next.js 라우터 객체를 페이지와 그 하위 컴포넌트에 명시적으로 주입하는 방법을 제공합니다. 주입되는 `router` 속성은 `pathname`, `asPath`, `query`처럼 `url`과 동일한 값을 가집니다.

다음은 `withRouter`를 사용하는 예시입니다:

pages/index.js
````code
    import { withRouter } from 'next/router'

    class Page extends React.Component {
      render() {
        const { router } = this.props
        console.log(router)
        return <div>{router.pathname}</div>
      }
    }

    export default withRouter(Page)
````

`url` 속성 사용을 `withRouter`로 자동 변환하는 codemod(코드 간 변환)를 제공합니다.

이 codemod와 실행 방법은 여기에서 확인할 수 있습니다: [Use `withRouter`](https://nextjs.org/docs/pages/guides/upgrading/codemods#url-to-withrouter)

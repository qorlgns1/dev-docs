---
title: 'LinkedErrors | Next.js용 Sentry'
description: '원본 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/linkederrors'
---

원본 URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/linkederrors

# LinkedErrors | Next.js용 Sentry

*가져오기 이름: `Sentry.linkedErrorsIntegration`*

이 통합은 기본적으로 활성화되어 있습니다. 기본 통합 구성을 수정하려면 [여기](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations.md#modifying-default-integrations)를 참고하세요.

이 통합을 사용하면 연결된 에러를 구성할 수 있습니다. 지정된 한도까지 재귀적으로 읽은 뒤, 특정 키를 기준으로 조회를 수행합니다. 기본적으로 Sentry SDK는 한도를 5로 설정하고, 사용하는 키는 `"cause"`입니다.

```JavaScript
Sentry.init({
  integrations: [Sentry.linkedErrorsIntegration()],
});
```

## [옵션](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/linkederrors.md#options)

- [`key`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/linkederrors.md#key)

*타입: `string`*

- [`limit`](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/linkederrors.md#limit)

*타입: `number`*

## [예시](https://docs.sentry.io/platforms/javascript/guides/nextjs/configuration/integrations/linkederrors.md#example)

다음은 이를 구현하는 방법에 대한 코드 예시입니다.

```javascript
document
  .querySelector("#get-reviews-btn")
  .addEventListener("click", async (event) => {
    const movie = event.target.dataset.title;
    try {
      const reviews = await fetchMovieReviews(movie);
      renderMovieReviews(reviews);
    } catch (e) {
      const fetchError = new Error(
        `Failed to fetch reviews for: ${movie}`,
      );
      fetchError.cause = e;
      Sentry.captureException(fetchError);
      renderMovieReviewsError(fetchError);
    }
  });
```


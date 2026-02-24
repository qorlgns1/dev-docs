---
title: 'Typescript 정의'
description: '원본 URL: https://docs.bullmq.io/bull/install'
---

원본 URL: https://docs.bullmq.io/bull/install

# 설치

**Npm**으로 설치:

```bash
npm install bull --save
```

또는 Yarn:

```bash
yarn add bull
```

Bull을 사용하려면 Redis 서버도 실행 중이어야 합니다. 로컬 개발 환경에서는 [docker](https://hub.docker.com/_/redis/)를 사용해 쉽게 설치할 수 있습니다.

Bull은 기본적으로 `localhost:6379`에서 실행 중인 Redis 서버에 연결을 시도합니다.

{% hint style="info" %}
*Bull은 `2.8.18` 이상 버전의 Redis가 필요합니다.*
{% endhint %}

### Typescript 정의

```bash
npm install @types/bull --save-dev
```

```bash
yarn add --dev @types/bull
```

정의는 현재 [DefinitelyTyped](https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/bull) repo에서 유지 관리되고 있습니다.


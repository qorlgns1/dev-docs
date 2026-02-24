---
title: 'Docker 사용'
description: 'BullMQ Pro를 설치하려면 taskforce.sh에서 발급한 NPM 토큰을 사용해야 합니다.'
---

Source URL: https://docs.bullmq.io/bullmq-pro/install

# 설치

BullMQ Pro를 설치하려면 [taskforce.sh](https://taskforce.sh)에서 발급한 NPM 토큰을 사용해야 합니다.

토큰을 준비했다면, 앱 리포지토리에서 `.npmrc` 파일을 업데이트하거나 새로 만들고 아래 내용을 추가하세요:

```
@taskforcesh:registry=https://npm.taskforce.sh/
//npm.taskforce.sh/:_authToken=${NPM_TASKFORCESH_TOKEN}
always-auth=true
```

여기서 `NPM_TASKFORCESH_TOKEN`은 해당 토큰을 가리키는 환경 변수입니다.

그다음 `npm`, `yarn`, 또는 `pnpm`으로 다른 패키지를 설치하듯 `@taskforcesh/bullmq-pro` 패키지를 설치하면 됩니다:

```
yarn add @taskforcesh/bullmq-pro
```

BullMQ Pro를 사용하려면 클래스의 *Pro* 버전을 import하면 됩니다. 이 클래스들은 오픈 소스 BullMQ 라이브러리의 서브클래스로, 새로운 기능이 추가되어 있습니다:

```typescript
import { QueuePro, WorkerPro } from '@taskforcesh/bullmq-pro';

const queue = new QueuePro('myQueue');

const worker = new WorkerPro('myQueue', async job => {
  // Process job
});
```

### Docker 사용

docker를 사용한다면, 위의 `.npmrc` 파일도 `Dockerfile`에 추가해야 합니다:

```docker
WORKDIR /app

ADD .npmrc /app/.npmrc
```


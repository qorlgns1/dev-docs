---
title: 'Jaeger 실행하기'
description: 'Jaeger를 실행하는 가장 쉬운 방법은 Docker compose를 사용하는 것입니다. docker가 설치되어 있다면, 이  파일을 실행하면 됩니다:'
---

Source URL: https://docs.bullmq.io/guide/telemetry/running-jaeger

# Jaeger 실행하기

Jaeger를 실행하는 가장 쉬운 방법은 Docker compose를 사용하는 것입니다. docker가 설치되어 있다면, 이 `docker-compose.yaml` 파일을 실행하면 됩니다:

```yaml
services:
  jaeger:
    image: jaegertracing/all-in-one:latest
    container_name: BullMQ_with_opentelemetry_jaeger
    ports:
      - '4318:4318'
      - '16686:16686'

```

여기서는 2개의 포트를 노출해야 한다는 점에 유의하세요. 첫 번째 포트(4318)는 트레이스를 export하기 위한 endpoint이고, 두 번째 포트(16686)는 UI입니다.

이제 다음으로 이 서비스를 실행하면 됩니다:

```
docker-compose up
```

몇 초 후 이미지가 실행 상태가 됩니다. 브라우저 창을 열고 [http://localhost:16686](http://localhost:16686/search) 로 접속해 정상 동작 여부를 확인할 수 있습니다.

아직 생성된 트레이스가 없으므로, 대시보드는 꽤 비어 있는 상태로 표시됩니다:

<figure><img src="https://1340146492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LUuDmt_xXMfG66Rn1GA%2Fuploads%2Fgit-blob-b6d84aedee561e5f859913f40391c6938c23cfab%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>


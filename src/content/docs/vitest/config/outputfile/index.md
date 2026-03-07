---
title: "outputFile {#outputfile}"
description: ", , 또는  옵션이 함께 지정된 경우 테스트 결과를 파일에 기록합니다."
---

출처 URL: https://vitest.dev/config/outputfile

# outputFile {#outputfile}

- **타입:** `string | Record<string, string>`
- **CLI:** `--outputFile=<path>`, `--outputFile.json=./path`

`--reporter=json`, `--reporter=html`, 또는 `--reporter=junit` 옵션이 함께 지정된 경우 테스트 결과를 파일에 기록합니다.
문자열 대신 객체를 제공하면 여러 리포터를 사용할 때 각 리포터별 출력 파일을 개별적으로 정의할 수 있습니다.

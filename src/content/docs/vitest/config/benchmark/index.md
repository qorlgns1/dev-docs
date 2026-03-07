---
title: "benchmark {#benchmark}"
description: "벤치마크 테스트 파일에 포함할 glob 패턴입니다."
---

출처 URL: https://vitest.dev/config/benchmark

# benchmark {#benchmark}

- **Type:** `{ include?, exclude?, ... }`

`vitest bench` 실행 시 사용되는 옵션입니다.

## benchmark.include

- **Type:** `string[]`
- **Default:** `['**/*.{bench,benchmark}.?(c|m)[jt]s?(x)']`

벤치마크 테스트 파일에 포함할 glob 패턴입니다.

## benchmark.exclude

- **Type:** `string[]`
- **Default:** `['node_modules', 'dist', '.idea', '.git', '.cache']`

벤치마크 테스트 파일에서 제외할 glob 패턴입니다.

## benchmark.includeSource

- **Type:** `string[]`
- **Default:** `[]`

소스 내 벤치마크 테스트 파일에 포함할 glob 패턴입니다. 이 옵션은 [`includeSource`](#includesource)와 유사합니다.

정의되면 Vitest는 `import.meta.vitest`가 포함된 일치 파일을 모두 실행합니다.

## benchmark.reporters

- **Type:** `Arrayable<BenchmarkBuiltinReporters | Reporter>`
- **Default:** `'default'`

출력을 위한 사용자 정의 reporter입니다. 하나 이상의 내장 report 이름, reporter 인스턴스, 그리고/또는 사용자 정의 reporter 경로를 포함할 수 있습니다.

## benchmark.outputFile

`benchmark.outputJson` 사용이 권장되므로 deprecated 되었습니다.

## benchmark.outputJson {#benchmark-outputJson}

- **Type:** `string | undefined`
- **Default:** `undefined`

벤치마크 결과를 저장할 파일 경로입니다. 나중에 `--compare` 옵션에 사용할 수 있습니다.

예시:

```sh
# save main branch's result
git checkout main
vitest bench --outputJson main.json

# change a branch and compare against main
git checkout feature
vitest bench --compare main.json
```

## benchmark.compare {#benchmark-compare}

- **Type:** `string | undefined`
- **Default:** `undefined`

현재 실행 결과와 비교할 이전 벤치마크 결과 파일의 경로입니다.

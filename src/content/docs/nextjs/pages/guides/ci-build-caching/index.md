---
title: '가이드: CI Build Caching'
description: '마지막 업데이트 2026년 2월 20일'
---

# 가이드: CI Build Caching | Next.js

출처 URL: https://nextjs.org/docs/pages/guides/ci-build-caching

[Pages Router](https://nextjs.org/docs/pages)[Guides](https://nextjs.org/docs/pages/guides)CI Build Caching

페이지 복사

# CI 빌드 캐싱 구성 방법

마지막 업데이트 2026년 2월 20일

빌드 성능을 개선하기 위해 Next.js는 빌드 간에 공유되는 캐시를 `.next/cache`에 저장합니다.

이 캐시를 CI(Continuous Integration) 환경에서 활용하려면, CI 워크플로가 빌드 사이에서 캐시를 올바르게 유지하도록 구성해야 합니다.

> CI가 빌드 사이에서 `.next/cache`를 보존하도록 설정되어 있지 않으면 [No Cache Detected](https://nextjs.org/docs/messages/no-cache) 오류가 발생할 수 있습니다.

아래는 일반적인 CI 공급자에 대한 캐시 구성 예시입니다.

## Vercel[](https://nextjs.org/docs/pages/guides/ci-build-caching#vercel)

Next.js 캐싱이 자동으로 구성되므로 추가 작업이 필요 없습니다. Vercel에서 Turborepo를 사용 중이라면 [여기에서 더 알아보세요](https://vercel.com/docs/monorepos/turborepo).

## CircleCI[](https://nextjs.org/docs/pages/guides/ci-build-caching#circleci)

`.circleci/config.yml`의 `save_cache` 단계를 수정해 `.next/cache`를 포함하세요:
[code] 
    steps:
      - save_cache:
          key: dependency-cache-{{ checksum "yarn.lock" }}
          paths:
            - ./node_modules
            - ./.next/cache
[/code]

`save_cache` 키가 없다면 CircleCI의 [빌드 캐싱 설정 문서](https://circleci.com/docs/2.0/caching/)를 참고하세요.

## Travis CI[](https://nextjs.org/docs/pages/guides/ci-build-caching#travis-ci)

`.travis.yml`에 다음 내용을 추가하거나 병합하세요:
[code] 
    cache:
      directories:
        - $HOME/.cache/yarn
        - node_modules
        - .next/cache
[/code]

## GitLab CI[](https://nextjs.org/docs/pages/guides/ci-build-caching#gitlab-ci)

`.gitlab-ci.yml`에 다음 내용을 추가하거나 병합하세요:
[code] 
    cache:
      key: ${CI_COMMIT_REF_SLUG}
      paths:
        - node_modules/
        - .next/cache/
[/code]

## Netlify CI[](https://nextjs.org/docs/pages/guides/ci-build-caching#netlify-ci)

[`@netlify/plugin-nextjs`](https://www.npmjs.com/package/@netlify/plugin-nextjs)를 포함한 [Netlify Plugins](https://www.netlify.com/products/build/plugins/)를 사용하세요.

## AWS CodeBuild[](https://nextjs.org/docs/pages/guides/ci-build-caching#aws-codebuild)

`buildspec.yml`에 다음을 추가(또는 병합)하세요:
[code] 
    cache:
      paths:
        - 'node_modules/**/*' # Cache `node_modules` for faster `yarn` or `npm i`
        - '.next/cache/**/*' # Cache Next.js for faster application rebuilds
[/code]

## GitHub Actions[](https://nextjs.org/docs/pages/guides/ci-build-caching#github-actions)

GitHub의 [actions/cache](https://github.com/actions/cache)를 사용해 워크플로 파일에 다음 단계를 추가하세요:
[code] 
    uses: actions/cache@v4
    with:
      # See here for caching with `yarn`, `bun` or other package managers https://github.com/actions/cache/blob/main/examples.md or you can leverage caching with actions/setup-node https://github.com/actions/setup-node
      path: |
        ~/.npm
        ${{ github.workspace }}/.next/cache
      # Generate a new cache whenever packages or source files change.
      key: ${{ runner.os }}-nextjs-${{ hashFiles('**/package-lock.json') }}-${{ hashFiles('**/*.js', '**/*.jsx', '**/*.ts', '**/*.tsx') }}
      # If source files changed but packages didn't, rebuild from a prior cache.
      restore-keys: |
        ${{ runner.os }}-nextjs-${{ hashFiles('**/package-lock.json') }}-
[/code]

## Bitbucket Pipelines[](https://nextjs.org/docs/pages/guides/ci-build-caching#bitbucket-pipelines)

`bitbucket-pipelines.yml`의 최상위(`pipelines`와 동일한 수준)에 다음을 추가하거나 병합하세요:
[code] 
    definitions:
      caches:
        nextcache: .next/cache
[/code]

그런 다음 파이프라인 `step`의 `caches` 섹션에서 이를 참조하세요:
[code] 
    - step:
        name: your_step_name
        caches:
          - node
          - nextcache
[/code]

## Heroku[](https://nextjs.org/docs/pages/guides/ci-build-caching#heroku)

Heroku의 [custom cache](https://devcenter.heroku.com/articles/nodejs-support#custom-caching)를 사용해 최상위 package.json에 `cacheDirectories` 배열을 추가하세요:
[code] 
    "cacheDirectories": [".next/cache"]
[/code]

## Azure Pipelines[](https://nextjs.org/docs/pages/guides/ci-build-caching#azure-pipelines)

Azure Pipelines의 [Cache 작업](https://docs.microsoft.com/en-us/azure/devops/pipelines/tasks/utility/cache)을 사용해 `next build`를 실행하는 작업 이전에 다음 작업을 파이프라인 yaml 파일에 추가하세요:
[code] 
    - task: Cache@2
      displayName: 'Cache .next/cache'
      inputs:
        key: next | $(Agent.OS) | yarn.lock
        path: '$(System.DefaultWorkingDirectory)/.next/cache'
[/code]

## Jenkins (Pipeline)[](https://nextjs.org/docs/pages/guides/ci-build-caching#jenkins-pipeline)

Jenkins의 [Job Cacher](https://www.jenkins.io/doc/pipeline/steps/jobcacher/) 플러그인을 사용해, 일반적으로 `next build` 또는 `npm install`을 실행하는 `Jenkinsfile` 위치에 다음 빌드 단계를 추가하세요:
[code] 
    stage("Restore npm packages") {
        steps {
            // Writes lock-file to cache based on the GIT_COMMIT hash
            writeFile file: "next-lock.cache", text: "$GIT_COMMIT"
     
            cache(caches: [
                arbitraryFileCache(
                    path: "node_modules",
                    includes: "**/*",
                    cacheValidityDecidingFile: "package-lock.json"
                )
            ]) {
                sh "npm install"
            }
        }
    }
    stage("Build") {
        steps {
            // Writes lock-file to cache based on the GIT_COMMIT hash
            writeFile file: "next-lock.cache", text: "$GIT_COMMIT"
     
            cache(caches: [
                arbitraryFileCache(
                    path: ".next/cache",
                    includes: "**/*",
                    cacheValidityDecidingFile: "next-lock.cache"
                )
            ]) {
                // aka `next build`
                sh "npm run build"
            }
        }
    }
[/code]

이 내용이 도움이 되었나요?

지원됨.

전송

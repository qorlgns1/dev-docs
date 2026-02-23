---
title: 'Guides: CI Build Caching'
description: 'To improve build performance, Next.js saves a cache to  that is shared between builds.'
---

# Guides: CI Build Caching | Next.js

Source URL: https://nextjs.org/docs/pages/guides/ci-build-caching

[Pages Router](https://nextjs.org/docs/pages)[Guides](https://nextjs.org/docs/pages/guides)CI Build Caching

Copy page

# How to configure Continuous Integration (CI) build caching

Last updated February 20, 2026

To improve build performance, Next.js saves a cache to `.next/cache` that is shared between builds.

To take advantage of this cache in Continuous Integration (CI) environments, your CI workflow will need to be configured to correctly persist the cache between builds.

> If your CI is not configured to persist `.next/cache` between builds, you may see a [No Cache Detected](https://nextjs.org/docs/messages/no-cache) error.

Here are some example cache configurations for common CI providers:

## Vercel[](https://nextjs.org/docs/pages/guides/ci-build-caching#vercel)

Next.js caching is automatically configured for you. There's no action required on your part. If you are using Turborepo on Vercel, [learn more here](https://vercel.com/docs/monorepos/turborepo).

## CircleCI[](https://nextjs.org/docs/pages/guides/ci-build-caching#circleci)

Edit your `save_cache` step in `.circleci/config.yml` to include `.next/cache`:
[code] 
    steps:
      - save_cache:
          key: dependency-cache-{{ checksum "yarn.lock" }}
          paths:
            - ./node_modules
            - ./.next/cache
[/code]

If you do not have a `save_cache` key, please follow CircleCI's [documentation on setting up build caching](https://circleci.com/docs/2.0/caching/).

## Travis CI[](https://nextjs.org/docs/pages/guides/ci-build-caching#travis-ci)

Add or merge the following into your `.travis.yml`:
[code] 
    cache:
      directories:
        - $HOME/.cache/yarn
        - node_modules
        - .next/cache
[/code]

## GitLab CI[](https://nextjs.org/docs/pages/guides/ci-build-caching#gitlab-ci)

Add or merge the following into your `.gitlab-ci.yml`:
[code] 
    cache:
      key: ${CI_COMMIT_REF_SLUG}
      paths:
        - node_modules/
        - .next/cache/
[/code]

## Netlify CI[](https://nextjs.org/docs/pages/guides/ci-build-caching#netlify-ci)

Use [Netlify Plugins](https://www.netlify.com/products/build/plugins/) with [`@netlify/plugin-nextjs`](https://www.npmjs.com/package/@netlify/plugin-nextjs).

## AWS CodeBuild[](https://nextjs.org/docs/pages/guides/ci-build-caching#aws-codebuild)

Add (or merge in) the following to your `buildspec.yml`:
[code] 
    cache:
      paths:
        - 'node_modules/**/*' # Cache `node_modules` for faster `yarn` or `npm i`
        - '.next/cache/**/*' # Cache Next.js for faster application rebuilds
[/code]

## GitHub Actions[](https://nextjs.org/docs/pages/guides/ci-build-caching#github-actions)

Using GitHub's [actions/cache](https://github.com/actions/cache), add the following step in your workflow file:
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

Add or merge the following into your `bitbucket-pipelines.yml` at the top level (same level as `pipelines`):
[code] 
    definitions:
      caches:
        nextcache: .next/cache
[/code]

Then reference it in the `caches` section of your pipeline's `step`:
[code] 
    - step:
        name: your_step_name
        caches:
          - node
          - nextcache
[/code]

## Heroku[](https://nextjs.org/docs/pages/guides/ci-build-caching#heroku)

Using Heroku's [custom cache](https://devcenter.heroku.com/articles/nodejs-support#custom-caching), add a `cacheDirectories` array in your top-level package.json:
[code] 
    "cacheDirectories": [".next/cache"]
[/code]

## Azure Pipelines[](https://nextjs.org/docs/pages/guides/ci-build-caching#azure-pipelines)

Using Azure Pipelines' [Cache task](https://docs.microsoft.com/en-us/azure/devops/pipelines/tasks/utility/cache), add the following task to your pipeline yaml file somewhere prior to the task that executes `next build`:
[code] 
    - task: Cache@2
      displayName: 'Cache .next/cache'
      inputs:
        key: next | $(Agent.OS) | yarn.lock
        path: '$(System.DefaultWorkingDirectory)/.next/cache'
[/code]

## Jenkins (Pipeline)[](https://nextjs.org/docs/pages/guides/ci-build-caching#jenkins-pipeline)

Using Jenkins' [Job Cacher](https://www.jenkins.io/doc/pipeline/steps/jobcacher/) plugin, add the following build step to your `Jenkinsfile` where you would normally run `next build` or `npm install`:
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

Was this helpful?

supported.

Send

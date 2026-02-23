---
title: 'next.config.js: deploymentId'
description: 'Last updated February 20, 2026'
---

# next.config.js: deploymentId | Next.js

Source URL: https://nextjs.org/docs/app/api-reference/config/next-config-js/deploymentId

[Configuration](https://nextjs.org/docs/app/api-reference/config)[next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)deploymentId

Copy page

# deploymentId

Last updated February 20, 2026

The `deploymentId` option allows you to set an identifier for your deployment. This identifier is used for [version skew](https://nextjs.org/docs/app/guides/self-hosting#version-skew) protection and cache busting during rolling deployments.

next.config.js
[code]
    module.exports = {
      deploymentId: 'my-deployment-id',
    }
[/code]

You can also set the deployment ID using the `NEXT_DEPLOYMENT_ID` environment variable:
[code] 
    NEXT_DEPLOYMENT_ID=my-deployment-id next build
[/code]

> **Good to know:** If both are set, the `deploymentId` value in `next.config.js` takes precedence over the `NEXT_DEPLOYMENT_ID` environment variable.

## How it works[](https://nextjs.org/docs/app/api-reference/config/next-config-js/deploymentId#how-it-works)

When a `deploymentId` is configured, Next.js:

  1. Appends `?dpl=<deploymentId>` to static asset URLs (JavaScript, CSS, images)
  2. Adds an `x-deployment-id` header to client-side navigation requests
  3. Adds an `x-nextjs-deployment-id` header to navigation responses
  4. Injects a `data-dpl-id` attribute on the `<html>` element



When the client detects a mismatch between its deployment ID and the server's (via the response header), it triggers a hard navigation (full page reload) instead of a client-side navigation. This ensures users always receive assets and Server Functions from a consistent deployment version.

> **Good to know:** Next.js does not read the `?dpl=` query parameter on incoming requests. The query parameter is for cache busting (ensuring browsers and CDNs fetch fresh assets), not for routing. If you need version-aware routing, consult your hosting provider or CDN's documentation for implementing deployment-based routing.

## Use cases[](https://nextjs.org/docs/app/api-reference/config/next-config-js/deploymentId#use-cases)

### Rolling deployments[](https://nextjs.org/docs/app/api-reference/config/next-config-js/deploymentId#rolling-deployments)

During a rolling deployment, some server instances may be running the new version while others are still running the old version. Without a deployment ID, users might receive a mix of old and new assets, causing errors.

Setting a consistent `deploymentId` per deployment ensures:

  * Clients always request assets from a matching deployment version
  * Mismatches trigger a full reload to fetch the correct assets
  * Server Functions work correctly across deployment boundaries



### Multi-server environments[](https://nextjs.org/docs/app/api-reference/config/next-config-js/deploymentId#multi-server-environments)

When running multiple instances of your Next.js application behind a load balancer, all instances for the same deployment should use the same `deploymentId`.

next.config.js
[code]
    module.exports = {
      deploymentId: process.env.DEPLOYMENT_VERSION || process.env.GIT_SHA,
    }
[/code]

## Version History[](https://nextjs.org/docs/app/api-reference/config/next-config-js/deploymentId#version-history)

Version| Changes  
---|---  
`v14.1.4`| `deploymentId` stabilized as top-level config option.  
`v13.4.10`| `experimental.deploymentId` introduced.  
  
## Related[](https://nextjs.org/docs/app/api-reference/config/next-config-js/deploymentId#related)

  * [Self-Hosting - Version Skew](https://nextjs.org/docs/app/guides/self-hosting#version-skew)
  * [generateBuildId](https://nextjs.org/docs/app/api-reference/config/next-config-js/generateBuildId)



Was this helpful?

supported.

Send

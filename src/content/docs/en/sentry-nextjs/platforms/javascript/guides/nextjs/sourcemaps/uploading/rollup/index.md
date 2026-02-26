---
title: 'Rollup | Sentry for Next.js'
description: "This guide assumes you're using a Sentry SDK version  or higher. If you're on an older version and you want to upload source maps, we recommend upgrad..."
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/uploading/rollup

# Rollup | Sentry for Next.js

This guide assumes you're using a **Sentry SDK version `7.47.0` or higher**. If you're on an older version and you want to upload source maps, we recommend upgrading your SDK to the newest version.

You can use the Sentry Rollup plugin to automatically create releases and upload source maps to Sentry when bundling your app.

## [Automatic Setup](https://docs.sentry.io/platforms/javascript/guides/koa/sourcemaps/uploading/rollup.md#automatic-setup)

The easiest way to configure source map uploading with rollup is by using the Sentry Wizard:

```bash
npx @sentry/wizard@latest -i sourcemaps
```

The wizard will guide you through the following steps:

* Logging into Sentry and selecting a project
* Installing the necessary Sentry packages
* Configuring your build tool to generate and upload source maps
* Configuring your CI to upload source maps

If you'd rather manually configure source map uploading with the CLI, follow the steps below.

## [Manual Setup](https://docs.sentry.io/platforms/javascript/guides/koa/sourcemaps/uploading/rollup.md#manual-setup)

Install the Sentry Rollup plugin:

```bash
npm install @sentry/rollup-plugin --save-dev
```

- [Configuration](https://docs.sentry.io/platforms/javascript/guides/koa/sourcemaps/uploading/rollup.md#configuration)

To upload source maps you have to configure an [Organization Token](https://sentry.io/orgredirect/organizations/:orgslug/settings/auth-tokens/).

Alternatively, you can also use a [Personal Token](https://sentry.io/orgredirect/organizations/:orgslug/settings/account/api/auth-tokens/), with the "Project: Read & Write" and "Release: Admin" permissions.

Auth tokens can be passed to the plugin explicitly with the `authToken` option, with a `SENTRY_AUTH_TOKEN` environment variable, or with an `.env.sentry-build-plugin` file (don't forget to add it to your `.gitignore` file, as this is sensitive data) in the working directory when building your project. We recommend you add the auth token to your CI/CD environment as an environment variable.

Learn more about configuring the plugin in our [Sentry Rollup Plugin documentation](https://www.npmjs.com/package/@sentry/rollup-plugin).

`.env.sentry-build-plugin`

```bash
SENTRY_AUTH_TOKEN=___ORG_AUTH_TOKEN___
```

Example:

`rollup.config.js`

```javascript
import { sentryRollupPlugin } from "@sentry/rollup-plugin";

export default {
  output: {
    sourcemap: "hidden", // Source map generation must be turned on ("hidden", true, etc.)
  },
  plugins: [
    // Put the Sentry rollup plugin after all other plugins
    sentryRollupPlugin({
      org: "___ORG_SLUG___",
      project: "___PROJECT_SLUG___",
      authToken: process.env.SENTRY_AUTH_TOKEN,
      sourcemaps: {
        // As you're enabling client source maps, you probably want to delete them after they're uploaded to Sentry.
        // Set the appropriate glob pattern for your output folder - some glob examples below:
        filesToDeleteAfterUpload: [
          "./**/*.map",
          ".*/**/public/**/*.map",
          "./dist/**/client/**/*.map",
        ],
      },
    }),
  ],
};
```

Generating source maps **may expose them to the public**, potentially causing your source code to be leaked. You can prevent this by configuring your server to deny access to `.js.map` files, or by using [Sentry Rollup Plugin's `sourcemaps.filesToDeleteAfterUpload`](https://www.npmjs.com/package/@sentry/rollup-plugin#sourcemapsfilestodeleteafterupload) option to delete source maps after they've been uploaded to Sentry.


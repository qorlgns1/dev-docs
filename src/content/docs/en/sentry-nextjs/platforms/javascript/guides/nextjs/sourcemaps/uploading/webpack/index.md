---
title: 'Webpack | Sentry for Next.js'
description: "This guide assumes you're using a Sentry SDK version  or higher. If you're on an older version and you want to upload source maps, we recommend upgrad..."
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/uploading/webpack

# Webpack | Sentry for Next.js

This guide assumes you're using a Sentry **SDK version `7.47.0` or higher**. If you're on an older version and you want to upload source maps, we recommend upgrading your SDK to the newest version.

You can use the Sentry webpack plugin to automatically create releases and upload source maps to Sentry when bundling your app.

## [Automatic Setup](https://docs.sentry.io/platforms/javascript/sourcemaps/uploading/webpack.md#automatic-setup)

The easiest way to configure source map uploading with webpack is by using the Sentry Wizard:

```bash
npx @sentry/wizard@latest -i sourcemaps
```

The wizard will guide you through the following steps:

* Logging into Sentry and selecting a project
* Installing the necessary Sentry packages
* Configuring your build tool to generate and upload source maps
* Configuring your CI to upload source maps

If you'd rather configure source map uploading with webpack manually, follow the steps below.

## [Manual Setup](https://docs.sentry.io/platforms/javascript/sourcemaps/uploading/webpack.md#manual-setup)

Install the Sentry webpack plugin:

```bash
npm install @sentry/webpack-plugin --save-dev
```

- [Configuration](https://docs.sentry.io/platforms/javascript/sourcemaps/uploading/webpack.md#configuration)

To upload source maps you have to configure an [Organization Token](https://sentry.io/orgredirect/organizations/:orgslug/settings/auth-tokens/).

Alternatively, you can also use a [Personal Token](https://sentry.io/orgredirect/organizations/:orgslug/settings/account/api/auth-tokens/), with the "Project: Read & Write" and "Release: Admin" permissions.

Auth tokens can be passed to the plugin explicitly with the `authToken` option, with a `SENTRY_AUTH_TOKEN` environment variable, or with an `.env.sentry-build-plugin` file (don't forget to add it to your `.gitignore` file, as this is sensitive data) in the working directory when building your project. We recommend you add the auth token to your CI/CD environment as an environment variable.

Learn more about configuring the plugin in our [Sentry webpack plugin documentation](https://www.npmjs.com/package/@sentry/webpack-plugin).

`.env.sentry-build-plugin`

```bash
SENTRY_AUTH_TOKEN=___ORG_AUTH_TOKEN___
```

And the following webpack config:

`webpack.config.js`

```javascript
const { sentryWebpackPlugin } = require("@sentry/webpack-plugin");

module.exports = {
  // ... other config above ...

  devtool: "hidden-source-map", // Source map generation must be turned on ("hidden-source-map", "source-map", etc.)
  plugins: [
    sentryWebpackPlugin({
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

Generating source maps **may expose them to the public**, potentially causing your source code to be leaked. You can prevent this by configuring your server to deny access to `.js.map` files, or by using [Sentry Webpack Plugin's `sourcemaps.filesToDeleteAfterUpload`](https://www.npmjs.com/package/@sentry/webpack-plugin#sourcemapsfilestodeleteafterupload) option to delete source maps after they've been uploaded to Sentry.

The Sentry webpack plugin doesn't upload source maps in watch-mode/development-mode. We recommend running a production build to test your configuration.

If you use [SourceMapDevToolPlugin](https://webpack.js.org/plugins/source-map-dev-tool-plugin) for more fine-grained control of source map generation, turn off `noSources` so Sentry can display proper source code context in event stack traces.


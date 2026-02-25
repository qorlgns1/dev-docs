---
title: 'Ionic | Sentry for Next.js'
description: "In this guide, you'll learn how to successfully upload source maps for TypeScript using our  tool."
---

Source URL: https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/uploading/ionic

# Ionic | Sentry for Next.js

In this guide, you'll learn how to successfully upload source maps for TypeScript using our `sentry-cli` tool.

This guide assumes the following:

* `sentry-cli` version >= `2.17.0`
* Sentry JavaScript SDK version >= `7.47.0`

This guide is only applicable if you're using `tsc` to compile your project. If you use another tool (such as webpack) in combination with TypeScript, you'll most likely want to follow that guide instead.

## [Automatic Setup](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/uploading/ionic.md#automatic-setup)

The easiest way to configure source map uploading with `tsc` and `sentry-cli` is by using the Sentry Wizard:

```bash
npx @sentry/wizard@latest -i sourcemaps
```

The wizard will guide you through the following steps:

* Logging into Sentry and selecting a project
* Installing the necessary Sentry packages
* Configuring your build tool to generate and upload source maps
* Configuring your CI to upload source maps

If you'd rather configure source maps manually, follow the steps below.

## [Manual Setup](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/uploading/ionic.md#manual-setup)

- [1. Generate Source Maps](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/uploading/ionic.md#1-generate-source-maps)

First, configure the TypeScript compiler to output source maps:

`tsconfig.json`

```json
{
  "compilerOptions": {
    "sourceMap": true,
    "inlineSources": true,

    // Set `sourceRoot` to  "/" to strip the build path prefix from
    // generated source code references. This will improve issue grouping in Sentry.
    "sourceRoot": "/"
  }
}
```

Generating source maps may expose them to the public, potentially causing your source code to be leaked. You can prevent this by configuring your server to deny access to `.js.map` files, or by deleting the source maps before deploying your application.

- [2. Configure Sentry CLI](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/uploading/ionic.md#2-configure-sentry-cli)

You can find installation instructions for Sentry CLI here: [https://docs.sentry.io/cli/installation/](https://docs.sentry.io/cli/installation.md)

For more info on `sentry-cli` configuration visit the [Sentry CLI configuration docs](https://docs.sentry.io/cli/configuration.md).

Make sure `sentry-cli` is configured for your project. For that you can use environment variables:

`.env.local`

```bash
SENTRY_ORG=___ORG_SLUG___
SENTRY_PROJECT=___PROJECT_SLUG___
SENTRY_AUTH_TOKEN=___ORG_AUTH_TOKEN___
```

- [3. Inject Debug IDs Into Artifacts](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/uploading/ionic.md#3-inject-debug-ids-into-artifacts)

Debug IDs are used to match the stack frame of an event with its corresponding minified source and source map file. Visit [What are Debug IDs](https://docs.sentry.io/platforms/javascript/sourcemaps/troubleshooting_js/debug-ids.md) if you want to learn more about Debug IDs.

To inject Debug IDs, use the following command:

```bash
sentry-cli sourcemaps inject /path/to/directory
```

#
- [Verify Debug IDs Were Injected in Artifacts](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/uploading/ionic.md#verify-debug-ids-were-injected-in-artifacts)

Minified source files should contain at the end a comment named `debugId` like:

`example_minified_file.js`

```javascript
...
//# debugId=<debug_id>
//# sourceMappingURL=<sourcemap_url>
```

Source maps should contain a field named `debug_id` like:

`example_source_map.js.map`

```json
{
    ...
    "debug_id":"<debug_id>",
    ...
}
```

- [4. Upload Artifact Bundle](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/uploading/ionic.md#4-upload-artifact-bundle)

After you've injected Debug IDs into your artifacts, upload them using the following command.

```bash
sentry-cli sourcemaps upload /path/to/directory
```

#
- [Verify That Artifact Bundles Were Uploaded](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/uploading/ionic.md#verify-that-artifact-bundles-were-uploaded)

Open up Sentry and navigate to **Project Settings > Source Maps**. If you choose “Artifact Bundles” in the tabbed navigation, you'll see all the artifact bundles that have been successfully uploaded to Sentry.

- [5. Deploy your Application](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/uploading/ionic.md#5-deploy-your-application)

If you're following this guide from your local machine, then you've successfully:

1. Generated minified source and source map files (artifacts) by running your application's build process
2. Injected Debug IDs into the artifacts you've just generated
3. Uploaded those artifacts to Sentry with our upload command

The last step is deploying a new version of your application using the generated artifacts you created in step one. **We strongly recommend that you integrate `sentry-cli` into your CI/CD Pipeline**, to ensure each subsequent deploy will automatically inject debug IDs into each artifact and upload them directly to Sentry.

- [Optional Steps](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/uploading/ionic.md#optional-steps)

##### Warning

Only follow these optional steps if you have concluded that you absolutely need them. Using `release` and `dist` values will make your artifact upload more specific, but will also make the entire process less forgiving, which may lead to your code not being unminified by Sentry.

#
- [Associating `release` with Artifact Bundle](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/uploading/ionic.md#associating-release-with-artifact-bundle)

Provide a `release` property in your SDK options.

```javascript
Sentry.init({
  // This value must be identical to the release name specified during upload
  // with the `sentry-cli`.
  release: "<release_name>",
});
```

Afterwards, run the `sourcemaps upload` command with the additional `--release` option. Please ensure that the value specified for `<release_name>` is the same value specified in your SDK options.

```bash
sentry-cli sourcemaps upload --release=<release_name> /path/to/directory
```

Running `upload` with `--release` **doesn't automatically create a release in Sentry**. Either wait until the first event with the new release set in `Sentry.init` is sent to Sentry, or create a release with the same name in a separate step [with the CLI](https://docs.sentry.io/cli/releases.md).

#
- [Associating `dist` with Artifact Bundle](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/uploading/ionic.md#associating-dist-with-artifact-bundle)

In addition to `release`, you can also add a `dist` to your uploaded artifacts, to set the distribution identifier for uploaded files. To do so, run the `sourcemaps upload` command with the additional `--dist` option.

Provide `release` and `dist` properties in your SDK options.

```javascript
Sentry.init({
  // These values must be identical to the release and dist names specified during upload
  // with the `sentry-cli`.
  release: "<release_name>",
  dist: "<dist_name>",
});
```

The distribution identifier is used to distinguish between multiple files of the same name within a single release. `dist` can be used to disambiguate build or deployment variants.

```bash
sentry-cli sourcemaps upload --release=<release_name> --dist=<dist_name> /path/to/directory
```

## [Dealing with TSLib](https://docs.sentry.io/platforms/javascript/guides/nextjs/sourcemaps/uploading/ionic.md#dealing-with-tslib)

During compilation, TypeScript will inject some of its runtime dependencies into the output files it produces if needed. It can include things like polyfills for function generators or APIs that may not be available in all the environments. However, the fact that there aren't any original sources makes it impossible to map frames from compiled code to the original sources.

As a workaround, you'll need to tell the TypeScript compiler to use `tslib`, its own 3rd party package, (which is internally the part of a compiler) instead of injecting runtime dependencies. You'll only need to change what's inside the TypeScript config file, not your source code. Here's how:

1. Make sure that `tslib` is listed as a dependency in your `package.json` file.
2. Once that's done, add two entries in the `compilerOptions` section of your `tsconfig.json`:

* `"noEmitHelpers": true` and -`"importHelpers": true`.

That's it! Now you should be able to correctly map the source maps for all your stack trace frames, including internal TypeScript compiler code snippets.


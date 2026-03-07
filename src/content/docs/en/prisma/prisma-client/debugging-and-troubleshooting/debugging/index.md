---
title: "Debugging"
description: "This page explains how to enable debugging output for Prisma Client by setting the  environment variable"
---

Source URL: https://docs.prisma.io/docs/orm/prisma-client/debugging-and-troubleshooting/debugging

# Debugging

This page explains how to enable debugging output for Prisma Client by setting the `DEBUG` environment variable

You can enable debugging output in Prisma Client and Prisma CLI via the [`DEBUG`](https://docs.prisma.io/docs/orm/reference/environment-variables-reference#debug) environment variable. It accepts two namespaces to print debugging output:

- `prisma:engine`: Prints relevant debug messages happening in a Prisma ORM [engine](https://github.com/prisma/prisma-engines/)
- `prisma:client`: Prints relevant debug messages happening in the Prisma Client runtime
- `prisma*`: Prints all debug messages from Prisma Client or CLI
- `*`: Prints all debug messages

Prisma Client can be configured to log warnings, errors and information related to queries sent to the database. See [Configuring logging](https://docs.prisma.io/docs/orm/prisma-client/observability-and-logging/logging) for more information.

## Setting the `DEBUG` environment variable

Here are examples for setting these debugging options in bash:

```
    # enable only `prisma:engine`-level debugging output
    export DEBUG="prisma:engine"

    # enable only `prisma:client`-level debugging output
    export DEBUG="prisma:client"

    # enable both `prisma-client`- and `engine`-level debugging output
    export DEBUG="prisma:client,prisma:engine"
```

To enable all `prisma` debugging options, set `DEBUG` to `prisma*`:

```
    export DEBUG="prisma*"
```

On Windows, use `set` instead of `export`:

```
    set DEBUG="prisma*"
```

To enable _all_ debugging options, set `DEBUG` to `*`:

```
    export DEBUG="*"
```

---
title: "Add methods to Prisma Client"
description: "Extend the functionality of Prisma Client, client component"
---

Source URL: https://docs.prisma.io/docs/orm/prisma-client/client-extensions/client

# Add methods to Prisma Client

Extend the functionality of Prisma Client, client component

You can use the `client` [Prisma Client extensions](https://docs.prisma.io/docs/orm/prisma-client/client-extensions) component to add top-level methods to Prisma Client.

## Extend Prisma Client

Use the `$extends` [client-level method](https://docs.prisma.io/docs/orm/reference/prisma-client-reference#client-methods) to create an _extended client_. An extended client is a variant of the standard Prisma Client that is wrapped by one or more extensions. Use the `client` extension component to add top-level methods to Prisma Client.

To add a top-level method to Prisma Client, use the following structure:

```
    const prisma = new PrismaClient().$extends({
      client?: { ... }
    })
```

- Example

The following example uses the `client` component to add two methods to Prisma Client:

- `$log` outputs a message.
- `$totalQueries` returns the number of queries executed by the current client instance.

```
    let total = 0;
    const prisma = new PrismaClient().$extends({
      client: {
        $log: (s: string) => console.log(s),
        async $totalQueries() {
          return total;
        },
      },
      query: {
        $allModels: {
          async $allOperations({ query, args }) {
            total += 1;
            return query(args);
          },
        },
      },
    });

    async function main() {
      prisma.$log("Hello world");
      const totalQueries = await prisma.$totalQueries();
      console.log(totalQueries);
    }
```

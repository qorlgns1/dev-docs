---
title: 'Featured sponsor: Jazz'
description: 'TypeScript-first schema validation with static type inference'
---

Source URL: https://zod.dev/

# Zod

TypeScript-first schema validation with static type inference
by [@colinhacks](https://x.com/colinhacks)

[](https://github.com/colinhacks/zod/actions?query=branch%3Amain)[](https://twitter.com/colinhacks)[](https://opensource.org/licenses/MIT)[](https://www.npmjs.com/package/zod)[](https://github.com/colinhacks/zod)

[Website](https://zod.dev) • [Discord](https://discord.gg/RcG33DQJdf) • [𝕏](https://twitter.com/colinhacks) • [Bluesky](https://bsky.app/profile/zod.dev)

Zod 4 is now stable! Read the [release notes here](https://zod.dev/v4).

## Featured sponsor: Jazz

[](https://jazz.tools/?utm_source=zod)

Interested in featuring? [Get in touch.](https://zod.dev/cdn-cgi/l/email-protection#85f6f5eaebf6eaf7f6edecf5c5e6eae9ecebede4e6eef6abe6eae8)

## [Introduction](https://zod.dev/?id=introduction)

Zod is a TypeScript-first validation library. Using Zod, you can define _schemas_ you can use to validate data, from a simple `string` to a complex nested object.
```
    import * as z from "zod";

    const User = z.object({
      name: z.string(),
    });

    // some untrusted data...
    const input = { /* stuff */ };

    // the parsed result is validated and type safe!
    const data = User.parse(input);

    // so you can use it with confidence :)
    console.log(data.name);
```

## [Features](https://zod.dev/?id=features)

  * Zero external dependencies
  * Works in Node.js and all modern browsers
  * Tiny: 2kb core bundle (gzipped)
  * Immutable API: methods return a new instance
  * Concise interface
  * Works with TypeScript and plain JS
  * Built-in JSON Schema conversion
  * Extensive ecosystem

## [Installation](https://zod.dev/?id=installation)
```
    npm install zod
```

Zod is also available as `@zod/zod` on [jsr.io](https://jsr.io/@zod/zod).

Zod provides an MCP server that can be used by agents to search Zod's docs. To add to your editor, follow [these instructions](https://share.inkeep.com/zod/mcp). Zod also provides an [llms.txt](https://zod.dev/llms.txt) file.

## [Requirements](https://zod.dev/?id=requirements)

Zod is tested against _TypeScript v5.5_ and later. Older versions may work but are not officially supported.

- [`"strict"`](https://zod.dev/?id=strict)

You must enable `strict` mode in your `tsconfig.json`. This is a best practice for all TypeScript projects.
```
    // tsconfig.json
    {
      // ...
      "compilerOptions": {
        // ...
        "strict": true
      }
    }
```

## [Ecosystem](https://zod.dev/?id=ecosystem)

Zod has a thriving ecosystem of libraries, tools, and integrations. Refer to the [Ecosystem page](https://zod.dev/ecosystem) for a complete list of libraries that support Zod or are built on top of it.

  * [Resources](https://zod.dev/ecosystem?id=resources)
  * [API Libraries](https://zod.dev/ecosystem?id=api-libraries)
  * [Form Integrations](https://zod.dev/ecosystem?id=form-integrations)
  * [Zod to X](https://zod.dev/ecosystem?id=zod-to-x)
  * [X to Zod](https://zod.dev/ecosystem?id=x-to-zod)
  * [Mocking Libraries](https://zod.dev/ecosystem?id=mocking-libraries)
  * [Powered by Zod](https://zod.dev/ecosystem?id=powered-by-zod)

I also contribute to the following projects, which I'd like to highlight:

  * [tRPC](https://trpc.io) \- End-to-end typesafe APIs, with support for Zod schemas
  * [React Hook Form](https://react-hook-form.com) \- Hook-based form validation with a [Zod resolver](https://react-hook-form.com/docs/useform#resolver)
  * [zshy](https://github.com/colinhacks/zshy) \- Originally created as Zod's internal build tool. Bundler-free, batteries-included build tool for TypeScript libraries. Powered by `tsc`.

## [Sponsors](https://zod.dev/?id=sponsors)

Sponsorship at any level is appreciated and encouraged. If you built a paid product using Zod, consider one of the [corporate tiers](https://github.com/sponsors/colinhacks).

- [Platinum](https://zod.dev/?id=platinum)

[](https://www.coderabbit.ai/)

Cut code review time & bugs in half

[coderabbit.ai](https://www.coderabbit.ai/)

- [Gold](https://zod.dev/?id=gold)

[](https://brand.dev/?utm_source=zod)

API for logos, colors, and company info

[brand.dev](https://brand.dev/?utm_source=zod)

[](https://www.courier.com/?utm_source=zod&utm_campaign=osssponsors)

The API platform for sending notifications

[courier.com](https://www.courier.com/?utm_source=zod&utm_campaign=osssponsors)

[](https://liblab.com/?utm_source=zod)

Generate better SDKs for your APIs

[liblab.com](https://liblab.com/?utm_source=zod)

[](https://neon.tech)

Serverless Postgres — Ship faster

[neon.tech](https://neon.tech)

[](https://retool.com/?utm_source=github&utm_medium=referral&utm_campaign=zod)

Build AI apps and workflows with Retool AI

[retool.com](https://retool.com/?utm_source=github&utm_medium=referral&utm_campaign=zod)

[](https://stainlessapi.com)

Generate best-in-class SDKs

[stainlessapi.com](https://stainlessapi.com)

[](https://speakeasy.com/?utm_source=zod+docs)

SDKs & Terraform providers for your API

[speakeasy.com](https://speakeasy.com/?utm_source=zod+docs)

- [Silver](https://zod.dev/?id=silver)

[sanity.io](https://www.sanity.io/)

[subtotal.com](https://www.subtotal.com/?utm_source=zod)

[nitric.io](https://nitric.io/)

[propelauth.com](https://www.propelauth.com/)

[cerbos.dev](https://cerbos.dev/)

[scalar.com](https://scalar.com/)

[trigger.dev](https://trigger.dev)

[transloadit.com](https://transloadit.com/?utm_source=zod&utm_medium=referral&utm_campaign=sponsorship&utm_content=github)

[infisical.com](https://infisical.com)

[whop.com](https://whop.com/)

[cryptojobslist.com](https://cryptojobslist.com/)

[plain.com](https://plain.com/)

[inngest.com](https://inngest.com/)

[storyblok.com](https://storyblok.com/)

[mux.link/zod](https://mux.link/zod)

- [Bronze](https://zod.dev/?id=bronze)

[](https://mintlify.com)[mintlify.com](https://mintlify.com)

[](https://www.val.town/)[val.town](https://www.val.town/)

[](https://www.route4me.com/)[route4me.com](https://www.route4me.com/)

[](https://encore.dev)[encore.dev](https://encore.dev)

[](https://www.replay.io/)[replay.io](https://www.replay.io/)

[](https://www.numeric.io)[numeric.io](https://www.numeric.io)

[](https://marcatopartners.com)[marcatopartners.com](https://marcatopartners.com)

[](https://interval.com)[interval.com](https://interval.com)

[](https://seasoned.cc)[seasoned.cc](https://seasoned.cc)

[](https://www.bamboocreative.nz/)[bamboocreative.nz](https://www.bamboocreative.nz/)

[](https://github.com/jasonLaster)[github.com/jasonLaster](https://github.com/jasonLaster)

[](https://www.clipboardhealth.com/engineering)[clipboardhealth.com/engineering](https://www.clipboardhealth.com/engineering)


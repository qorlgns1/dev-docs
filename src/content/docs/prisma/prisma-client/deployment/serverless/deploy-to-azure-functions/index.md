---
title: "Azure Functions에 배포하기"
description: "Prisma Client 기반 REST API를 Azure Functions에 배포하고 Azure SQL 데이터베이스에 연결하는 방법을 알아보세요."
---

출처 URL: https://docs.prisma.io/docs/orm/prisma-client/deployment/serverless/deploy-to-azure-functions

# Azure Functions에 배포하기

Prisma Client 기반 REST API를 Azure Functions에 배포하고 Azure SQL 데이터베이스에 연결하는 방법을 알아보세요.

이 가이드는 Node.js 기반 함수 앱을 [Azure Functions](https://azure.microsoft.com/en-us/products/functions/)를 사용해 Azure에 배포할 때 흔히 발생하는 문제를 피하는 방법을 설명합니다.

Azure Functions는 서버리스 배포 플랫폼입니다. 코드를 배포하기 위해 인프라를 직접 유지관리할 필요가 없습니다. Azure Functions에서 기본 구성 단위는 [function app](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference?tabs=blob&pivots=programming-language-typescript)입니다. function app은 함수가 실행되는 Azure 내 실행 컨텍스트를 제공합니다. 이는 Azure가 함께 관리, 배포, 확장하는 하나 이상의 개별 함수로 구성됩니다. 여러 함수를 하나의 논리적 단위로 구성하고 통합 관리할 수 있습니다.

## Prerequisites

- Prisma ORM이 포함된 기존 function app 프로젝트

## Things to know

Prisma ORM은 Azure functions와 잘 작동하지만, 애플리케이션 배포 전에 알아두어야 할 몇 가지 사항이 있습니다.

- Connection pooling

일반적으로 데이터베이스와 상호작용하기 위해 FaaS(Function as a Service) 환경을 사용하면, 함수가 호출될 때마다 데이터베이스에 새 연결이 만들어질 수 있습니다. 이는 계속 실행되는 Node.js 서버에서는 문제가 되지 않습니다. 따라서 더 나은 성능을 위해 DB 연결을 풀링하는 것이 유리합니다. 이 문제를 해결하려면 [Prisma Postgres](https://docs.prisma.io/docs/postgres)를 사용할 수 있습니다. 다른 해결 방법은 [서버리스 환경용 연결 관리 가이드](https://docs.prisma.io/docs/orm/prisma-client/setup-and-configuration/databases-connections#serverless-environments-faas)를 참고하세요.

## Summary

Prisma Client API를 더 깊이 이해하려면 함수 핸들러를 살펴보고 [Prisma Client API Reference](https://docs.prisma.io/docs/orm/reference/prisma-client-reference)를 확인해 보세요.

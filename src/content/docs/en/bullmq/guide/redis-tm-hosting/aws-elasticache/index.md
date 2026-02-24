---
title: 'AWS Elasticache'
description: 'Elasticache is a managed caching service offered by Amazon Web Services (AWS), and it can be a good option when using BullMQ within the AWS infrastruc...'
---

Source URL: https://docs.bullmq.io/guide/redis-tm-hosting/aws-elasticache

# AWS Elasticache

Elasticache is a managed caching service offered by Amazon Web Services (AWS), and it can be a good option when using BullMQ within the AWS infrastructure.

Here are some points to consider when using Elasticache with BullMQ within AWS:

1. Use the standard cache-nodes setup (i.e. not the serverless version, as serverless for the moment uses an incompatible maxmemory-policy)
2. In order to access your Elasticache instance you will need to create a security group that allows the instance to be accessible to the services running BullMQ instances.
3.

<figure><img src="https://1340146492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LUuDmt_xXMfG66Rn1GA%2Fuploads%2Fgit-blob-b5e688395c2061a69a970890d35e77fa217a460a%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

4\. You will need to specify a VPC and an Inbound rule. Most likely just a custom TCP with port range 6379 and some suitable source (anywhere works well for testing and in some simpler cases), remember that the cluster will not be accessible outside from AWS in any case. 5. Attach the security group to your Elasticache cluster and to the services that need to access it. 6. Make sure that you are using maxmemory-policy: noeviction in your Redis parameters. As you cannot modify any default parameter group you will need to create a new one.

```
1. Go to Elasticache > Parameter Groups and click on Create.
2. Fill name, description, and Family, at the time of writing redis7 is the newest and the recommended one.

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>
```

7\. Click on "Create". Then find the parameter group in the list. Click on Edit parameter values and then search for maxmemory-policy:

<figure><img src="https://1340146492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LUuDmt_xXMfG66Rn1GA%2Fuploads%2Fgit-blob-6305ad6bc21de4aa7e6e56ea7d8ee9772d895226%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

8. Change the value to "noeviction":

<figure><img src="https://1340146492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LUuDmt_xXMfG66Rn1GA%2Fuploads%2Fgit-blob-556e6c2decabcb31969d8e0913077e2ba118142b%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

9. Save changes. Now you can go to your elasticache cluster and change the parameter group to your custom group. Just find your instance, click on modify and go to cluster settings where you can change the parameter group:

<figure><img src="https://1340146492-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LUuDmt_xXMfG66Rn1GA%2Fuploads%2Fgit-blob-837ae979da2ee9a9ed1405a576068d3dfbab2ea9%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

10. Preview changes and Modify. After this your cluster is ready to be used with BullMQ.


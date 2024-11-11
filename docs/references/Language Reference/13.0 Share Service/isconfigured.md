---
title: IsConfigured
pathName: isconfigured
parent: share_service
status: imported
section: references
---

## Definition

Sets when the Share Service is correctly configured. Typically this would be set after the account is authorized, at which point the adapter will allow for the user to share content to the sharing service.

{% callout type="note" %}

It is not required for a Share Service to authorize a user, therefore it is possible to set **IsConfigured** to true in **State.SetDefaults** which will bypass any sort of authorization or additional setup that may be needed for the share adapter.

{% /callout %}

## Property Value

A bool value when true determines if the Share Adapter is properly configured.

## Syntax

**IsConfigured**

## Examples

```csharp
public override void OnAuthorizeAccount()
{
   //Authorization logic would be here, after success, set **IsConfigured** to true.

   IsConfigured = true;

```

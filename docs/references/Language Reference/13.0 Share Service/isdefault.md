---
title: IsDefault
pathName: isdefault
parent: share_service
status: imported
section: references
---

## Definition

Sets the default Share Service used when the type of sharing service is selected.

For example, if you are using two different email adapters, you may set one to be the default when the user selects the email sharing service. Setting this property as the default would only apply to any email adapters and would not apply to any other types of sharing services which have their own respective default adapter.

## Property Value

A bool value that represents if the current adapter is default Share Service used for that type of sharing service.

{% callout type="warning" %}

This property should ONLY be set from the **OnStateChange()** method during **State.SetDefaults**.

{% /callout %}

## Syntax

**Default**

## Examples

```csharp
protected override void OnStateChange()
{
    if (State == State.SetDefaults)
    {
        Default        = false;
    }
}

```

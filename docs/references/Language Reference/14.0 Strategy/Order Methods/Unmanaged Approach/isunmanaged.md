---
title: IsUnmanaged
pathName: isunmanaged
parent: unmanaged_approach
section: references
status: imported
---

## Definition

Determines if the strategy will be using Unmanaged order methods.

{% callout type="note" %}

Unmanaged order methods and **Managed order methods** cannot be used interchangeably. When **IsUnmanaged** is set to true, calling managed order methods such as **EnterLong()**, **SetStopLoss()**, etc., will generate an error which will be displayed on the **Log tab** of the Control Center.

{% /callout %}

## Property Value

This property returns true if the strategy will use Unmanaged order methods; otherwise, false. Default is set to false.

{% callout type="warning" %}

Warning: This property should ONLY be set from the **OnStateChange()** method during **State.SetDefaults** or **State.Configure**.

{% /callout %}

## Syntax

**IsUnmanaged**

## Examples

```csharp
protected override void OnStateChange()
{
    if (State == State.SetDefaults)
    {
        // Use Unmanaged order methods
        IsUnmanaged = true;
    }
}
```

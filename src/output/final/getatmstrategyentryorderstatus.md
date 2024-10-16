---
title: "GetAtmStrategyEntryOrderStatus()"
pathName: /docs/desktop/getatmstrategyentryorderstatus
---

## Definition

Gets the current state of the specified entry order.

{% callout type="note" %}
If the method can't find the specified order, an empty array is returned.
{% /callout %}

## Method Return Value

A `string[]` array holding three elements that represent average fill price, filled amount and order state.

## Syntax

```csharp
GetAtmStrategyEntryOrderStatus(string orderId)
```

## Parameters

|  |  |
| --- | --- |
| orderId | The unique identifier for the entry order |

## Examples

```csharp
protected override void OnBarUpdate()
{
    string[] entryOrder = GetAtmStrategyEntryOrderStatus("orderId");
    // Check length to ensure that returned array holds order information
    if (entryOrder.Length > 0)
    {
        Print("Average fill price is " + entryOrder[0].ToString());
        Print("Filled amount is " + entryOrder[1].ToString());
        Print("Current state is " + entryOrder[2].ToString());
    }
}
```


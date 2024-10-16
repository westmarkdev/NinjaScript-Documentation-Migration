---
title: "AtmStrategyCancelEntryOrder()"
pathName: /docs/desktop/atmstrategycancelentryorder
---

## Definition

Cancels the specified entry order determined by the string "orderId" parameter.

{% callout type="note" %}
1. This method is intended ONLY for orders submitted as [Atm Entry Orders](/docs/desktop/atmstrategycreate) and assumes the [OrderState](/docs/desktop/getatmstrategyentryorderstatus) is NOT terminal (i.e., Cancelled, Filled, Rejected, Unknown).
2. If the specified order does not exist, the method returns false and an error is logged.
{% /callout %}

## Method Return Value

Returns true if the specified order was found; otherwise false.

## Syntax

```csharp
AtmStrategyCancelEntryOrder(string orderId)
```

{% callout type="warning" %}
This method should ONLY be called once the strategy [State](/docs/desktop/state) has reached State.Realtime
{% /callout %}

## Parameters

|  |  |
| --- | --- |
| orderId | The unique identifier for the entry order |

## Examples

```csharp
protected override void OnBarUpdate()
{
    // ATM strategy methods only work during real-time
    if (State != State.Realtime)
        return;
    string[] entryOrder = GetAtmStrategyEntryOrderStatus("orderId");
    // checks if the entry order exists
    // and the order state is not already cancelled/filled/rejected
    if (entryOrder.Length > 0 && entryOrder[2] == "Working")
    {
        AtmStrategyCancelEntryOrder("orderId");
    }
}
```


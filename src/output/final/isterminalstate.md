---
title: "IsTerminalState()"
pathName: /docs/desktop/isterminalstate
---

## Definition

A static method used to determine if an order's OrderState is considered terminal and no longer active.

{% callout type="note" %}
This is a static method and is compared against an order state, NOT the order itself. Please see the example below for correct syntax and usage.
{% /callout %}

## Method Return Value

A `bool` value which will return true when an `OrderState` is equal to `OrderState.Cancelled`, `OrderState.Filled`, `OrderState.Rejected`, `OrderState.Unknown`; otherwise false.

## Syntax

```csharp
IsTerminalState(OrderState orderState)
```

## Parameters

|  |  |
| --- | --- |
| orderState | The `OrderState` to compare |

## Examples

```csharp
private Order entryOrder = null;

protected override void OnBarUpdate()
{
    // submit order under valid condition
    // note that the order assignment and handling is done in OnOrderUpdate()
    if (entryOrder == null && Close[0] > Open[0])
        EnterLongLimit(Close[0] - 1, "myEntryOrder");
}

protected override void OnOrderUpdate(Order order, double limitPrice, double stopPrice, int quantity, int filled, double averageFillPrice, OrderState orderState, DateTime time, ErrorCode error, string nativeError)
{
    // assign incoming order
    if (entryOrder == null)
    {
        // check that order matches by signal name, that order is not in terminal state
        if (order.Name == "myEntryOrder" && !Order.IsTerminalState(order.OrderState))
            entryOrder = order;
    }

    if (entryOrder != null && entryOrder == order)
    {
        // set "entryOrder" to null if it is Cancelled, Filled, Rejected, Unknown
        if (Order.IsTerminalState(entryOrder.OrderState))
            entryOrder = null;
    }
}
```

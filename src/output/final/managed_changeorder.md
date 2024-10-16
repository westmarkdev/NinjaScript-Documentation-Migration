---
title: "ChangeOrder()"
pathName: /docs/desktop/changeorder
---

## Definition

Amends a specified [Order](/docs/desktop/order).

{% callout type="note" %}
This method is only relevant for Managed orders with IsLiveUntilCancelled set to true and Unmanaged orders.
{% /callout %}

## Syntax

```csharp
ChangeOrder(Order order, int quantity, double limitPrice, double stopPrice)
```

{% callout type="warning" %}
If you have existing historical [Order](/docs/desktop/order) references which have transitioned to real-time, you MUST update the order object reference to the newly submitted real-time order; otherwise errors may occur as you attempt to change the order. You may use the [GetRealtimeOrder()](/docs/desktop/getrealtimeorder) helper method to assist in this transition.
{% /callout %}

## Parameters

|  |  |
| --- | --- |
| order | [Order object](/docs/desktop/order) of the order you wish to amend |
| quantity | Order quantity |
| limitPrice | Order limit price. Use "0" should this parameter be irrelevant for the OrderType being submitted. |
| stopPrice | Order stop price. Use "0" should this parameter be irrelevant for the OrderType being submitted. |

## Examples

```csharp
private Order stopOrder = null;
protected override void OnBarUpdate()
{
    // Raise stop loss to breakeven when you are at least 4 ticks in profit
    if (stopOrder != null && stopOrder.StopPrice < Position.AveragePrice && Close[0] >= Position.AveragePrice + 4 * TickSize)
        ChangeOrder(stopOrder, stopOrder.Quantity, 0, Position.AveragePrice);
}
```

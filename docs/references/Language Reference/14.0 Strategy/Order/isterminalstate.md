---
title: IsTerminalState()
pathName: isterminalstate
parent: order
section: references
status: imported
---

## Definition

A static method used to determine if the an order's **OrderState** is considered terminal and no longer active.

{% callout type="note" %}

This is a static method and is compared against an order state, NOT the order itself. Please see the example below for correct syntax and usage.

{% /callout %}

## Method Return Value

A bool value which will return true when an **OrderState** is equal to **OrderState.Cancelled**, **OrderState.Filled**, **OrderState.Rejected**, **OrderState.Unknown**; otherwise false.

## Syntax

**IsTerminalState(OrderState orderState)**

## Parameters

{% table %}

* **Parameter**
* **Description**

---

* **orderState**
* The **OrderState** to compare

{% /table %}

## Examples

```csharp
private Order entryOrder = null;
protected override void OnBarUpdate()
{
if (entryOrder == null && Close[0] > Open[0])
 EnterLongLimit(Close[0] - 1, "myEntryOrder");
}

protected override void OnOrderUpdate(Order order, double limitPrice, double stopPrice, int quantity, int filled, double averageFillPrice, OrderState orderState, DateTime time, ErrorCode error, string nativeError)
if (entryOrder == null)

if (order.Name == "myEntryOrder" && !Order.IsTerminalState(order.OrderState))
 entryOrder = order;

if (entryOrder != null && entryOrder == order)
 if (Order.IsTerminalState(entryOrder.OrderState))
  entryOrder = null;
```

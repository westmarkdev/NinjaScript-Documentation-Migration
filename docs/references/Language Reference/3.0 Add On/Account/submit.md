---
title: Submit()
pathName: submit
parent: account
section: references
status: imported
---

## Definition

Submits specified **Order** object(s).

## Syntax

**Submit(IEnumerable<`order`> orders)**

## Parameters

{% table %}

* Parameter
* Description

---

* **orders**
* Order(s) to submit
{% /table %}

## Examples

```csharp
Order stopOrder = null;  
stopOrder = myAccount.CreateOrder(myInstrument, OrderAction.Sell, OrderType.StopMarket, TimeInForce.Day, 1, 0, 1400, "myOCO", "stopOrder", null);  
myAccount.Submit(new[] { stopOrder });
```

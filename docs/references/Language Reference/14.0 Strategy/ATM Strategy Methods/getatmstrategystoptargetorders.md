---
title: GetAtmStrategyStopTargetOrderStatus()
pathName: getatmstrategystoptargetorderstatus
parent: atm_strategy_methods
section: references
status: imported
---

## Definition

Gets the current order state(s) of the specified stop or target order of a still-active ATM strategy.

{% callout type="note" %}

Notes:  

1. If the method can't find the specified order(s), an empty array is returned.  
2. A specified stop or target within an ATM strategy can actually hold multiple orders. For example, if your ATM strategy submits a stop and target and you receive multiple partial fills on entry with a delay of a few seconds or more between entry fills, the ATM strategy will submit stop and target orders for each partial fill all with the same price and order type.
{% /callout %}

## Method Return Value

A string[,] multi-dimensional array holding three dimensions that represent average fill price, filled amount and **order state**. The length (number of elements) represents the number of orders that represent the specified name.

## Syntax

**GetAtmStrategyStopTargetOrderStatus(string orderName, string atmStrategyId)**

## Parameters

{% table %}

---

* **orderName**
* The order name such as "Stop1" or "Target2"

---

* **atmStrategyId**
* The unique identifier for the ATM strategy
{% /table %}

## Examples

```csharp
protected override void OnBarUpdate()
{
     string[,] orders = GetAtmStrategyStopTargetOrderStatus("Target1", "idValue");

     // Check length to ensure that returned array holds order information
     if (orders.Length > 0)
     {
         for (int i = 0; i < orders.GetLength(0); i++)
         {
               Print("Average fill price is " + orders[i, 0].ToString());
               Print("Filled amount is " + orders[i, 1].ToString());
               Print("Current state is " + orders[i, 2].ToString());
         }
     }
}
```

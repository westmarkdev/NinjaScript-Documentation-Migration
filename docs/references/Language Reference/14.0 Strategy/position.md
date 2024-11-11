---
title: Position
pathName: position
parent: strategy
section: references
status: imported
---

## Definition

Represents position related information that pertains to an instance of a strategy.

{% callout type="note" %}

Tips:

* For multi-instrument scripts, please see **Positions** object which holds an array of all instrument positions managed by the strategy's account.
* For a real-world Account Position, please see **PositionAccount**.
{% /callout %}

## Methods and Properties

{% table %}

* Property
* Description

---

* **Account**
* An **Account** object which corresponds to the position

---

* **AveragePrice**
* Gets the average entry price of the strategy position

---

* **GetUnrealizedProfitLoss()**
* Gets the unrealized PnL

---

* **Instrument**
* An **Instrument** value representing the instrument of an order

---

* **MarketPosition**
* Gets the current market position
  * Possible values:
    * **MarketPosition.Flat**
    * **MarketPosition.Long**
    * **MarketPosition.Short**

---

* **Quantity**
* Gets the current position size

---

* **ToString()**
* A string representation of a position
{% /table %}

## Examples

```csharp
protected override void OnBarUpdate()
{
     // Print out the average entry price
     Print("The average entry price is " + Position.AveragePrice);
}
```

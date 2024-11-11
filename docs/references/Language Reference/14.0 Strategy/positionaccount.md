---
title: PositionAccount
pathName: positionaccount
parent: strategy
section: references
status: imported
---

## Definition

Represents position related information that pertains to real-world account (live or simulation).

{% callout type="note" %}

Tips:

* For multi-instrument scripts, please see **PositionsAccount** object which holds an array of all instrument positions managed by the strategy's account.
* For a Strategy Position, please see **Position**.
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
* Gets the average entry price of the account position

---

* **GetUnrealizedProfitLoss()**
* Gets the unrealized PnL for the account

---

* **Instrument**
* An **Instrument** value representing the instrument of an order

---

* **MarketPosition**
* Gets the current market position of the account
  * Possible values:
    * **MarketPosition.Flat**
    * **MarketPosition.Long**
    * **MarketPosition.Short**

---

* **Quantity**
* Gets the current account position size

---

* **ToString()**
* A string representation of an account position
{% /table %}

## Examples

```csharp
protected override void OnBarUpdate()
{
    // Print out the average entry price
    Print("The average entry price is " + PositionAccount.AveragePrice);
}
```

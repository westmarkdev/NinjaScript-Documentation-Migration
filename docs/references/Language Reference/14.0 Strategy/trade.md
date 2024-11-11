---
title: Trade
pathName: trade
parent: strategy
section: references
status: imported
---

## Definition

A Trade is a completed buy/sell or sell/buy transaction. It consists of an entry and exit execution.

{% table %}

* Example 1
* Example 2

---

* Buy 1 contract at a price of 1000 and sell 1 contract at a price of 1001 is one complete trade.
* Buy 2 contracts at a price of 1000 and sell the 1st contract at a price of 1001, then sell the 2nd contract at a price of 1002 are two completed trades.
{% /table %}

In the second example above, two trade objects are created to represent each individual trade. Each trade object will hold the same entry execution for two contracts since this single execution was the opening execution for both individual trades.

## Methods and Properties

{% table %}

---

* Commission
* A **double** value representing the commission of the trade

---

* Entry
* Gets an **Execution** object representing the entry

---

* EntryEfficiency
* A **double** value representing the entry efficiency of the trade

---

* Exit
* Gets an **Execution** object representing the exit

---

* ExitEfficiency
* A **double** value representing the exit efficiency of the trade

---

* MaeCurrency
* A **double** value representing max adverse excursion in currency

---

* MaePercent
* A **double** value representing max adverse excursion as a percentage

---

* MaePips
* A **double** value representing max adverse excursion in pips

---

* MaePoints
* A **double** value representing max adverse excursion in points

---

* MaeTicks
* A **double** value representing max adverse excursion in ticks

---

* MfeCurrency
* A **double** value representing max favorable excursion in currency

---

* MfePercent
* A **double** value representing max favorable excursion as a percentage

---

* MfePips
* A **double** value representing max favorable excursion in pips

---

* MfePoints
* A **double** value representing max favorable excursion in points

---

* MfeTicks
* A **double** value representing max favorable excursion in ticks

---

* ProfitCurrency
* A **double** value representing profit quoted in currency.

---

* ProfitPercent
* A **double** value representing profit as a percentage

---

* ProfitPips
* A **double** value representing profit in pips

---

* ProfitPoints
* A **double** value representing profit in points

---

* ProfitTicks
* A **double** value representing profit in ticks

---

* Quantity
* An **int** value representing the quantity of the trade

---

* TotalEfficiency
* A **double** value representing the total efficiency of the trade

---

* TradeNumber
* An **int** value representing the trade number by the sequence it occurred

---

* ToString()
* A string representation of the Trade object
{% /table %}

## Examples

```csharp
{
   if (SystemPerformance.RealTimeTrades.Count > 0)
   {
       // Check to make sure there is at least one trade in the collection
       Trade lastTrade = SystemPerformance.RealTimeTrades[SystemPerformance.RealTimeTrades.Count - 1];

       // Calculate the PnL for the last completed real-time trade
       double lastProfitCurrency = lastTrade.ProfitCurrency;

       // Store the quantity of the last completed real-time trade
       double lastTradeQty = lastTrade.Quantity;

       // Print the PnL to the NinjaScript Output window
       Print("The last trade's profit in currency is " + lastProfitCurrency);
       // The trade profit is quantity aware, we can easily print the profit per traded unit as well
       Print("The last trade's profit in currency per traded unit is " + (lastProfitCurrency / lastTradeQty));
   }
}
```

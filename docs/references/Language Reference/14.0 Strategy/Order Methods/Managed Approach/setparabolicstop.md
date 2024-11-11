---
section: references
status: double_check
parent: managed_approach
title: SetParabolicStop()
pathName: setparabolicstop
lg2m: true
---

## Definition

Generates a parabolic type trail stop order with the signal name **Parabolic stop** to exit a position. Parabolic stops are amended on a bar update basis, so dependent upon the [Calculate](calculate) setting of the parent strategy. Parabolic stop orders are real working orders (unless simulated is specified in which case the stop order is locally simulated and submitted as market once triggered) submitted immediately to the market upon receiving an execution from an entry order.

Although logic wise very similar, this technique works different from the [ParablicSAR](parabolic_sar) indicator. The indicator will provide trailing stop levels 'always in the market' assuming a constant market position switch, either long or short (reversing). The **SetParabolicStop()** method in contrast will apply the same parabolic trailing technique sensitive to price acceleration to the custom strategy entry signal / position it is associated with.

{% callout type="note" %}

Notes:

* The **SetParabolicStop()** method can NOT be used concurrently with the [SetStopLoss()](setstoploss) or [SetTrailStop()](settrailstop) method for the same position, if any of methods are called for the same position (fromEntrySignal) the [SetStopLoss()](setstoploss) will always take precedence. You can however, use all three methods in the same strategy if they reference different signal names.
* Parabolic stop orders are submitted in real-time on incoming executions from entry orders.
* Since they are submitted upon receiving an execution, the **Set** method should be called prior to submitting the associated entry order to ensure an initial level is set.
* A strategy will either generate a trail stop order for each partial fill of an entry order or one order for all fills. See additional information under the [Strategies](options_strategies) tab of the Options dialog window.
* If a [profit target](setprofittarget) order is generated in addition to a trail stop order, they are submitted as OCO (one cancels other).
* Parabolic stop orders are submitted as stop-market orders.
* A parabolic stop order is automatically canceled if the managing position is closed by another strategy generated exit order.
* Should you have multiple Bars objects of the same instrument while using **SetParabolicStop()** in your strategy, you should only submit orders for this instrument to the first Bars context of that instrument. This is to ensure your order logic is processed correctly and any necessary order amendments are done properly.
* Parabolic stop orders are modified based on the strategies 'Calculate' settings. In the case of 'Calculate' on bar close, when the bar closes the parabolic stop order modification will occur using the closing price of the bar as the reference price to apply the trail offset. Subsequently if the open price of the next bar is significantly higher or lower than the current close price then there is a possibility that the calculated parabolic stop price is now an invalid stop price. This is a risk with modifying any stop order closer to the current market price since any modification above/below the current price would be rejected.
{% /callout %}

## Syntax

**SetParabolicStop(CalculationMode mode, double value)**

**SetParabolicStop(string fromEntrySignal, CalculationMode mode, double value, bool isSimulatedStop, double acceleration, double accelerationMax, double accelerationStep)**

{% callout type="warning" %}

* This method CANNOT be called from the [OnStateChange()](onstatechange) method during State.SetDefaults.
* CalculationMode.Price is irrelevant for trail stops. Attempting to use this mode will log a message and the stop order be ignored. Please use [SetStopLoss()](setstoploss) for this mode instead.
{% /callout %}

## Parameters

{% table %}

* Parameter
* Description

---

* **mode**
* Determines the manner in which the value parameter is calculated. Possible values are:
  * **CalculationMode.Currency**: Initial PnL away from average entry. Calculated by the dollar per tick value for the order quantity used. When this mode is used, [StopTargetHandling](stoptargethandling) will automatically be set to ByStrategyPosition. The Stop loss will then continue to update following each parabolic step.
  * **CalculationMode.Percent**: Percentage away from the average entry, based on the average entry price.
  * **CalculationMode.Pips**: Pips away from average entry.
  * **CalculationMode.Ticks**: Ticks away from entry average entry.
  * Please note in percentage calculation mode a value of 1 is equal to 100%, a value of 0.1 is equal to 10%, and a value of 0.01 will be 1%.

---

* **isSimulatedStop**
* If true, will simulate the stop order and submit as market once triggered.

---

* **value**
* The value the trail stop order is offset from the position entry price.

---

* **fromEntrySignal**
* The entry signal name. This ties the trail stop exit to the entry and exits the position quantity represented by the actual entry. Using an empty string will attach the exit order to all entries.

---

* **acceleration**
* Sets the acceleration value.

---

* **accelerationMax**
* Sets the maximum acceleration value.

---

* **accelerationStep**
* Sets the step value used to increment acceleration value.
{% /table %}

{% callout type="note" %}

Tips (also see [Overview](managed_approach)):

* It is suggested to call this method from within the strategy [OnStateChange()](onstatechange) method if your stop loss price/offset is static.
* You may call this method from within the strategy [OnBarUpdate()](onbarupdate) method should you wish to dynamically change the stop loss price while in an open position.
* Should you call this method to dynamically change the stop loss price in the strategy [OnBarUpdate()](onbarupdate) method, you should always reset the stop loss price / offset value when your strategy is flat otherwise, the last price/offset value set will be used to generate your stop loss order on your next open position.
* The signal name generated internally by this method is **Parabolic stop** which can be used with various methods such as [BarsSinceExitExecution()](barssinceexitexecution), or other order concepts which rely on identifying a signal name.
{% /callout %}

## Examples

```csharp
protected override void OnStateChange()
{
     if (State == State.Configure)
     {
         // Sets a parabolic stop using default acceleration (0.02), accelerationMax (0.2), accelerationStep (0.02) settings and a floor value of 12 ticks
         SetParabolicStop(CalculationMode.Ticks, 12);

         // Sets a parabolic stop of with a currency floor of 500 
         SetParabolicStop("MyLongEntry", CalculationMode.Currency, 500, false, 0.03, 0.3, 0.01);
     }
}
```

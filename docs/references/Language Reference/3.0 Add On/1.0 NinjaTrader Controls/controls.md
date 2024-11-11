---
title: NinjaTrader Controls
pathName: ninjatrader_controls
parent: controls
section: references
status: removed
---

## NinjaTrader Controls

The following section contains controls that are native **NinjaTrader** controls. To fully integrate your Add On within **NinjaTrader** it is recommended to use these controls as opposed to building your own when possible.

{% callout type="note" %}

For cleaning up these resources, please see the **NTTabPage.Cleanup()** method.
{% /callout %}

{% table %}

* Control
* Description

---

* [AccountSelector](accountselector)
* AccountSelector can be used as a UI element users can interact with for selecting accounts.

---

* [AtmStrategySelector](atmstrategyselector)
* AtmStrategySelector is a UI element users can interact with for selecting ATM Strategies.

---

* [InstrumentSelector](instrumentselector)
* InstrumentSelector is a UI element users can interact with for selecting instruments. This can be used with instrument linking between windows.

---

* [IntervalSelector](intervalselector)
* IntervalSelector is a UI element users can interact with for selecting intervals. This can be used with interval linking between windows.

---

* [TifSelector](tifselector)
* TifSelector can be used as a UI element users can interact with for selecting TIF.

---

* [QuantityUpDown](quantityupdown)
* QuantityUpDown can be used as a UI element users can interact with for selecting quantity.
{% /table %}

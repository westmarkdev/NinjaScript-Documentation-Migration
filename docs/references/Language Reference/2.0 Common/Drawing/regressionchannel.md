---
title: RegressionChannel
pathName: regressionchannel
parent: drawing
section: references
status: review
---

## Definition

Represents an interface that exposes information regarding a Regression Channel **IDrawingTool**.

## Methods and Properties

{% table %}

* Parameter

* Description

---

* StartAnchor

* An **IDrawingTool's ChartAnchor** representing the starting point of the drawing object

---

* EndAnchor

* An **IDrawingTool's ChartAnchor** representing the starting point of the drawing object

---

* RegressionStroke

* The **Stroke** object used to draw the middle line of the object

---

* LowerChannelStroke

* The **Stroke** object used to draw the lower line of the object

---

* UpperChannelStroke

* The **Stroke** object used to draw the upper line of the object

---

* PriceType

* Possible values are:

  * **PriceType.Close**

  * **PriceType.High**

  * **PriceType.Low**

  * **PriceType.Median**

  * **PriceType.Open**

  * **PriceType.Typical**

---

* ChannelType

* An enum value representing if the object will use standard deviations calculations for the upper/lower lines. Possible values are:

* **RegressionChannelType.Segment**

* **RegressionChannelType.StandardDeviation**

---

* ExtendLeft

* A bool value representing if the object will extend to the left

---

* ExtendRight

* A bool value representing if the object will extend to the right

---

* StandardDeviationLowerDistance

* A double value representing the standard deviation distance to the lower line

---

* StandardDeviationUpperDistance

* A double value representing the standard deviation distance to the upper line

---

{% /table %}

## Examples

```csharp
// Instantiate a RegressionChannel object
NinjaTrader.NinjaScript.DrawingTools.RegressionChannel myRegChan = Draw.RegressionChannel(this, "tag1", 10, 0, Brushes.Blue);

// Change the object's PriceType
myRegChan.PriceType = PriceType.Median;
```

{% callout type="note" %}

To differentiate between **DrawingTools.RegressionChannel** and **Indicators.RegressionChannel** when assigning a RegressionChannel object, you will need to invoke the former path explicitly, as seen in the example above.

{% /callout %}

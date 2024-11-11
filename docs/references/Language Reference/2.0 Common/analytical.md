---
title: Analytical
pathName: analytical
parent: common
section: references
aliases:
  - market_data
status: review
---

NinjaScript provides a number of methods and properties useful for analyzing and identifying specific conditions within **Series`<t>`** collections. Some of these methods test a condition and return true or false, while others return an int-based bar index or other numerical value. A list of analytical methods can be found below:

{% table %}

* Methods and Properties
* Description

---

* [CountIf()](countif)
* Counts the number of occurrences of the test condition

---

* [CrossAbove()](crossabove)
* Evaluates a cross above condition

---

* [CrossBelow()](crossbelow)
* Evaluates a cross below condition

---

* [GetCurrentAsk()](getcurrentask)
* Returns the current Ask price

---

* [GetCurrentAskVolume()](getcurrentaskvolume)
* Returns the current Ask volume

---

* [GetCurrentBid()](getcurrentbid)
* Returns the current Bid price

---

* [GetCurrentBidVolume()](getcurrentbidvolume)
* Returns the current Bid volume

---

* [GetMedian()](getmedian)
* Returns the median value of the specified series

---

* [HighestBar()](highestbar)
* Returns the number of bars ago the highest price value occurred

---

* [IsFalling()](falling)
* Evaluates a falling condition

---

* [IsRising()](rising)
* Evaluates a rising condition

---

* [Least Recent Occurrence (LRO)](least_recent_occurence_lro)
* Returns the number of bars ago that the least recent occurrence of a test condition evaluated to true

---

* [LowestBar()](lowestbar)
* Returns the number of bars ago the lowest price value occurred

---

* [Most Recent Occurrence (MRO)](most_recent_occurrence_mro.md)
* Returns the number of bars ago that the most recent occurrence of a test condition evaluated to true

---

* [Slope()](slope)
* Returns a measurement of the steepness of a price series measured by the change over time

---

* [TickSize](ticksize)
* The value of 1 tick for the corresponding instrument

---

* [ToDay()](today)
* Calculates an integer value representing a date

---

* [ToTime()](totime)
* Calculates an integer value representing a time
{% /table %}

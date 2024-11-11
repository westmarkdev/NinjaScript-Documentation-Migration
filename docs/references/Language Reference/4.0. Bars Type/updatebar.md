---
title: UpdateBar()
pathName: updatebar
parent: bars_type
status: imported
section: references
---


## Definition

Updates a data point in our Bars Type.

## Syntax

**UpdateBar(Bars bars, double high, double low, double close, DateTime time, long volumeAdded)**

## Parameters

{% table %}

---

* bars
* The Bars object of your bars type

---

* high
* A double value representing the high price  

---

* low
* A double value representing the low price

---

* close  
* A double value representing the close price

---

* time
* A DateTime value representing the time

---

* volume
* A long value representing the volume

---

{% /table %}

## Examples

```csharp
UpdateBar(bars, high, low, close, time, volume);
```

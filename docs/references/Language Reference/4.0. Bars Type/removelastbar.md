---
title: RemoveLastBar()
pathName: removelastbar
parent: bars_type
status: imported
section: references
---

## Definition

Removes the last data point for the Bars Type. There may be cases where your custom bar type may need to amend the last values added on a bar that has already closed. Calling **RemoveLastBar()** will remove the last points for that bar type and allow you to call **AddBar()** with the updated values.

{% callout type="note" %}

* In order to use this method, the [**IsRemoveLastBarSupported**](isremovelastbarsupported) method must be true.
* **RemoveLastBar()** CANNOT be used with [**TickReplay**](tick_replay)
{% /callout %}

## Syntax

**RemoveLastBar(Bars bars)**

## Parameters

{% table %}

* Parameter
* Description

---

* **bars**
* The Bars object of your bars type
{% /table %}

## Examples

```csharp
RemoveLastBar(bars);
```

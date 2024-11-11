---
title: AttachedTo
pathName: attachedto
parent: drawing_tools
status: imported
section: references
---

## Definition

An object which holds information regarding where the drawing tool is attached.

## Available Properties

{% table %}

* Name

* Description

---

* AttachedToType

* An enum representing the type of object the drawing tool is attached. Possible values are:

* Bars - The chart bars of the parent chart

* GlobalInstrument - The bars of an instrument across all charts

* Indicator - A NinjaScript indicator

* Strategy - A NinjaScript strategy

---

* ChartObject

* A ChartObject interface such as an indicator, strategy, chart bars

---

* DisplayName

* A **string** value indicating the name of the object the drawing tool is attached

---

* Instrument

* The Instrument that the drawing tool is attached

---

{% /table %}

## Syntax

**AttachedTo**

## Examples

```csharp

if (AttachedTo.AttachedToType == AttachedToType.Indicator)
   // do something

```

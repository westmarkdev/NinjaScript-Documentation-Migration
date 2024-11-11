---
title: RearmAlert()
pathName: rearmalert
parent: alert_and_debug_concepts
section: references
status: imported
---

## Definition

Rearms an existing alert event by the string "id" parameter created via the [AlertCallback()](alertcallback) method. A NinjaScript generated alert by may need to be rearmed after the alert is triggered depending on the Alert()'s rearmSeconds parameter.

{% callout type="note" %}

The NinjaScriptBase has a non-static method implemented with the same name. Please see the [RearmAlert()](rearmalert) method for Indicator or Strategies.

{% /callout %}

## Method Return Value

This method does not return a value.

## Syntax

**NinjaTrader.NinjaScript.Alert.RearmAlert(string id)**

## Parameters

{% table %}

* id

---

* A unique string id representing an alert id to reset
{% /table %}

## Examples

```csharp
if (resetCondition) 
{
   NinjaTrader.NinjaScript.Alert.ResetAlertRearmById("someId");
   resetCondition = false;
}
```

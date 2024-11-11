---
title: RearmAlert()
pathName: rearmalert
parent: alert_debug_share
section: references
status: review
---

## Definition

Rearms an alert created via the **Alert()** method.

{% callout type="note" %}

A NinjaScript generated alert may need to be rearmed after the alert is triggered depending on the **Alert()** method's **rearmSeconds** parameter.

{% /callout %}

## Method Return Value

This method does not return a value.

## Syntax

**RearmAlert(string id)**

## Parameters

{% table %}

* Parameter
* Description

---

* id
* A unique string id representing an alert id to rearm
{% /table %}

## Examples

```csharp
protected override void OnBarUpdate()
{
   //rearms "myAlert" on each new trading session
   if(Bars.IsFirstBarOfSession)
     RearmAlert("myAlert");
}
```

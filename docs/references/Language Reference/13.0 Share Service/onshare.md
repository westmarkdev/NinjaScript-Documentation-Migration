---
title: OnShare()
pathName: onshare
parent: share_service
status: imported
section: references
---

## Definition

This method is called when the user clicks OK on the Share window in **NinjaTrader**. This method can also be called by Alerts and general **NinjaScript** objects.

## Method Return Value

This method does not return a value.

## Parameters

{% table %}

---

* **text**
* The message being sent to the social network or other Share provider. This is what appears in the textbox of the Share window.

---

* **imageFilePath**
* Optional path to screenshot or other image to be sent to the social network or other Share provider.
{% /table %}

## Syntax

You must override the method in your Share Service with the following syntax.

**public override void OnShare(string text, string imageFilePath)**

## Examples

```csharp
public override void OnShare(string text, string imgFilePath)
{
  // place your share service logic here
}
```

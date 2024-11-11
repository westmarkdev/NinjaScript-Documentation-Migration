---
title: SetPropertyName()
pathName: setpropertyname_chartstyle
parent: chart_style
status: changed
section: references
lg2m:
---

## Definition

Sets a default property name to a custom string to be displayed on the UI.

## Method Return Value

This method does not return a value.

## Syntax

**SetPropertyName(string propertyName, string displayName)**

## Method Parameters

{% table %}

* propertyName
* displayName

---

* A string representing the property to be renamed. Possible values include:
  * **UpBrush**
  * **DownBrush**
  * **BarWidth**
  * **Stroke**
  * **Stroke2**
* A string representing the desired property name
{% /table %}

## Examples

```csharp
protected override void OnStateChange()
{
   if (State == State.Configure)
   {
       Properties.Remove(Properties.Find("Stroke", true));
       Properties.Remove(Properties.Find("Stroke2", true));

       SetPropertyName("UpBrush", "AdvanceBar");
       SetPropertyName("DownBrush", "DeclineBar");
   }
}
```

{% callout type="note" %}

If you do not wish to use specific properties accessible via **SetPropertyName**(), you will need to remove them from the list via **Properties.Remove**, as shown in the example above.

{% /callout %}

---
title: Icon
pathName: icon_chartstyle
parent: chart_style
status: changed
section: references
---

## Definition

The shape which displays next to the Chart Style menu item. Since this is a standard object, any type of icon can be used (unicode characters, custom image file resource, geometry path, etc).

For more information on using images to create icons, see the [Using Images with Custom Icons](using_images_and_geometry_with_custom_icons).

{% callout type="note" %}

When using **UniCode** characters, first ensure that the desired characters exist in the icon pack for the font family used in **NinjaTrader**.

{% /callout %}

## Property Value

A generic virtual object representing the drawing tools menu icon. This property is read-only.

## Syntax

You must override this property using the following syntax:

```csharp
public override object Icon
```

## Examples

```csharp

public override object Icon
{
   get
   {
     //use a unicode character as our string which will render an arrow
     string uniCodeArrow = "\u279A";
     return uniCodeArrow;
   }
}
```

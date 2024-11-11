---
title: SimpleFont
pathName: simplefont
parent: common
section: references
status: review
---

## Definition

Defines a particular font configuration.

{% callout type="note" %}

Note: SimpleFont objects are used for various **Drawing** methods, and can be used when defining UI element for Add-ons.

{% /callout %}

## Constructors

{% table %}

---

* **SimpleFont()**
* Creates a SimpleFont object using a family name of "Arial" and a size of "12"

---

* **SimpleFont(string familyName, int size)**
* Creates a SimpleFont object using the specified family name and size
{% /table %}

## Methods and Properties

{% table %}

---

* **Bold**
* A bool value determining if the Font is bold style

---

* **Family**
* A [FontFamily](fontfamily) representing a family of Fonts

---

* **Italic**
* A bool value determining if the Font is italic style

---

* **Size**
* A **double** value determining the size of font in WPF units (please see the tip below)

---

* **Typeface**
* A [Typeface](typeface) used to represent the variation of the font used

---

* **ApplyTo()**
* Applies a custom [SimpleFont](simplefont) object's properties (family, size, and style) to a [Windows Control](windowscontrol)

---

* **ToDirectWriteTextFormat()**
* Converts a SimpleFont object to a SharpDX compatible font which can be used for chart rendering.
{% /table %}

{% callout type="note" %}

The WPF unit used is the default px one, so device independent pixels. With a default system DPI setting of 96, the physical pixel on the screen would be identical in size, but can vary if a custom DPI is employed. Both should not be confused with the points based font sizing known from other familiar Windows applications like Word, the advantage here is that the non points based size measurement will increase / decrease in size if the system DPI is changed - a more detailed discussion is located [here](https://blogs.msdn.microsoft.com/text/2009/12/11/wpf-text-measurement-units/).

{% /callout %}

## Examples

```csharp
// create custom Courier New, make it big and bold
NinjaTrader.Gui.Tools.SimpleFont myFont = new NinjaTrader.Gui.Tools.SimpleFont("Courier New", 12) { Size = 50, Bold = true };

Draw.Text(this, "myTag", false, "Hi There!", 0, Low[0], 5, Brushes.Blue, myFont, TextAlignment.Center, Brushes.Black, null, 1);
```
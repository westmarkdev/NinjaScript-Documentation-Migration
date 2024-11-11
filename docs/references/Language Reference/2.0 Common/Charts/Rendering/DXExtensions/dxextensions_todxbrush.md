---
title: ToDxBrush()
pathName: todxbrush
parent: rendering
section: references
status: imported
---

## Definition

Converts a WPF Brush to a SharpDX Brush used for **SharpDX rendering**. Supports **SolidColorBrush**, **LinearGradientBrush**, and **RadialGradientBrush** types.

{% callout type="note" %}

If you are using a large number of brushes, and are not tied to WPF resources, you should favor creating the SharpDX Brush directly since the ToDxBrush() method can lead to performance issues if called too frequently during a single render pass.

{% /callout %}

## Method Return Value

A new **SharpDX.Direct2D1.Brush** constructed colors and brush properties of the WPF brush.

## Syntax

**DxExtensions.ToDxBrush(this System.Windows.Media.Brush brush, RenderTarget renderTarget)**  

**<`wpfbrush`>.ToDxBrush(RenderTarget renderTarget)**

## Parameters

{% table %}

---

* brush
* The **System.Windows.Media.Brush** to convert

---

* renderTarget
* The **RenderTarget** associated with the brush resource
{% /table %}

## Examples

```csharp
protected override void OnStateChange()
{
    if (State == State.SetDefaults)
    {
        Name = "Example ToDXBrush";

        // pushes the WPF brush to the UI for user to configure
        TextBrush = System.Windows.Media.Brushes.DodgerBlue;
    }
}

protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
    // convert user WPF selection to a DX brush
    SharpDX.Direct2D1.Brush dxBrush = TextBrush.ToDxBrush(RenderTarget);

    using (dxBrush)
    {
        RenderTarget.FillRectangle(new RectangleF(ChartPanel.X, ChartPanel.Y, ChartPanel.W, ChartPanel.H), dxBrush);
    }
}

// the WPF exposed to the UI which the user defines
[XmlIgnore]
public System.Windows.Media.Brush TextBrush { get; set; }

[Browsable(false)]
public string TextBrushSerialize
{
    get { return Serialize.BrushToString(TextBrush); }
    set { TextBrush = Serialize.StringToBrush(value); }
}
```

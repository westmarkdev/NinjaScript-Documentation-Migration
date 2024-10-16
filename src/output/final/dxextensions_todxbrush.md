---
title: "ToDxBrush()"
pathName: /docs/desktop/dxextensions_todxbrush
---

## Definition

Converts a WPF Brush to a SharpDX Brush used for [SharpDX rendering](/docs/desktop/using_sharpdx_for_custom_chart_rendering). Supports SolidColorBrush, LinearGradientBrush, and RadialGradientBrush types.

{% callout type="note" %}
If you are using a large number of brushes, and are not tied to WPF resources, you should favor creating the SharpDX Brush directly since the ToDxBrush() method can lead to performance issues if called too frequently during a single render pass.
{% /callout %}

## Method Return Value

A new [SharpDX.Direct2D1.Brush](/docs/desktop/sharpdx_direct2d1_brush) constructed with the colors and brush properties of the WPF brush.

## Syntax

```csharp
DxExtensions.ToDxBrush(this System.Windows.Media.Brush brush, RenderTarget renderTarget)
```

```csharp
<wpfbrush>.ToDxBrush(RenderTarget renderTarget)
```

## Parameters

|  |  |
| --- | --- |
| brush | The [System.Windows.Media.Brush](https://msdn.microsoft.com/en-us/library/system.windows.media.brush(v=vs.110).aspx) to convert |
| renderTarget | The [RenderTarget](/docs/desktop/rendertarget) associated with the brush resource |

## Example

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


---
title: "NTMessageBoxSimple.Show()"
pathName: /docs/desktop/ntmessageboxsimple_show
---

## Definition

Creates a message box window.

{% callout type="note" %}
For more information on using MessageBox windows, please see [Microsoft .NET MessageBox Class Documentation](https://docs.microsoft.com/en-us/dotnet/api/system.windows.messagebox?view=netframework-4.8)
{% /callout %}

## Method Return Value

`MessageBoxResult`; an enum representing the button press used to close the MessageBox window.

## Syntax

```csharp
NTMessageBoxSimple.Show(Window input, string messageTxt, string caption, MessageBoxButton buttonSet, MessageBoxImage icon)
```

## Parameters

| Parameter | Description |
| --- | --- |
| parent | A `Window` (DependencyObject) which represents the owning window. |
| messageTxt | The message body of the MessageBox window. |
| caption | The header of the MessageBox window. |
| buttonSet | A `MessageBoxButton` enum determining the buttons used for the MessageBox window. |
| icon | A `MessageBoxImage` enum determining the icon used for the MessageBox window. |

## Examples

```csharp
// Create a MessageBox window from a Chart
ChartControl.Dispatcher.InvokeAsync(new Action(() => {
    NinjaTrader.Gui.Tools.NTMessageBoxSimple.Show(Window.GetWindow(ChartControl.OwnerChart as DependencyObject), "Message Body", "Message Header", MessageBoxButton.OK, MessageBoxImage.None);
}));
```

```csharp
// Create a MessageBox window from a button press in an AddOn
private void OnMenuItemClick(object sender, RoutedEventArgs e)
{
    NinjaTrader.Gui.Tools.NTMessageBoxSimple.Show(Window.GetWindow(e.Source as DependencyObject), "Message Body", "Message Header", MessageBoxButton.OK, MessageBoxImage.None);
}
```

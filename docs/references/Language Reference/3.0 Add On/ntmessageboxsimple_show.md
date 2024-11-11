---
title: NTMessageBoxSimple.Show()
pathName: ntmessageboxsimple_show
parent: add_on
section: references
status: check
---

## Definition

Creates a message box window.

{% callout type="note" %}

For more information on using MessageBox windows, please see **.NET MessageBox Class Documentation** [here](https://docs.microsoft.com/en-us/dotnet/api/system.windows.messagebox?view=netframework-4.8).

{% /callout %}

## Method Return Value

**MessageBoxResult**; an enum representing the button press used to close the MessageBox window.

## Syntax

**NTMessageBoxSimple.Show(Window input, string messageTxt, string caption, MessageBoxButton buttonSet, MessageBoxImage icon)**

## Parameters

{% table %}

---

* **parent**
* A Window (DependencyObject) which represents the owning window

---

* **messageTxt**
* The message body of the MessageBox window

---

* **caption**
* The header of the MessageBox window

---

* **buttonSet**
* A MesageBoxButton enum determining the buttons used for the MessageBox window

---

* **icon**
* A MesageBoxImage enum determining the icon used for the MessageBox window
{% /table %}

## Examples

```csharp
// Create a MessageBox window from a Chart
ChartControl.Dispatcher.InvokeAsync(new Action(() => {
   NinjaTrader.Gui.Tools.NTMessageBoxSimple.Show(Window.GetWindow(ChartControl.OwnerChart as DependencyObject), "Message Body", "Message Header", MessageBoxButton.OK, MessageBoxImage.None);
}));

// Create a MessageBox window from a button press in an AddOn**
private void OnMenuItemClick(object sender, RoutedEventArgs e)
{
    NinjaTrader.Gui.Tools.NTMessageBoxSimple.Show(Window.GetWindow(e.Source as DependencyObject), "Message Body", "Message Header", MessageBoxButton.OK, MessageBoxImage.None);
```

---
title: "IWorkspacePersistence Interface"
pathName: /docs/desktop/iworkspacepersistence_interface
---

When creating your [NTWindow](/docs/desktop/ntwindow), be sure to implement the IWorkspacePersistence interface as well for the ability to save and restore your window with NinjaTrader workspaces.

{% callout type="note" %}
AddOn Classes which derive from NTWindow or implement IWorkspacePersistence CANNOT be a [nested type](https://msdn.microsoft.com/en-us/library/ms173120.aspx) of another class and MUST have a [default constructor](https://msdn.microsoft.com/en-us/library/ms173115.aspx).
{% /callout %}

This interface contains two methods and one property which must be hidden by the implementing class:

|  |  |
| --- | --- |
| [Restore()](/docs/desktop/iworkspacepersistence_restore) | Restores the window from workspaces. |
| [Save()](/docs/desktop/iworkspacepersistence_save) | Saves the window to workspaces. |
| [WorkspaceOptions](/docs/desktop/workspaceoptions) | Sets required workspace options. |

## Examples

```csharp
public class MyWindow : NTWindow, IWorkspacePersistence
{
    // default constructor
    public MyWindow()
    {
        // Define our NTWindow. If we want to use NT style tabs, we would define that here.
        // WorkspaceOptions property must be set
        Loaded += (o, e) =>
        {
            if (WorkspaceOptions == null)
                WorkspaceOptions = new WorkspaceOptions("MyWindow-" + Guid.NewGuid().ToString("N"), this);
        };
    }

    // IWorkspacePersistence member. Required for restoring window from workspaces
    public void Restore(XDocument document, XElement element)
    {
        if (MainTabControl != null)
            MainTabControl.RestoreFromXElement(element);
    }

    // IWorkspacePersistence member. Required for saving window to workspaces
    public void Save(XDocument document, XElement element)
    {
        if (MainTabControl != null)
            MainTabControl.SaveToXElement(element);
    }

    // IWorkspacePersistence member
    public WorkspaceOptions WorkspaceOptions { get; set; }
}
```


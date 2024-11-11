---
status: double_check
title: WorkspaceOptions
pathName: workspaceoptions
parent: iworkspacepersistence_interface
section: references
lg2m: true
---

## Definition

Sets required workspace options.

{% callout type="note" %}

- The WorkspaceOptions class includes logic for opening, closing, saving, and restoring workspaces, checking windows are off screen, and setting basic properties such as the workspace name and current status.

- A WorkspaceOptions property must simply be declared within your NTWindow, as in the example below. All of its contained logic is taken care of automatically.
{% /callout %}

## Examples

```csharp
// IWorkspacePersistence member

public WorkspaceOptions WorkspaceOptions { get; set; }
```

{% callout type="note" %}

**Tip**: For a complete, working example of this class in use, please download the [AddOn Framework NinjaScript Basic Example](AddOn_Framework_NinjaScript_Basic.zip) to your desktop.

{% /callout %}












 


IWorkspacePersistence Interface







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?iworkspacepersistence_interface.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt;
IWorkspacePersistence Interface | [Previous page](createtabpage.htm)
[Return to chapter overview](add_on.htm)










When creating your [NTWindow](ntwindow.htm), be sure to implement the IWorkspacePersistence interface as well for the ability to save and restore your window with NinjaTrader workspaces. 


 




|  |
| --- |
| Note:  AddOn Classes which derive from NTWindow or implements IWorkspacePersistance CANNOT be a [nested type](https://msdn.microsoft.com/en-us/library/ms173120.aspx) of another class and MUST have a [default constructor](https://msdn.microsoft.com/en-us/library/ms173115.aspx) |



 


 


This interface contains two methods and one property which must be hidden by the implementing class:


 




|  |  |
| --- | --- |
| [Restore()](iworkspacepersistence_restore.htm) | Restores the window from workspaces. |
| [Save()](iworkspacepersistence_save.htm) | Saves the window to workspaces. |
| [WorkspaceOptions](workspaceoptions.htm) | Sets required workspace options.  |




Examples
--------




| ns |
| --- |
| public class MyWindow : NTWindow, IWorkspacePersistence
{
   // default constructor 
   public MyWindow()
     {
         // Define our NTWindow. If we want to use NT style tabs, we would define that here.
          
         // WorkspaceOptions property must be set
          Loaded += (o, e) =&gt;
          {
               if (WorkspaceOptions == null)
                    WorkspaceOptions = new WorkspaceOptions("MyWindow-" + Guid.NewGuid().ToString("N"), this);
          };
     }
 
     // IWorkspacePersistence member. Required for restoring window from workspaces
     public void Restore(XDocument document, XElement)
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
} |






 
 var lastSlashPos = document.URL.lastIndexOf("/") &gt; document.URL.lastIndexOf("\\") ? document.URL.lastIndexOf("/") : document.URL.lastIndexOf("\\");
 if (document.URL.substring(lastSlashPos + 1, lastSlashPos + 4).toLowerCase() != "~hh") {
 if (document.all) setTimeout(function() {
 nsrInit();
 }, 20);
 else nsrInit();
 }
 
 
 $('.sync-toc').show();
 $('p.crumbs').hide();
 }
 
 
 




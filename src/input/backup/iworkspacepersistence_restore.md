










 


Restore()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?iworkspacepersistence_restore.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt; [IWorkspacePersistence Interface](iworkspacepersistence_interface.htm) &gt;
Restore() | [Previous page](iworkspacepersistence_interface.htm)
[Return to chapter overview](iworkspacepersistence_interface.htm)










Restores the window from workspaces.


 



Examples
--------




| ns |
| --- |
| // IWorkspacePersistence member. Required for restoring window from workspaces
public void Restore(XDocument document, XElement)
{
     if (MainTabControl != null)
          MainTabControl.RestoreFromXElement(element);
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
 
 
 




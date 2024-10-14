










 


Save()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?iworkspacepersistence_save.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt; [IWorkspacePersistence Interface](iworkspacepersistence_interface.htm) &gt;
Save() | [Previous page](iworkspacepersistence_restore.htm)
[Return to chapter overview](iworkspacepersistence_interface.htm)










Saves the window to workspaces.


 



Examples
--------




| ns |
| --- |
| // IWorkspacePersistence member. Required for saving window to workspaces
public void Save(XDocument document, XElement element)
{
     if (MainTabControl != null)
         MainTabControl.SaveToXElement(element);
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
 
 
 















 


Restore()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?nttabpage_restore.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt; [NTTabPage Class](nttabpage_class.htm) &gt;
Restore() | [Previous page](getheaderpart.htm)
[Return to chapter overview](nttabpage_class.htm)










Restores any elements in our NTTabPage from the workspace. (e.g. Selected accounts or instruments)


 



Examples
--------




| ns |
| --- |
| // NTTabPage member. Required for restoring elements from workspaces
public void Restore(XElement element)
{
     if (element == null)
         return;
 
     // Restore any elements you may have saved. e.g. selected accounts or instruments
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
 
 
 




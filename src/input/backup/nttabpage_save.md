










 


Save()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?nttabpage_save.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt; [NTTabPage Class](nttabpage_class.htm) &gt;
Save() | [Previous page](nttabpage_restore.htm)
[Return to chapter overview](nttabpage_class.htm)










Saves elements in our NTTabPage to the workspace (e.g. Selected accounts or instruments)


 



Examples
--------




| ns |
| --- |
| // NTTabPage member. Required for saving elements to workspaces
public void Save(XElement element)
{
     if (element == null)
         return;
 
     // Save any elements you may want persisted. e.g. selected accounts or instruments
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
 
 
 















 


OnRestoreValues()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?onrestorevalues.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [SuperDOM Column](superdom_column.htm) &gt;
OnRestoreValues() | [Previous page](superdomcolumn_onrender.htm)
[Return to chapter overview](superdom_column.htm)










Definition
----------


Called when the column is restored (e.g. from a workspace).  All public properties in a SuperDOM Column are saved to the workspace upon closing and selecting save.  You may choose to do something explicit with a certain property when the OnRestoreValues() method is called.


 


Method Return Value
-------------------


This method does not return a value


 


Syntax
------


You may override the method in your SuperDOM column with the following syntax:
------------------------------------------------------------------------------



public override void OnRestoreValues()  

{  

     

}



Parameters
----------


This method does not require any parameters



Examples
--------




| ns |
| --- |
| public override void OnRestoreValues()
{
   // Do something with the restored values. Can also trigger a repaint via OnPropertyChanged()
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
 
 
 















 


NinjaScript Editor Components







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?ns_editor_components.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Editor](editor.htm) &gt;
NinjaScript Editor Components | [Previous page](nodoc.htm)
[Return to chapter overview](editor.htm)










Overview
--------


The NinjaScript Editor is a powerful scripting editor that allows you to create custom indicators, strategies, and any other custom NinjaScript types used to enhance the NinjaTrader platform.  The NinjaScript Editor can be opened by selecting the New menu from the NinjaTrader Control Center. Then left mouse click on the menu item NinjaScript Editor


 


1. NinjaScript Explorer - Displays files, folders, and allows for additional file management


2. Tool bar - Moving your mouse over each icon will display the function of the icon button


3. Line numbers


4. Line modification marking - Yellow flags indicate unsaved line modifications where green flags indicate saved modifications


5. Tabs for creating new scripts via the [NinjaScript wizard](ns_wizard.htm) and working on multiple scripts.


 


     ![NS_Editor_1](ns_editor_1.png)


 


Context Menus
-------------


Context menus can be opened by right-clicking in the NinjaScript Editor.


 


![NinjaScriptEditorContextMenu](ninjascripteditorcontextmenu.png)


 


 




|  |  |
| --- | --- |
| Context Menu Items |  |
| Save | Saves pending changes to the currently open NinjaScript |
| Save As | Creates a copy of the script and attempts to rename the class name so the new script is unique |
| Insert Code Snippet | Inserts a code snippet (see [Code Snippets](code_snippets.htm) for more information) |
| Go To Line... | Moves the cursor to the line of code specified. |
| Undo | Undoes the last modification |
| Redo | Applies the modification that was last Undone |
| Cut | Removes selected text and copies to clipboard |
| Copy | Copies selected text to clipboard |
| Paste | Pastes the text saved in the clipboard |
| Remove | Removes the selected text |
| Select All | Selects all text in the Code Editor |
| Debug Mode | Sets if a debug dll should be generated on compilation (see [Visual Studio Debugging](visual_studio_debugging.htm) for more information)  |
| References... | Opens the list of dll references used by NinjaTrader. This includes dll's used by NinjaTrader and dll's installed with custom Add On's. |
| Show Warnings | Enables Warning messages to be seen alongside compile errors |
| Always On Top | Sets the  NinjaScript Editor to viewed on top of other windows |
| Print | Allows printing the content of this window (see [Printing Content](printing_content.htm) for more information)  |
| Share | Allows sharing the content of this window (see [Sharing Content](sharing_content.htm) for more information)  |
| Properties | Opens the Properties menu (see below) |





Properties and Definitions
--------------------------



NinjaTrader_2020-12-03_10-03-00
-------------------------------





|  |  |
| --- | --- |
| General |  |
| Auto hide NinjaScript explorer | Sets if the NinjaScript explorer should be collapsed by default |
| Debug mode | Sets if a debug dll should be generated on compilation (see [Visual Studio Debugging](visual_studio_debugging.htm) for more information) |
| Inline syntax checking | Sets if errors and warnings should be detected as code is written (without needing to compile) |
| Auto bracket completion | Sets if opening characters should automatically bed appended closing characters. Works for (parentheses), [brackets], {braces}, <angled brackets=""> |
| Show indentation lines | Displays vertical lines for code formatting |
| Show Warnings | Sets if code warnings should be show on compilation.   |
| Font | Sets the font options |
| Window |  |
| Always on top | Sets if the window will be always on top of other windows. |



 





 
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
 
 
 



</angled>
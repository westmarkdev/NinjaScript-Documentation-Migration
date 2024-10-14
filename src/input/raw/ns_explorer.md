










 


NinjaScript Explorer







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?ns_explorer.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Editor](editor.htm) &gt;
NinjaScript Explorer | [Previous page](ns_editor_components.htm)
[Return to chapter overview](editor.htm)



[Show/Hide Hidden Text](javascript:HMToggleExpandAll(!HMAnyToggleOpen()) "Click to open/close expanding sections")









The NinjaScript Explorer provides a Folder view of all the supported NinjaScript categories that can be developed in NinjaTrader.  


![tog_minus](tog_minus.gif)        [Understanding the NinjaScript Explorer display](javascript:HMToggle('toggle','UnderstandingTheNinjascriptExplorerDisplay','UnderstandingTheNinjascriptExplorerDisplay_ICON'))




|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Folder Displays
The NinjaScript Explorer will organize each script installed on your system by type of NinjaScript object (Indicator, Strategy, SuperDOM Column, etc).  Each folder will display the following scripts under each category:
 


|  |  |
| --- | --- |
| 1. Locked scripts | Pre-built system scripts which come installed with NinjaTrader which can be viewed as read-only and are required for compilation (of course you can safe a custom copy of those to modify) |
| 2. Custom scripts | Any script imported, or under development, which can be modified |
| 3. Ignored custom scripts | Custom scripts which have been excluded from compilation (see the "Excluding a script from compilation" section below for more information) |



 
NS_Editor_17
 
Pinning the NinjaScript Explorer
1.  By default the NinjaScript Explorer will be "pinned" to the right side of the NinjaScript editor, however it can be collapsed out of view by pressing the pin icon NS_Editor_14 located at the top right of the explorer window. 
 
 NS_Editor_12
 
2. Once the NinjaScript Explorer is collapsed, you can quickly bring it back in view simply by selecting the NinjaTrader Explorer tab located on the right side. Selecting the pin icon NS_Editor_15 again will re-pin the NinjaScript Explorer to the NinjaScript Editor.
 
NS_Editor_13
 
Right Click Menu
Right clicking on an individual folder or script will give you a number of different menu items to help with the management of your custom scripts.
 
NS_Editor_16
 


|  |  |
| --- | --- |
| New | Opens the [NinjaScript Wizard](ns_wizard.htm) for the relevant object type. |
| Open | Opens the selected script in a new tab in the current NinjaScript Editor window |
| Open In New NinjaScript Editor | Opens the selected script(s) in a new NinjaScript Editor window |
| Exclude From Compilation | Prevents the selected script(s) from being compiled (see the "Excluding a script from compilation" section below for more information) |
| Remove | Removes the current file or folder from the system |
| New Folder | Creates a new custom folder to organize your scripts |
| Rename | Renames the current selected file or folder |


 |



![tog_minus](tog_minus.gif)        [Managing scripts and folders](javascript:HMToggle('toggle','ManagingScriptsAndFolders','ManagingScriptsAndFolders_ICON'))




|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Opening an existing Script
There are two ways to open a script:
 
1.  Double left mouse click on the script you wish to view or edit in the current window
2.  Right mouse click on the script and select open to view or edit the script as a tab the current window, or select Open in NinjaScript Editor to open the script as a tab in a new window
 
Creating new scripts
Right clicking on a NinjaScript category and selecting New... will open the NinjaScript wizard allowing you to create new custom scripts.  
 
Please see the Help Topic on the [NinjaScript Wizard](ns_wizard.htm) for more information.
 
Creating custom folders
The NinjaScript Explorer gives you the flexibility to relocate and organize your custom scripts in a number of custom user defined folders.
 
•To create a new folder, simply right click on the NinjaScript folder category you wish to organize, select New Folder, and use your keyboard to type a user defined name to identify the folder. 
NS_Editor_18
 
Once you have created your new folder, using your mouse you can drag and drop any custom scripts of it's category under this folder.
 


|  |
| --- |
| Notes:  
1.You cannot relocate a locked system script. 2.You can only relocate a custom script if it is closed from the NinjaScript Editor.3.You can only relocate a script to a folder under it's own folder category (i.e., custom strategies can only be placed under the strategy folder, it would not be possible to move it to an indicator folder)4.If you move a child script that is called by a parent, please be sure to update the references to the child as well, as the new folder you assigned will automatically move the child to a new namespace |



 
Renaming scripts and folders
There are two methods for renaming custom scripts:
 
1. Right mouse click on the script from the NinjaScript explorer and select Rename.  
2. Select the desired script and press the F2 key on your keyboard
 
Renaming a script will automatically rename all relevant class names and all other required components.
 


|  |
| --- |
| Notes:  
1. You cannot rename a locked system script or folder.
2. You can only rename a custom script when it is closed.  
3. You can only rename a folder if all of the scripts contained are closed. |



 
Removing scripts and folders
There are two methods for removing custom scripts from your system
 
1. Right mouse click on the script from the NinjaScript explorer and select Remove  
2. Select the desired script and press the DEL key on your keyboard
 
Removing a script will completely delete the script from your system.  This action cannot be undone.
 


|  |
| --- |
| Notes:  
1. You cannot delete a locked system script or folder.
2. Removing a custom folder will delete all of the scripts contained within |



 
Understanding Folders in the NinjaScript Editor and the File System
When you create a folder in the NinjaScript Editor, it will also be created in the file system on your PC. For example, if you were to create a sub-folder named "MyScripts" in the existing "Indicators" folder, a sub-folder would also be created in the Documents\NinjaTrader 8\bin\Custom\Indicators folder. Once a sub-folder is created, scripts can be created or moved in that folder using the same processes outlined above.
 


|  |
| --- |
| Warning: Changes to Sub-folders directly through the file system will NOT be reflected in the NinjaScript Editor. Creating and editing folders must be performed within the NinjaScript Editor. |


 |



![tog_minus](tog_minus.gif)        [Excluding a script from compilation](javascript:HMToggle('toggle','ExcludingAScriptFromCompilation','ExcludingAScriptFromCompilation_ICON'))




|  |  |  |
| --- | --- | --- |
| Ignoring a script
There may be situations where you have a custom script installed on your system that is preventing other scripts from compiling due to [errors](compile_errors.htm).  The reason for this is that NinjaTrader will compile ALL custom NinjaScript files into a single DLL for performance reasons.  If you find you have installed a script that is giving you errors that you cannot resolve, or you're currently in the middle of developing a script which is unable to compile, you can easily ignore these files from the compiler from the NinjaScript editor.
 
•To ignore a script, right click on script name and select Exclude From Compilation  
When a script is ignored, it will be faded from the NinjaScript explorer to indicate that it will not be compiled.
 
NS_Editor_19
 
To include this script for the next compilation, simply right click on the script from the NinjaScript Explorer and uncheck Exclude From Compilation 
 


|  |
| --- |
| Note:  You cannot excluded a locked system script or folder |



 


|  |
| --- |
| Tip:  You will also find an option to exclude scripts from compilation by right clicking on the listed of errors generated at the bottom of the NinjaScript editor |



 
•Selecting Exclude From Compilation will ignore only the NinjaScript file selected•Selecting Exclude All From Compilation will exclude all the NinjaScript files currently with errors 
NS_Editor_20 |






 
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
 
 
 


HMInitToggle('UnderstandingTheNinjascriptExplorerDisplay\_ICON','hm.type','dropdown','hm.state','0','hm.src0','tog\_plus.gif','hm.src1','tog\_minus.gif','onclick','HMToggle(\'toggle\',\'UnderstandingTheNinjascriptExplorerDisplay\',\'UnderstandingTheNinjascriptExplorerDisplay\_ICON\')');
HMInitToggle('UnderstandingTheNinjascriptExplorerDisplay','hm.type','dropdown','hm.state','0');
HMInitToggle('ManagingScriptsAndFolders\_ICON','hm.type','dropdown','hm.state','0','hm.src0','tog\_plus.gif','hm.src1','tog\_minus.gif','onclick','HMToggle(\'toggle\',\'ManagingScriptsAndFolders\',\'ManagingScriptsAndFolders\_ICON\')');
HMInitToggle('ManagingScriptsAndFolders','hm.type','dropdown','hm.state','0');
HMInitToggle('ExcludingAScriptFromCompilation\_ICON','hm.type','dropdown','hm.state','0','hm.src0','tog\_plus.gif','hm.src1','tog\_minus.gif','onclick','HMToggle(\'toggle\',\'ExcludingAScriptFromCompilation\',\'ExcludingAScriptFromCompilation\_ICON\')');
HMInitToggle('ExcludingAScriptFromCompilation','hm.type','dropdown','hm.state','0');




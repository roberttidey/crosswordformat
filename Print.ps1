Start-Process -Filepath  $args[0] -Verb Print
$wshell = New-Object -ComObject wscript.shell;
$wshell.AppActivate("Print Pictures")
Start-Sleep -Seconds 2
$wshell.SendKeys("{ENTER}")
Start-Sleep -Seconds 5

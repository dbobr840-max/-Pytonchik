Set WshShell = CreateObject("WScript.Shell")

If WScript.Arguments.Count > 0 Then
    filePath = WScript.Arguments(0)
    
    On Error Resume Next
    WshShell.Run "code """ & filePath & """", 1, False
    If Err.Number = 0 Then
        WScript.Quit
    End If
    
    Err.Clear
    WshShell.Run "notepad """ & filePath & """", 1, False
Else
    MsgBox "No file specified"
End If
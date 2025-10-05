Set WshShell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")

' Получаем путь к файлу из аргументов
If WScript.Arguments.Count > 0 Then
    filePath = WScript.Arguments(0)
    
    ' Проверяем установлен ли VS Code через реестр
    On Error Resume Next
    vsCodePath = ""
    Err.Clear
    vsCodePath = WshShell.RegRead("HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\Code.exe\")
    
    If Err.Number = 0 And vsCodePath <> "" Then
        ' Открываем в VS Code
        WshShell.Run """" & vsCodePath & """ """ & filePath & """", 1, False
    Else
        ' Очищаем ошибку
        Err.Clear
        
        ' Проверяем установлен ли VS Code в пользовательском реестре
        vsCodePath = WshShell.RegRead("HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\Code.exe\")
        
        If Err.Number = 0 And vsCodePath <> "" Then
            ' Открываем в VS Code
            WshShell.Run """" & vsCodePath & """ """ & filePath & """", 1, False
        Else
            ' Проверяем установлен ли Notepad++
            Err.Clear
            nppPath = WshShell.RegRead("HKEY_LOCAL_MACHINE\SOFTWARE\Notepad++\")
            
            If Err.Number = 0 Then
                ' Находим путь к notepad++.exe
                nppExePath = "C:\Program Files\Notepad++\notepad++.exe"
                If fso.FileExists(nppExePath) Then
                    WshShell.Run """" & nppExePath & """ """ & filePath & """", 1, False
                Else
                    nppExePath = "C:\Program Files (x86)\Notepad++\notepad++.exe"
                    If fso.FileExists(nppExePath) Then
                        WshShell.Run """" & nppExePath & """ """ & filePath & """", 1, False
                    Else
                        OpenInNotepad(filePath)
                    End If
                End If
            Else
                ' Открываем в блокноте
                OpenInNotepad(filePath)
            End If
        End If
    End If
Else
    MsgBox "Не указан файл для открытия"
End If

Function OpenInNotepad(filePath)
    ' Пробуем найти другие редакторы
    On Error Resume Next
    
    ' Пробуем Notepad2
    Set shellApp = CreateObject("Shell.Application")
    set folders = shellApp.NameSpace(0)
    
    ' Просто открываем в стандартном блокноте
    WshShell.Run "notepad.exe """ & filePath & """", 1, False
End Function
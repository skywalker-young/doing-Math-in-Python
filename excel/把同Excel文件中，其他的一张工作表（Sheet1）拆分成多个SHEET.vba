####
###http://club.excelhome.net/thread-1340148-1-1.html
#
' 把同Excel文件中，其他的一张工作表（Sheet1）拆分成多个SHEET
'
Sub 拆分成多个SHEET()
Application.ScreenUpdating = False
Application.DisplayAlerts = False
Dim arr As Variant
Dim i, s As Integer
Dim brr()
Dim d As Object
Set d = CreateObject("scripting.dictionary")
Dim sh As Worksheet
For Each sh In Worksheets
If sh.Name <> "扫" And sh.Name <> "执行按钮" Then    '指定需保留几个工作表Sheet
sh.Delete
End If
Next sh
'arr = ActiveSheet.Range("a1").CurrentRegion
arr = Sheets(2).Range("a1").CurrentRegion           '将“扫”工作表里的源数据，放进数组
For i = 2 To UBound(arr)
d(arr(i, 1)) = ""
Next i
For Each k In d.keys
Worksheets.Add after:=Worksheets(Worksheets.Count)
        ActiveSheet.Name = k
ReDim brr(1 To UBound(arr), 1 To UBound(arr, 2))
n = 0
For i = 2 To UBound(arr)
If arr(i, 1) = k Then
n = n + 1
For s = 1 To UBound(arr, 2)
brr(n, s) = arr(i, s)
Next s
End If
Next i
Sheets(k).Range("a1").Resize(1, UBound(arr, 2)) = arr
  Sheets(k).Range("a2").Resize(UBound(brr), UBound(brr, 2)) = brr
  For i = 1 To UBound(arr, 2)
Sheets(k).Columns(i).ColumnWidth = Sheets("扫").Columns(i).ColumnWidth
  Next i
  Next k
Sheets("扫").Select
Application.DisplayAlerts = True
Application.ScreenUpdating = True

End Sub

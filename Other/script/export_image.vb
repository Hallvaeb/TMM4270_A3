Imports System
Imports NXOpen

Module NXJournal
Sub Main (ByVal args() As String) 

Dim theSession As NXOpen.Session = NXOpen.Session.GetSession()
Dim workPart As NXOpen.Part = theSession.Parts.Work

Dim displayPart As NXOpen.Part = theSession.Parts.Display

' ----------------------------------------------
'   Menu: File->Export->Image...
' ----------------------------------------------
Dim markId1 As NXOpen.Session.UndoMarkId = Nothing
markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")

Dim theUI As NXOpen.UI = NXOpen.UI.GetUI()

Dim imageExportBuilder1 As NXOpen.Gateway.ImageExportBuilder = Nothing
imageExportBuilder1 = theUI.CreateImageExportBuilder()

imageExportBuilder1.RegionMode = False

Dim regiontopleftpoint1(1) As Integer
regiontopleftpoint1(0) = 0
regiontopleftpoint1(1) = 0
imageExportBuilder1.SetRegionTopLeftPoint(regiontopleftpoint1)

imageExportBuilder1.RegionWidth = 1

imageExportBuilder1.RegionHeight = 1

imageExportBuilder1.FileFormat = NXOpen.Gateway.ImageExportBuilder.FileFormats.Png

imageExportBuilder1.FileName = ".\Product_images\"+FILENAME+".png"

imageExportBuilder1.BackgroundOption = NXOpen.Gateway.ImageExportBuilder.BackgroundOptions.Original

imageExportBuilder1.EnhanceEdges = False

Dim nXObject1 As NXOpen.NXObject = Nothing
nXObject1 = imageExportBuilder1.Commit()

theSession.DeleteUndoMark(markId1, "Export Image")

imageExportBuilder1.Destroy()

End Sub
End Module
import os
import brainstim.seeg_models as SEEG

scirun_bin = os.path.normpath("C:/PROGRA~1/SCIRun_5.0/bin/SCIRun.exe")
scirun_net_dir = os.path.normpath("D:\Code\Chantel\brainstim\data\scirun_nets")

subject = "c765c3"
subject_dir = os.path.normpath(os.path.join("D:/Data/Chantel/UW", subject))
# subject_dir = os.path.normpath(os.path.join("D:\Data", subject))

x = SEEG.SeegClass(scirun_bin, scirun_net_dir, subject, subject_dir)
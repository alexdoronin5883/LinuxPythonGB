   # команда вывода списка файлов (l)
   def test_step6(self, clear_folders, make_files, start_time):
       res = []
       res.append(ssh_checkout(data["ip"], data["user"], data["passwd"], "cd {}; 7z a "
           "{}/arx2".format(data["folder_in"], data["folder_out"]), "Everything is Ok"))
       for item in make_files:
           res.append(ssh_checkout(data["ip"], data["user"], data["passwd"], "cd {}; 7z l"
           " arx2.7z".format(data["folder_out"], data["folder_ext"]), item))
       self.save_log(start_time, "log6.txt")
       assert all(res), "test6 FAIL"

  # команда разархивирования с путями (x)
   def test_step7(self, clear_folders, make_files, make_subfolder, start_time):
       res = []
       res.append(ssh_checkout(data["ip"], data["user"], data["passwd"], "cd {}; 7z a "
           "{}/arx".format(data["folder_in"], data["folder_out"]), "Everything is Ok"))
       res.append(ssh_checkout(data["ip"], data["user"], data["passwd"], "cd {};"
           " 7z x arx.7z -o{} -y".format(data["folder_out"], data["folder_ext2"]), "Everything is Ok"))
     
  # команды расчёта хеша (h)
   def test_step9(self, clear_folders, make_files, start_time):
       res  = []
       res.append(ssh_checkout(data["ip"], data["user"], data["passwd"], "cd {}; 7z  a {}/arx -t{} ".format(data["folder_in"],
                                                                                                data["folder_out"], data["type"]),
                               "Everything is Ok"))
       for item in make_files:
           res.append(ssh_checkout(data["ip"], data["user"], data["passwd"], "cd {}; 7z h {}".format(data["folder_in"],
                                                                                                     item),
                                   "Everything is Ok"))
           hash = ssh_getout(data["ip"], data["user"], data["passwd"], "cd {}; "
                                                                       "crc32 {}".format(data["folder_in"],
                                                                                         item)).upper()
           res.append(ssh_checkout(data["ip"], data["user"], data["passwd"], "cd {}; 7z h {}".format(data["folder_in"],
                                                                                                     item), hash))
       assert all(res), "test9 FAIL"
